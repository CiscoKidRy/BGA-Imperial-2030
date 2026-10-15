"""Local playtest server for the Imperial 2030 rules engine.

It serves the schematic page and one in-memory game. It does not upload
anything to Board Game Arena.
"""

from __future__ import annotations

import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from engine import Game

ROOT = Path(__file__).resolve().parent
LOCK = threading.Lock()
GAMES: dict[str, Game] = {}
NEXT_ID = 1


def _read_json(handler: BaseHTTPRequestHandler) -> dict:
    length = int(handler.headers.get("Content-Length", "0"))
    if length <= 0:
        return {}
    raw = handler.rfile.read(length)
    data = json.loads(raw.decode("utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Expected an object")
    return data


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt: str, *args) -> None:
        return

    def _send(self, code: int, payload, content: str = "application/json; charset=utf-8") -> None:
        if isinstance(payload, bytes):
            body = payload
        else:
            body = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", content)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path in ("/", "/index.html"):
            self._send(200, (ROOT / "index.html").read_bytes(), "text/html; charset=utf-8")
            return
        if parsed.path.startswith("/api/game/"):
            game_id = parsed.path.split("/")[3]
            seat_text = parse_qs(parsed.query).get("seat", ["0"])[0]
            try:
                seat = int(seat_text)
            except ValueError:
                self._send(400, {"error": "Seat must be a number"})
                return
            with LOCK:
                game = GAMES.get(game_id)
                if game is None:
                    self._send(404, {"error": "No game with that id"})
                    return
                if not 0 <= seat < game.n:
                    self._send(400, {"error": "That seat is not in this game"})
                    return
                state = game.view(seat)
            state["id"] = game_id
            state["seat"] = seat
            self._send(200, state)
            return
        self._send(404, {"error": "Not found"})

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        try:
            data = _read_json(self)
        except (json.JSONDecodeError, ValueError) as exc:
            self._send(400, {"error": str(exc)})
            return
        if parsed.path == "/api/game":
            names = data.get("names")
            if not isinstance(names, list) or not all(isinstance(name, str) and name.strip() for name in names):
                self._send(400, {"error": "Names must be 2 to 6 non-empty strings"})
                return
            names = [name.strip() for name in names]
            try:
                game = Game(names)
            except ValueError as exc:
                self._send(400, {"error": str(exc)})
                return
            global NEXT_ID
            with LOCK:
                game_id = str(NEXT_ID)
                NEXT_ID += 1
                GAMES[game_id] = game
                state = game.view(0)
            state["id"] = game_id
            state["seat"] = 0
            self._send(200, state)
            return
        parts = parsed.path.strip("/").split("/")
        if len(parts) == 4 and parts[0] == "api" and parts[1] == "game" and parts[3] == "act":
            game_id = parts[2]
            try:
                seat = int(data["seat"])
                action = str(data["action"])
            except (KeyError, TypeError, ValueError):
                self._send(400, {"error": "Seat and action are required"})
                return
            with LOCK:
                game = GAMES.get(game_id)
                if game is None:
                    self._send(404, {"error": "No game with that id"})
                    return
                try:
                    state = game.act(seat, action)
                except ValueError as exc:
                    self._send(400, {"error": str(exc)})
                    return
            state["id"] = game_id
            state["seat"] = seat
            self._send(200, state)
            return
        self._send(404, {"error": "Not found"})


def main() -> None:
    server = ThreadingHTTPServer(("127.0.0.1", 8765), Handler)
    print("Imperial 2030 test at http://127.0.0.1:8765/", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
