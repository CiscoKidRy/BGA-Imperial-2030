"""Imperial 2030 test engine.

Numbers come from the English booklet (BGG file 50631) and the empty board
photo 574713. Map moves exist only for borders named in the booklet or the
Quick Intro. Other borders are absent on purpose.
"""

from __future__ import annotations

NATIONS = ["russia", "china", "india", "brazil", "usa", "europe"]
LABEL = {
    "russia": "Russia",
    "china": "China",
    "india": "India",
    "brazil": "Brazil",
    "usa": "United States",
    "europe": "Europe",
}
COLOR = {
    "russia": "purple",
    "china": "yellow",
    "india": "black",
    "brazil": "green",
    "usa": "red",
    "europe": "blue",
}
MARK = {"russia": "R", "china": "C", "india": "I", "brazil": "B", "usa": "U", "europe": "E"}
CODE = {"russia": "RU", "china": "CN", "india": "IN", "brazil": "BR", "usa": "US", "europe": "EU"}
SPACE_NAME = [
    "Factory",
    "Production, after Factory",
    "Maneuver, before Investor",
    "Investor",
    "Import",
    "Production, after Import",
    "Maneuver, before Taxation",
    "Taxation",
]
ARMIES = {"china": 10, "usa": 6, "russia": 8, "india": 8, "brazil": 8, "europe": 8}
FLEETS = {"china": 6, "usa": 10, "russia": 8, "india": 8, "brazil": 8, "europe": 8}
RONDEL = [
    "Factory",
    "Production",
    "Maneuver",
    "Investor",
    "Import",
    "Production",
    "Maneuver",
    "Taxation",
]
BONDS = [(1, 2), (2, 4), (3, 6), (4, 9), (5, 12), (6, 16), (7, 20), (8, 25), (9, 30)]
CASH = {2: 37, 3: 25, 4: 19, 5: 15, 6: 13}
TAX_MIN = [0, 6, 8, 10, 11, 12, 13, 14, 15, 16, 18]
TAX_BONUS = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
TAX_POWER = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# kind, starts_with_factory. Squares start occupied. Circles do not.
# Shapes are from crops of image 574713. Quick Intro confirms the occupied pairs
# for every nation except India's harbor square, which is the Mumbai crop.
CITIES = {
    "usa": [("San Francisco", "harbor", False), ("Chicago", "armament", True), ("New York", "harbor", False), ("New Orleans", "harbor", True)],
    "brazil": [("Manaus", "armament", False), ("Brasilia", "armament", True), ("Fortaleza", "harbor", False), ("Rio de Janeiro", "harbor", True)],
    "europe": [("London", "harbor", True), ("Paris", "armament", True), ("Berlin", "armament", False), ("Rome", "harbor", False)],
    "russia": [("Murmansk", "harbor", False), ("Moscow", "armament", True), ("Novosibirsk", "armament", False), ("Vladivostok", "harbor", True)],
    "china": [("Urumqi", "armament", False), ("Beijing", "armament", True), ("Chongqing", "armament", False), ("Shanghai", "harbor", True)],
    "india": [("New Delhi", "armament", True), ("Mumbai", "harbor", True), ("Kolkata", "harbor", False), ("Chennai", "armament", False)],
}

# Borders named in the booklet or the Quick Intro. This is not the whole map.
LAND = [
    ("New Orleans", "Mexico"),
    ("Rome", "Turkey"),
    ("Paris", "London"),
    ("Kolkata", "Indochina"),
    ("Kolkata", "Chongqing"),
    ("Vladivostok", "Korea"),
]
SEA = [
    ("North Atlantic", "Caribbean Sea"),
    ("North Atlantic", "Gulf of Guinea"),
    ("North Atlantic", "Mediterranean Sea"),
    ("Caribbean Sea", "North Pacific"),
    ("Mediterranean Sea", "Indian Ocean"),
    ("North Pacific", "Sea of Japan"),
    ("North Pacific", "China Sea"),
    ("South Pacific", "China Sea"),
    ("South Pacific", "Tasman Sea"),
]
HARBOR = [
    ("London", "North Atlantic"),
    ("Rome", "Mediterranean Sea"),
    ("Vladivostok", "Sea of Japan"),
    ("Rio de Janeiro", "South Atlantic"),
]
COAST = [
    ("Japan", "Sea of Japan"),
    ("Indonesia", "Indian Ocean"),
    ("Indonesia", "Tasman Sea"),
    ("Indonesia", "China Sea"),
]
CANAL = {
    ("Caribbean Sea", "North Pacific"): "Colombia",
    ("North Pacific", "Caribbean Sea"): "Colombia",
    ("Mediterranean Sea", "Indian Ocean"): "North Africa",
    ("Indian Ocean", "Mediterranean Sea"): "North Africa",
}
SEAS = [
    "North Pacific", "South Pacific", "Caribbean Sea", "North Atlantic",
    "Mediterranean Sea", "Gulf of Guinea", "South Atlantic", "Indian Ocean",
    "China Sea", "Sea of Japan", "Tasman Sea",
]
NEUTRAL = [
    "Mexico", "Turkey", "Indochina", "Korea", "Japan", "Indonesia",
    "Colombia", "North Africa",
]


def factor(points: int) -> int:
    if points <= 5:
        return 0
    if points <= 10:
        return 1
    if points <= 15:
        return 2
    if points <= 20:
        return 3
    if points <= 24:
        return 4
    return 5


def tax_index(revenue: int) -> int:
    idx = 0
    for i, minimum in enumerate(TAX_MIN):
        if revenue >= minimum:
            idx = i
    return idx


def _adj(pairs):
    graph = {}
    for a, b in pairs:
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)
    return graph


LAND_ADJ = _adj(LAND)
SEA_ADJ = _adj(SEA)
HARBOR_ADJ = _adj(HARBOR)
COAST_ADJ = _adj(COAST)


class Game:
    def __init__(self, names: list[str]):
        if not 2 <= len(names) <= 6:
            raise ValueError("Imperial 2030 is for 2 to 6 players")
        self.names = list(names)
        self.n = len(names)
        self.cash = [CASH[self.n]] * self.n
        self.bonds = {p: [] for p in range(self.n)}  # (nation, interest, price)
        self.pile = {nat: list(BONDS) for nat in NATIONS}
        self.treasury = {nat: 0 for nat in NATIONS}
        self.controller = {nat: None for nat in NATIONS}
        self.power = {nat: 0 for nat in NATIONS}
        self.marker = {nat: None for nat in NATIONS}
        self.factories = {}  # city -> kind
        self.armies = []  # (nation, region, hostile)
        self.fleets = []  # (nation, region) region is a sea, or a city while in harbor
        self.flags = {}  # region -> nation
        self.supply_a = dict(ARMIES)
        self.supply_f = dict(FLEETS)
        self.supply_flag = {nat: 15 for nat in NATIONS}
        self.factory_pool = {"armament": 12, "harbor": 12}
        self.investor = None
        self.swiss = [False] * self.n
        self.log = []
        self.over = False
        self.winner = None
        self.draft_nation = 0
        self.draft_i = 0
        self.leader = 0
        self.turn = 0
        self.phase = "draft"
        self.pending = None
        self.rondel_choice = None
        self.limit_note = (
            "This is a local test of the experienced setup, not the published board. "
            "Fleet and army moves are only offered across borders named in the booklet or the Quick Intro. "
            "Panama's west mouth is not drawn. "
            "Convoy, factory destruction, the 15-flag replacement choice, and both variants are not in this test. "
            "A peace offer ends the battle without asking each defender. "
            "If the government cannot cover interest from personal cash, the unpaid part remains. "
            "The booklet does not name who leads India, Brazil, the United States, or Europe. This test rotates that lead."
        )
        for nat, cities in CITIES.items():
            for city, kind, start in cities:
                if start:
                    self.factories[city] = kind
                    self.factory_pool[kind] -= 1
        self._log(f"Experienced setup. Each player has {CASH[self.n]} million. Russia is chosen first.")

    def _log(self, text: str) -> None:
        self.log.append(text)

    def _bond_rows(self, seat: int) -> list[dict]:
        rows = []
        for nat, interest, price in self.bonds[seat]:
            rows.append({"nation": nat, "label": LABEL[nat], "code": CODE[nat], "interest": interest, "price": price})
        return rows

    def _actor_seat(self):
        if self.over:
            return None
        if self.phase == "draft":
            return self._draft_seat()
        if self.phase == "swiss-veto":
            return self.pending["ask"][0]
        if self.phase == "investor-buy":
            return self.pending["buyer"]
        if self.phase == "battle":
            return self.pending["ask"]
        if self.phase == "rondel":
            return self.controller[self._active_nation()]
        if self.phase in ("bond-pick", "import", "maneuver", "flags", "production-confirm", "tax-confirm"):
            return self.controller[self.pending["nation"]]
        return None

    def _legal_for(self, legal: list[dict], actor, viewer) -> list[dict]:
        """Other seats see public costs. They do not see a personal-cash block, and they get no buttons."""
        if viewer == actor:
            return legal
        shown = []
        for item in legal:
            if item.get("role") in ("primary", "alert", "secondary"):
                continue
            copy = dict(item)
            if item.get("privateBlock"):
                copy["enabled"] = True
                copy["privateBlock"] = False
                copy["detail"] = item.get("publicDetail") or item["detail"]
            shown.append(copy)
        return shown

    def _seat_name(self, seat: int) -> str:
        return self.names[seat]

    def _gov(self, nat: str):
        return self.controller[nat]

    def _credit(self, seat: int, nat: str) -> int:
        return sum(price for owner_nat, _interest, price in self.bonds[seat] if owner_nat == nat)

    def _interest_of(self, seat: int, nat: str) -> int:
        return sum(interest for owner_nat, interest, _price in self.bonds[seat] if owner_nat == nat)

    def _interest_due(self, nat: str) -> int:
        return sum(self._interest_of(seat, nat) for seat in range(self.n))

    def _home(self, city: str):
        for nat, cities in CITIES.items():
            for name, _kind, _start in cities:
                if name == city:
                    return nat
        return None

    def _city_kind(self, city: str):
        for cities in CITIES.values():
            for name, kind, _start in cities:
                if name == city:
                    return kind
        return None

    def _hostile_in(self, region: str) -> bool:
        return any(reg == region and hostile for _nat, reg, hostile in self.armies)

    def _rail_open(self, nat: str, city: str) -> bool:
        return self._home(city) == nat and not self._hostile_in(city)

    def view(self, seat: int | None) -> dict:
        show_cash = self.over
        you = None
        if seat is not None and 0 <= seat < self.n:
            you = {
                "seat": seat,
                "name": self.names[seat],
                "cash": self.cash[seat],
                "bonds": self._bond_rows(seat),
                "swiss": self.swiss[seat],
                "investor": self.investor == seat,
            }
        players = []
        for i, name in enumerate(self.names):
            players.append({
                "seat": i,
                "name": name,
                "bonds": self._bond_rows(i),
                "swiss": self.swiss[i],
                "investor": self.investor == i,
                "nations": [LABEL[nat] for nat in NATIONS if self.controller[nat] == i],
                "cash": self.cash[i] if (show_cash or seat == i) else None,
            })
        nations = []
        for nat in NATIONS:
            gov = self.controller[nat]
            best = max(self._credit(s, nat) for s in range(self.n))
            issued = best > 0
            pile = sorted(self.pile[nat], key=lambda pair: pair[1])
            top = None if not pile else {"interest": pile[0][0], "price": pile[0][1], "left": len(pile)}
            armament = sum(1 for city, kind in self.factories.items() if kind == "armament" and self._home(city) == nat)
            harbor = sum(1 for city, kind in self.factories.items() if kind == "harbor" and self._home(city) == nat)
            armies_out = sum(1 for owner, _reg, _h in self.armies if owner == nat)
            fleets_out = sum(1 for owner, _reg in self.fleets if owner == nat)
            flags_out = sum(1 for owner in self.flags.values() if owner == nat)
            pf = factor(self.power[nat])
            nations.append({
                "id": nat,
                "label": LABEL[nat],
                "mark": MARK[nat],
                "code": CODE[nat],
                "color": COLOR[nat],
                "treasury": self.treasury[nat],
                "power": self.power[nat],
                "factor": None if self.power[nat] == 0 else pf,
                "factorText": "" if self.power[nat] == 0 else f"x{pf}",
                "government": self.names[gov] if gov is not None else "no government",
                "credit": (self._credit(gov, nat) if gov is not None else best) if issued else None,
                "interest": self._interest_due(nat) if issued else None,
                "pile": [{"interest": a, "price": b} for a, b in pile],
                "topBond": top,
                "factories": {"armament": armament, "harbor": harbor},
                "armies": {"board": armies_out, "supply": self.supply_a[nat]},
                "fleets": {"board": fleets_out, "supply": self.supply_f[nat]},
                "flags": {"board": flags_out, "supply": self.supply_flag[nat]},
                "rondel": None if self.marker[nat] is None else SPACE_NAME[self.marker[nat]],
                "rondelIndex": self.marker[nat],
                "active": self.phase != "draft" and not self.over and NATIONS[self.turn] == nat,
            })
        banner, steps, legal = self._prompt(seat)
        actor = self._actor_seat()
        banner = dict(banner)
        banner["actor"] = actor
        banner["decision"] = banner.get("decision", banner["sentence"])
        if actor is not None and seat != actor and not self.over:
            banner["waiting"] = True
            banner["sentence"] = f"Waiting for {self.names[actor]}: {banner['decision']}"
        else:
            banner["waiting"] = False
        legal = self._legal_for(legal, actor, seat)
        return {
            "banner": banner,
            "steps": steps,
            "legal": legal,
            "players": players,
            "nations": nations,
            "you": you,
            "log": self.log[-40:],
            "over": self.over,
            "scores": self._scores() if self.over else None,
            "limit": self.limit_note,
            "map": self._map(),
            "tax": {"min": TAX_MIN, "bonus": TAX_BONUS, "power": TAX_POWER},
            "rondelOrder": SPACE_NAME,
            "choice": self.rondel_choice,
        }

    def _scores(self) -> list[dict]:
        rows = []
        for seat in range(self.n):
            bond_points = 0
            for nat, interest, _price in self.bonds[seat]:
                bond_points += interest * factor(self.power[nat])
            rows.append({
                "name": self.names[seat],
                "bonds": bond_points,
                "cash": self.cash[seat],
                "total": bond_points + self.cash[seat],
            })
        return rows

    def _map(self) -> list[dict]:
        rows = []
        for nat, cities in CITIES.items():
            for city, kind, _start in cities:
                rows.append(self._region_row(city, "home", nat, kind))
        for sea in SEAS:
            rows.append(self._region_row(sea, "sea", None, None))
        for name in NEUTRAL:
            rows.append(self._region_row(name, "neutral", None, None))
        return rows

    def _region_row(self, name, kind, nation, city_kind) -> dict:
        armies = [
            {"nation": nat, "hostile": hostile}
            for nat, reg, hostile in self.armies if reg == name
        ]
        fleets = [nat for nat, reg in self.fleets if reg == name]
        return {
            "name": name,
            "kind": kind,
            "nation": nation,
            "cityKind": city_kind,
            "factory": self.factories.get(name),
            "flag": self.flags.get(name),
            "armies": armies,
            "fleets": fleets,
            "railBlocked": bool(nation and self._hostile_in(name)),
        }

    def _prompt(self, seat):
        if self.over:
            nation = ""
            for nat in NATIONS:
                if self.power[nat] >= 25:
                    nation = LABEL[nat]
                    break
            return (
                {
                    "who": "No one",
                    "nation": nation,
                    "phase": "Game over",
                    "sentence": f"Game over: {nation} reached 25.",
                    "decision": f"Game over: {nation} reached 25.",
                },
                [],
                [],
            )
        if self.phase == "draft":
            return self._draft_prompt()
        if self.phase == "swiss-veto":
            return self._veto_prompt()
        if self.phase == "investor-buy":
            return self._buy_prompt()
        if self.phase == "bond-pick":
            return self._bond_prompt()
        if self.phase == "production-confirm":
            return self._production_prompt()
        if self.phase == "tax-confirm":
            return self._tax_prompt()
        if self.phase == "import":
            return self._import_prompt()
        if self.phase == "maneuver":
            return self._maneuver_prompt()
        if self.phase == "battle":
            return self._battle_prompt()
        if self.phase == "flags":
            return self._flag_prompt()
        if self.phase == "rondel":
            return self._rondel_prompt()
        if self.phase == "stalled":
            return (
                {
                    "who": "No one",
                    "nation": "None",
                    "phase": "Setup",
                    "sentence": "No nation has a government, so no rondel turn opens.",
                    "decision": "No nation has a government, so no rondel turn opens.",
                },
                [],
                [],
            )
        return (
            {"who": "", "nation": "", "phase": self.phase, "sentence": "Waiting."},
            [],
            [],
        )

    def _draft_leader(self) -> int:
        # Russia: start player. China: the player to their left.
        # Later nations: the booklet says "in the same way" and does not name the seat.
        # This test rotates one seat per nation and says so on the banner.
        return (self.leader + self.draft_nation) % self.n

    def _draft_seat(self) -> int:
        return (self._draft_leader() + self.draft_i) % self.n

    def _draft_prompt(self):
        nat = NATIONS[self.draft_nation]
        seat = self._draft_seat()
        named = self.draft_nation < 2
        decision = f"Choose one {LABEL[nat]} bond, or pass."
        if not named:
            decision += " The booklet does not name who leads this nation. This test rotates the lead."
        sentence = f"{self.names[seat]}, {decision[0].lower()}{decision[1:]}"
        legal = []
        for interest, price in self.pile[nat]:
            afford = self.cash[seat] >= price
            legal.append({
                "id": f"buy:{nat}:{price}",
                "label": f"price {price} · interest {interest}",
                "detail": "You cannot pay it." if not afford else "Pays the printed price into the treasury.",
                "publicDetail": f"price {price} · interest {interest}",
                "enabled": afford,
                "privateBlock": not afford,
                "role": "choice",
                "primary": False,
            })
        legal.append({
            "id": "pass",
            "label": "Pass",
            "detail": "Take no bond in this nation.",
            "enabled": True,
            "role": "primary",
            "primary": True,
        })
        steps = [
            {"id": nat, "label": LABEL[nat], "state": "now" if i == self.draft_nation else ("done" if i < self.draft_nation else "later")}
            for i, nat in enumerate(NATIONS)
        ]
        return (
            {"who": self.names[seat], "nation": LABEL[nat], "phase": "Setup", "sentence": sentence, "decision": decision},
            steps,
            legal,
        )

    def _active_nation(self) -> str:
        return NATIONS[self.turn]

    def _rondel_cost(self, start: int | None, dest: int, pf: int) -> tuple[int, int]:
        if start is None:
            return 0, 0
        steps = (dest - start) % 8
        return steps, max(0, steps - 3) * (1 + pf)

    def _rondel_prompt(self):
        nat = self._active_nation()
        gov = self.controller[nat]
        pf = factor(self.power[nat])
        start = self.marker[nat]
        first = start is None
        selected = self.rondel_choice
        if selected is not None:
            steps, cost = self._rondel_cost(start, selected, pf)
            if first:
                decision = f"Confirm {SPACE_NAME[selected]}. The first turn costs nothing."
            else:
                unit = "space" if steps == 1 else "spaces"
                decision = f"Confirm {SPACE_NAME[selected]} ({steps} {unit}, cost {cost})."
        elif first:
            decision = (
                f"First turn for {LABEL[nat]}. The octagon is in the hub. "
                "Any of the eight spaces may be chosen. The move is not limited to six spaces, and it costs nothing."
            )
        elif start == 3 and pf == 2:
            decision = "On Investor, factor 2, choosing Taxation (4 spaces, cost 3) or Factory (5 spaces, cost 6)."
        else:
            decision = (
                f"On {SPACE_NAME[start]}, factor {pf}. "
                "Move clockwise 1 to 6 spaces. The first 3 cost 0."
            )
        legal = []
        for index in range(8):
            steps, cost = self._rondel_cost(start, index, pf)
            if not first and not 1 <= steps <= 6:
                continue
            afford = self.cash[gov] >= cost
            passes = (not first) and self._passes_investor(start, index)
            tag = "any" if first else f"{steps} spaces, cost {cost}"
            detail = tag
            if not afford:
                detail = f"Costs {cost} million. You cannot pay it."
            elif passes:
                detail = f"{tag}. Pass over Investor. Interest is not paid."
            legal.append({
                "id": f"rondel:{index}",
                "label": SPACE_NAME[index],
                "detail": detail,
                "publicDetail": tag + (". Pass over Investor. Interest is not paid." if passes else ""),
                "enabled": afford,
                "privateBlock": not afford,
                "role": "choice",
                "primary": False,
                "cost": cost,
                "steps": None if first else steps,
                "selected": selected == index,
                "passes": passes,
            })
        if selected is not None:
            chosen = next(item for item in legal if item["selected"])
            legal.append({
                "id": "confirm",
                "label": "Place here" if first else "Confirm move",
                "detail": chosen["label"],
                "enabled": chosen["enabled"],
                "role": "primary",
                "primary": True,
            })
            legal.append({
                "id": "cancel",
                "label": "Cancel",
                "detail": "Clear the selected space.",
                "enabled": True,
                "role": "alert",
                "primary": False,
            })
        return (
            {
                "who": self.names[gov],
                "nation": LABEL[nat],
                "phase": "Rondel",
                "sentence": decision,
                "decision": decision,
            },
            [],
            legal,
        )

    def _passes_investor(self, start: int, dest: int) -> bool:
        steps = (dest - start) % 8
        for step in range(1, steps):
            if RONDEL[(start + step) % 8] == "Investor":
                return True
        return False

    def _veto_prompt(self):
        seat = self.pending["ask"][0]
        nat = self.pending["nation"]
        holders = len(self.pending["ask"])
        decision = f"stop {LABEL[nat]} on Investor?"
        sentence = f"{self.names[seat]}, {decision}"
        legal = [
            {"id": "force", "label": "Stop on Investor", "detail": "The nation lands on Investor and the cost is recalculated.", "enabled": True, "role": "primary", "primary": True},
            {"id": "allow", "label": "Let it pass", "detail": "The chosen space still happens.", "enabled": True, "role": "secondary", "primary": False},
        ]
        return (
            {
                "who": self.names[seat],
                "nation": LABEL[nat],
                "phase": "Rondel",
                "sentence": sentence,
                "decision": decision,
                "swissIndex": f"Swiss Bank 1 of {holders}",
            },
            [{"id": "veto", "label": "Swiss Bank", "state": "now"}],
            legal,
        )

    def _gift(self, seat: int, action: str) -> dict:
        _tag, nat, amount_s = action.split(":")
        amount = int(amount_s)
        if self.controller[nat] != seat:
            raise ValueError("You can add cash only to a nation you govern")
        if amount < 1 or self.cash[seat] < amount:
            raise ValueError("That amount is not in your cash")
        self.cash[seat] -= amount
        self.treasury[nat] += amount
        self._log(f"{self.names[seat]} adds {amount} million to the {LABEL[nat]} treasury.")
        return self.view(seat)

    def _act_draft(self, seat: int, action: str) -> None:
        nat = NATIONS[self.draft_nation]
        if action == "pass":
            self._log(f"{self.names[seat]} passes on {LABEL[nat]}.")
        elif action.startswith("buy:"):
            _tag, nation, price_s = action.split(":")
            price = int(price_s)
            if nation != nat:
                raise ValueError("That bond is from another nation")
            found = next((pair for pair in self.pile[nat] if pair[1] == price), None)
            if found is None:
                raise ValueError("That bond is gone")
            if self.cash[seat] < price:
                raise ValueError("You cannot afford that bond")
            self.pile[nat].remove(found)
            self.cash[seat] -= price
            self.treasury[nat] += price
            self.bonds[seat].append((nat, found[0], found[1]))
            self._log(f"{self.names[seat]} buys {LABEL[nat]} {found[1]} million, interest {found[0]}.")
        else:
            raise ValueError("Choose a bond or pass")
        self.draft_i += 1
        if self.draft_i >= self.n:
            self.draft_i = 0
            self.draft_nation += 1
            if self.draft_nation >= 6:
                self._finish_setup()

    def _finish_setup(self) -> None:
        for nat in NATIONS:
            self._assign_government(nat, initial=True)
        russia = self.controller["russia"]
        china = self.controller["china"]
        if russia is not None:
            self.investor = (russia + 1) % self.n
        elif china is not None:
            self.investor = (china + 1) % self.n
        else:
            self.investor = 0
            self._log("Neither Russia nor China has a government. The Investor card starts at the start player.")
        self._refresh_swiss()
        self.phase = "rondel"
        self.turn = 0
        self._skip_unowned()
        self._log(f"{self.names[self.investor]} holds the Investor card.")

    def _assign_government(self, nat: str, initial: bool = False) -> None:
        scores = [(self._credit(seat, nat), seat) for seat in range(self.n)]
        best = max(score for score, _seat in scores)
        if best == 0:
            self.controller[nat] = None
            return
        holders = [seat for score, seat in scores if score == best]
        current = self.controller[nat]
        if current is not None and self._credit(current, nat) == best:
            return
        if len(holders) == 1:
            self.controller[nat] = holders[0]
            self._log(f"{self.names[holders[0]]} governs {LABEL[nat]}.")
            return
        if initial or self.investor is None:
            self.controller[nat] = None
            self._log(f"{LABEL[nat]} is tied. Nobody governs it yet.")
            return
        order = [(self.investor + i) % self.n for i in range(self.n)]
        for seat in order:
            if seat in holders:
                self.controller[nat] = seat
                self._log(f"{self.names[seat]} governs {LABEL[nat]} on the seating tiebreak.")
                return

    def _refresh_swiss(self) -> None:
        governs = {self.controller[nat] for nat in NATIONS if self.controller[nat] is not None}
        for seat in range(self.n):
            if seat in governs:
                if self.swiss[seat]:
                    self.swiss[seat] = False
                    self._log(f"{self.names[seat]} returns the Swiss Bank.")
            elif not self.swiss[seat]:
                self.swiss[seat] = True
                self._log(f"{self.names[seat]} receives a Swiss Bank.")

    def _skip_unowned(self) -> None:
        for _ in range(6):
            nat = self._active_nation()
            if self.controller[nat] is not None and not self.over:
                return
            self._log(f"{LABEL[nat]} has no government and is skipped.")
            self.turn = (self.turn + 1) % 6
        else:
            self.phase = "stalled"
            self._log("No nation has a government. The rondel does not open.")

    def _act_rondel(self, seat: int, action: str) -> None:
        nat = self._active_nation()
        if action == "cancel":
            self.rondel_choice = None
            return
        if action == "confirm":
            if self.rondel_choice is None:
                raise ValueError("Choose a space first")
            dest = self.rondel_choice
            self.rondel_choice = None
            self._start_rondel_move(seat, nat, dest)
            return
        if not action.startswith("rondel:"):
            raise ValueError("Choose a rondel space")
        dest = int(action.split(":")[1])
        start = self.marker[nat]
        pf = factor(self.power[nat])
        steps, cost = self._rondel_cost(start, dest, pf)
        if start is not None and not 1 <= steps <= 6:
            raise ValueError("That space is not 1 to 6 clockwise")
        if self.cash[seat] < cost:
            raise ValueError("You cannot pay the rondel cost")
        self.rondel_choice = dest

    def _start_rondel_move(self, seat: int, nat: str, dest: int) -> None:
        start = self.marker[nat]
        pf = factor(self.power[nat])
        steps, cost = self._rondel_cost(start, dest, pf)
        if start is not None and not 1 <= steps <= 6:
            raise ValueError("That space is not 1 to 6 clockwise")
        if self.cash[seat] < cost:
            raise ValueError("You cannot pay the rondel cost")
        passes = start is not None and self._passes_investor(start, dest)
        if passes and self.treasury[nat] >= self._interest_due(nat):
            ask = [s for s in range(self.n) if self.swiss[s]]
            if ask:
                start_from = self.investor if self.investor is not None else 0
                ask.sort(key=lambda s: (s - start_from) % self.n)
                self.pending = {"nation": nat, "dest": dest, "cost": cost, "ask": ask, "passed": True}
                self.phase = "swiss-veto"
                return
        self._commit_rondel(nat, dest, cost, passes)

    def _act_veto(self, action: str) -> None:
        if action == "force":
            nat = self.pending["nation"]
            start = self.marker[nat]
            dest = (start + 1) % 8
            while RONDEL[dest] != "Investor":
                dest = (dest + 1) % 8
            steps = (dest - start) % 8
            cost = max(0, steps - 3) * (1 + factor(self.power[nat]))
            gov = self.controller[nat]
            if self.cash[gov] < cost:
                raise ValueError("The government cannot pay to stop on Investor")
            self._log(f"{self.names[self.pending['ask'][0]]} forces {LABEL[nat]} to stop on Investor.")
            self.pending = None
            self._commit_rondel(nat, dest, cost, False)
            return
        if action != "allow":
            raise ValueError("Force the stop or allow the pass")
        self.pending["ask"].pop(0)
        if self.pending["ask"]:
            return
        nat = self.pending["nation"]
        dest = self.pending["dest"]
        cost = self.pending["cost"]
        self.pending = None
        self._commit_rondel(nat, dest, cost, True)

    def _commit_rondel(self, nat: str, dest: int, cost: int, passed: bool) -> None:
        gov = self.controller[nat]
        if cost:
            self.cash[gov] -= cost
            self._log(f"{self.names[gov]} pays {cost} million to move {LABEL[nat]} on the rondel.")
        self.marker[nat] = dest
        space = RONDEL[dest]
        self._log(f"{LABEL[nat]} lands on {space}.")
        self.pending = {"nation": nat, "passed": passed, "space": space}
        self._begin_space(nat, space)

    def _begin_space(self, nat: str, space: str) -> None:
        if space == "Factory":
            self._do_factory(nat)
        elif space == "Production":
            self._do_production(nat)
        elif space == "Import":
            self.pending["picked"] = []
            self.phase = "import"
        elif space == "Maneuver":
            self.pending["sub"] = "fleet"
            self.pending["moved"] = []
            self.phase = "maneuver"
        elif space == "Investor":
            self._pay_interest(nat)
            if self.over:
                return
            self._open_invest(nat, pay_two=True)
        elif space == "Taxation":
            self._do_tax(nat)
        else:
            raise ValueError(space)

    def _after_space(self) -> None:
        if self.over:
            return
        passed = self.pending and self.pending.get("passed")
        nat = self.pending["nation"] if self.pending else self._active_nation()
        if passed and not self.over:
            self._open_invest(nat, pay_two=True)
            return
        self._next_nation()

    def _open_invest(self, nat: str, pay_two: bool) -> None:
        if self.over:
            return
        buyer = self.investor
        if pay_two:
            self.cash[buyer] += 2
            self._log(f"{self.names[buyer]} receives 2 million from the bank for the Investor card.")
        queue = []
        if pay_two:
            queue.append(buyer)
        start = self.investor
        for step in range(1, self.n):
            seat = (start + step) % self.n
            if self.swiss[seat] and seat != self.investor:
                queue.append(seat)
        if not queue:
            self._finish_investor()
            return
        self.pending = {"nation": nat, "queue": queue, "buyer": queue[0], "passed": False}
        self.phase = "investor-buy"

    def _buy_prompt(self):
        seat = self.pending["buyer"]
        holds_card = seat == self.investor
        sentence = (
            f"{self.names[seat]}, buy one new bond in any nation, upgrade one bond, or pass."
            if holds_card
            else f"{self.names[seat]} has a Swiss Bank and may invest once, or pass. There is no 2 million payment."
        )
        decision = (
            "Buy one new bond in any nation, upgrade one bond of the same nation, or pass."
            if holds_card
            else "Swiss Bank: invest once, or pass. There is no 2 million payment."
        )
        sentence = f"{self.names[seat]}, {decision[0].lower()}{decision[1:]}"
        legal = [{"id": "pass", "label": "Do not invest", "detail": "Skip this investment.", "enabled": True, "role": "primary", "primary": True}]
        for nat in NATIONS:
            owned = [bond for bond in self.bonds[seat] if bond[0] == nat]
            for interest, price in self.pile[nat]:
                afford = self.cash[seat] >= price
                legal.append({
                    "id": f"new:{nat}:{price}",
                    "label": f"New {LABEL[nat]} price {price}",
                    "detail": "You cannot pay it." if not afford else f"Interest {interest}. Pay {price}.",
                    "publicDetail": f"Interest {interest}. Price {price}.",
                    "enabled": afford,
                    "privateBlock": not afford,
                    "role": "choice",
                    "primary": False,
                })
                for _n, _old_interest, old_price in owned:
                    if price <= old_price:
                        continue
                    diff = price - old_price
                    afford_up = self.cash[seat] >= diff
                    legal.append({
                        "id": f"up:{nat}:{old_price}:{price}",
                        "label": f"Upgrade {LABEL[nat]} {old_price} to {price}",
                        "detail": "You cannot pay it." if not afford_up else f"Pay the difference, {diff}.",
                        "publicDetail": f"Difference {diff}.",
                        "enabled": afford_up,
                        "privateBlock": not afford_up,
                        "role": "choice",
                        "primary": False,
                    })
        return (
            {"who": self.names[seat], "nation": "", "phase": "Investor", "sentence": sentence, "decision": decision},
            [
                {"id": "interest", "label": "1 Interest", "state": "done"},
                {"id": "card", "label": "2 Investor card", "state": "now"},
                {"id": "swiss", "label": "3 Swiss Bank", "state": "later"},
            ],
            legal,
        )

    def _act_invest(self, seat: int, action: str) -> None:
        if action == "pass":
            self._log(f"{self.names[seat]} does not invest.")
        elif action.startswith("new:"):
            _tag, nat, price_s = action.split(":")
            price = int(price_s)
            found = next((pair for pair in self.pile[nat] if pair[1] == price), None)
            if found is None or self.cash[seat] < price:
                raise ValueError("That bond cannot be bought")
            self.pile[nat].remove(found)
            self.cash[seat] -= price
            self.treasury[nat] += price
            self.bonds[seat].append((nat, found[0], found[1]))
            self._log(f"{self.names[seat]} buys {LABEL[nat]} {price} million, interest {found[0]}.")
        elif action.startswith("up:"):
            _tag, nat, old_s, new_s = action.split(":")
            old_price, new_price = int(old_s), int(new_s)
            owned = next((bond for bond in self.bonds[seat] if bond[0] == nat and bond[2] == old_price), None)
            found = next((pair for pair in self.pile[nat] if pair[1] == new_price), None)
            if owned is None or found is None or new_price <= old_price:
                raise ValueError("That upgrade is not available")
            diff = new_price - old_price
            if self.cash[seat] < diff:
                raise ValueError("You cannot afford the difference")
            self.bonds[seat].remove(owned)
            self.pile[nat].append((owned[1], owned[2]))
            self.pile[nat].sort(key=lambda pair: pair[1])
            self.pile[nat].remove(found)
            self.cash[seat] -= diff
            self.treasury[nat] += diff
            self.bonds[seat].append((nat, found[0], found[1]))
            self._log(f"{self.names[seat]} upgrades {LABEL[nat]} {old_price} to {new_price}, paying {diff}.")
        else:
            raise ValueError("Buy, upgrade, or pass")
        if action.startswith("new:") or action.startswith("up:"):
            self._assign_government(action.split(":")[1])
        self.pending["queue"].pop(0)
        if self.pending["queue"]:
            self.pending["buyer"] = self.pending["queue"][0]
            return
        self._finish_investor()

    def _finish_investor(self) -> None:
        for nat in NATIONS:
            self._assign_government(nat)
        self._refresh_swiss()
        holder = self.investor
        self.investor = (self.investor + 1) % self.n
        self._log(f"The Investor card passes to {self.names[self.investor]}.")
        self._next_nation()

    def _pay_interest(self, nat: str) -> None:
        gov = self.controller[nat]
        others = []
        own = self._interest_of(gov, nat) if gov is not None else 0
        for seat in range(self.n):
            if seat == gov:
                continue
            due = self._interest_of(seat, nat)
            if due:
                others.append((seat, due))
        for seat, due in others:
            paid = min(self.treasury[nat], due)
            self.treasury[nat] -= paid
            self.cash[seat] += paid
            rest = due - paid
            if rest and gov is not None:
                take = min(self.cash[gov], rest)
                if take:
                    self.cash[gov] -= take
                    self.cash[seat] += take
                    self._log(f"{self.names[gov]} pays {take} million to {self.names[seat]} for {LABEL[nat]} interest.")
                unpaid = rest - take
                if unpaid:
                    self._log(f"{LABEL[nat]} interest of {unpaid} million to {self.names[seat]} is unpaid in this test.")
            if paid:
                self._log(f"{LABEL[nat]} treasury pays {paid} million interest to {self.names[seat]}.")
        if own:
            paid = min(self.treasury[nat], own)
            self.treasury[nat] -= paid
            self.cash[gov] += paid
            self._log(f"{self.names[gov]} receives {paid} million interest and forgoes {own - paid}.")

    def _do_factory(self, nat: str) -> None:
        gov = self.controller[nat]
        if self.treasury[nat] < 5:
            self._log(f"{LABEL[nat]} cannot pay 5 million, so no factory is built.")
            self._after_space()
            return
        choices = []
        for city, kind, _start in CITIES[nat]:
            if city in self.factories:
                continue
            if self._hostile_in(city):
                continue
            if self.factory_pool[kind] < 1:
                continue
            choices.append((city, kind))
        if not choices:
            self._log(f"{LABEL[nat]} has no legal city for a factory.")
            self._after_space()
            return
        self.pending["choices"] = choices
        self.phase = "bond-pick"

    def _bond_prompt(self):
        nat = self.pending["nation"]
        gov = self.controller[nat]
        legal = []
        for city, kind in self.pending["choices"]:
            word = "armament" if kind == "armament" else "shipyard"
            legal.append({
                "id": f"city:{city}",
                "label": f"{city} ({word})",
                "detail": "Cost 5. The treasury pays the bank.",
                "enabled": True,
                "role": "choice",
                "region": city,
                "primary": not legal,
            })
        decision = f"Build one factory for {LABEL[nat]}. The treasury pays 5 million."
        return (
            {"who": self.names[gov], "nation": LABEL[nat], "phase": "Factory", "sentence": decision, "decision": decision},
            [{"id": "factory", "label": "Choose city", "state": "now"}],
            legal,
        )

    def _act_import(self, action: str) -> None:
        nat = self.pending["nation"]
        if action == "done":
            self._after_space()
            return
        if len(self.pending["picked"]) >= 3:
            raise ValueError("Import is limited to 3 units")
        if self.treasury[nat] < 1:
            raise ValueError("The treasury cannot pay 1 million")
        kind, region = action.split(":", 1)
        if kind == "army":
            if self._home(region) != nat or self._hostile_in(region) or self.supply_a[nat] < 1:
                raise ValueError("That army cannot be imported")
            self.supply_a[nat] -= 1
            self.armies.append((nat, region, False))
        elif kind == "fleet":
            if self._city_kind(region) != "harbor" or self._home(region) != nat or self._hostile_in(region) or self.supply_f[nat] < 1:
                raise ValueError("That fleet cannot be imported")
            self.supply_f[nat] -= 1
            self.fleets.append((nat, region))
        else:
            raise ValueError("Import an army or a fleet, or finish")
        self.treasury[nat] -= 1
        self.pending["picked"].append(action)
        self._log(f"{LABEL[nat]} imports a {kind} in {region}.")

    def _import_prompt(self):
        nat = self.pending["nation"]
        gov = self.controller[nat]
        count = len(self.pending["picked"])
        legal = [{"id": "done", "label": "Done importing", "detail": f"{count} of 3 bought.", "enabled": True, "role": "primary", "primary": count == 3 or self.treasury[nat] < 1}]
        if count < 3 and self.treasury[nat] >= 1:
            for city, kind, _start in CITIES[nat]:
                if self._hostile_in(city):
                    continue
                if self.supply_a[nat] > 0:
                    legal.append({"id": f"army:{city}", "label": f"Army in {city}", "detail": "1 million from the treasury.", "enabled": True, "role": "choice", "region": city, "primary": False})
                if kind == "harbor" and self.supply_f[nat] > 0:
                    legal.append({"id": f"fleet:{city}", "label": f"Fleet in {city}", "detail": "1 million from the treasury. Harbor only.", "enabled": True, "role": "choice", "region": city, "primary": False})
        if legal and not any(item["primary"] for item in legal):
            legal[0]["primary"] = True
        return (
            {"who": self.names[gov], "nation": LABEL[nat], "phase": "Import", "sentence": f"Buy up to 3 units for {LABEL[nat]}. Each costs 1 million from the treasury."},
            [{"id": "import", "label": f"Unit {count + 1 if count < 3 else 3}", "state": "now"}],
            legal,
        )

    def act_city(self, seat: int, action: str) -> None:
        nat = self.pending["nation"]
        if seat != self.controller[nat]:
            raise ValueError("Only the government builds")
        city = action.split(":", 1)[1]
        found = next((item for item in self.pending["choices"] if item[0] == city), None)
        if found is None:
            raise ValueError("That city is not legal")
        _city, kind = found
        self.treasury[nat] -= 5
        self.factory_pool[kind] -= 1
        self.factories[city] = kind
        self._log(f"{LABEL[nat]} builds a factory in {city}.")
        self._after_space()

    def _do_production(self, nat: str) -> None:
        builds = []
        for city, _kind, _start in CITIES[nat]:
            if city not in self.factories:
                continue
            if self._hostile_in(city):
                self._log(f"{city} is blocked by a hostile army.")
                continue
            built = self.factories[city]
            if built == "armament" and self.supply_a[nat] > 0:
                builds.append({"city": city, "unit": "army"})
            elif built == "harbor" and self.supply_f[nat] > 0:
                builds.append({"city": city, "unit": "fleet"})
            else:
                self._log(f"{LABEL[nat]} has no {built} piece left for {city}.")
        self.pending["builds"] = builds
        self.phase = "production-confirm"

    def _production_prompt(self):
        nat = self.pending["nation"]
        gov = self.controller[nat]
        builds = self.pending.get("builds") or []
        if builds:
            listed = ", ".join(f"{item['unit']} in {item['city']}" for item in builds)
            decision = f"Commit production: {listed}."
        else:
            decision = "No unit is produced."
        return (
            {"who": self.names[gov], "nation": LABEL[nat], "phase": "Production", "sentence": decision, "decision": decision},
            [{"id": "production", "label": "Production", "state": "now"}],
            [{"id": "commit", "label": "Commit production", "detail": decision, "enabled": True, "role": "primary", "primary": True}],
        )

    def _require_production(self, seat, action):
        nat = self.pending["nation"]
        if seat != self.controller[nat]:
            raise ValueError("Only the government produces")
        if action != "commit":
            raise ValueError("Commit production")
        for item in self.pending.get("builds") or []:
            if item["unit"] == "army" and self.supply_a[nat] > 0:
                self.supply_a[nat] -= 1
                self.armies.append((nat, item["city"], False))
                self._log(f"{LABEL[nat]} produces an army in {item['city']}.")
            elif item["unit"] == "fleet" and self.supply_f[nat] > 0:
                self.supply_f[nat] -= 1
                self.fleets.append((nat, item["city"]))
                self._log(f"{LABEL[nat]} produces a fleet in {item['city']}.")
        self._after_space()

    def _tax_preview(self, nat: str) -> dict:
        factories = [city for city in self.factories if self._home(city) == nat and not self._hostile_in(city)]
        flag_count = sum(1 for owner in self.flags.values() if owner == nat)
        revenue = min(23, 2 * len(factories) + flag_count)
        units = sum(1 for owner, _reg, _h in self.armies if owner == nat) + sum(1 for owner, _reg in self.fleets if owner == nat)
        treasury_after_revenue = self.treasury[nat] + revenue
        pay = min(treasury_after_revenue, units)
        column = tax_index(revenue)
        bonus = TAX_BONUS[column]
        gain = TAX_POWER[column]
        after_pay = treasury_after_revenue - pay
        paid_bonus = min(after_pay, bonus)
        return {
            "revenue": revenue,
            "pay": pay,
            "bonus": paid_bonus,
            "chartBonus": bonus,
            "gain": gain,
            "column": column,
            "header": TAX_MIN[column],
        }

    def _do_tax(self, nat: str) -> None:
        self.pending["tax"] = self._tax_preview(nat)
        self.phase = "tax-confirm"

    def _tax_prompt(self):
        nat = self.pending["nation"]
        gov = self.controller[nat]
        tax = self.pending["tax"]
        decision = (
            f"Check the four taxation results, then commit. "
            f"Revenue {tax['revenue']} uses header {tax['header']}. "
            f"Upkeep {tax['pay']}. Bonus {tax['bonus']}. Power +{tax['gain']}."
        )
        return (
            {"who": self.names[gov], "nation": LABEL[nat], "phase": "Taxation", "sentence": decision, "decision": decision},
            [
                {"id": "pay-in", "label": "1 Pay in", "state": "now"},
                {"id": "upkeep", "label": "2 Upkeep", "state": "later"},
                {"id": "bonus", "label": "3 Bonus", "state": "later"},
                {"id": "power", "label": "4 Power", "state": "later"},
            ],
            [{
                "id": "commit",
                "label": "Commit taxation",
                "detail": decision,
                "enabled": True,
                "role": "primary",
                "primary": True,
                "taxColumn": tax["column"],
            }],
        )

    def _require_tax(self, seat, action):
        nat = self.pending["nation"]
        if seat != self.controller[nat]:
            raise ValueError("Only the government taxes")
        if action != "commit":
            raise ValueError("Commit taxation")
        tax = self.pending["tax"]
        self.treasury[nat] += tax["revenue"]
        self.treasury[nat] -= tax["pay"]
        self.treasury[nat] -= tax["bonus"]
        gov = self.controller[nat]
        if gov is not None and tax["bonus"]:
            self.cash[gov] += tax["bonus"]
        self.power[nat] += tax["gain"]
        self._log(
            f"{LABEL[nat]} taxes {tax['revenue']}. Soldiers cost {tax['pay']}. "
            f"Bonus {tax['bonus']}. Power +{tax['gain']}, now {self.power[nat]}."
        )
        if self.power[nat] >= 25:
            self.power[nat] = 25
            self.over = True
            self._log(f"{LABEL[nat]} reaches 25. The game ends.")
            if self.pending and self.pending.get("passed"):
                self._log("Investor steps 2 and 3 are skipped because Taxation reaches 25.")
            return
        self._after_space()

    def _maneuver_prompt(self):
        nat = self.pending["nation"]
        gov = self.controller[nat]
        sub = self.pending["sub"]
        sentence = (
            f"Move {LABEL[nat]} fleets, or finish the fleet step. A fleet may stay."
            if sub == "fleet"
            else f"Move {LABEL[nat]} armies, or finish the army step. An army may stay."
        )
        legal = [{"id": "done", "label": "Finish this step", "detail": "Units that do not move stay where they are.", "enabled": True, "role": "primary", "primary": True}]
        if sub == "fleet":
            for index, (owner, region) in enumerate(self.fleets):
                if owner != nat or index in self.pending["moved"]:
                    continue
                for dest in self._fleet_destinations(region):
                    legal.append({
                        "id": f"fleet:{index}:{dest}",
                        "label": f"Fleet {region} to {dest}",
                        "detail": "One named sea, or out of a harbor.",
                        "enabled": True,
                        "role": "choice",
                        "region": dest,
                        "primary": False,
                    })
        else:
            for index, (owner, region, _hostile) in enumerate(self.armies):
                if owner != nat or index in self.pending["moved"]:
                    continue
                for dest in self._army_destinations(nat, region):
                    legal.append({
                        "id": f"army:{index}:{dest}",
                        "label": f"Army {region} to {dest}",
                        "detail": "Named border or open rail.",
                        "enabled": True,
                        "role": "choice",
                        "region": dest,
                        "primary": False,
                    })
        return (
            {"who": self.names[gov], "nation": LABEL[nat], "phase": "Maneuver", "sentence": sentence},
            [
                {"id": "fleet", "label": "1 Fleets", "state": "now" if sub == "fleet" else "done"},
                {"id": "army", "label": "2 Armies", "state": "now" if sub == "army" else "later"},
                {"id": "flags", "label": "3 Flags", "state": "later"},
            ],
            legal,
        )

    def _fleet_destinations(self, region: str) -> list[str]:
        dests = set(SEA_ADJ.get(region, set()))
        if self._home(region):
            dests |= HARBOR_ADJ.get(region, set())
        return sorted(dests)

    def _army_destinations(self, nat: str, region: str) -> list[str]:
        dests = set(LAND_ADJ.get(region, set()))
        if self._rail_open(nat, region):
            for city, _kind, _start in CITIES[nat]:
                if city != region and self._rail_open(nat, city):
                    dests.add(city)
        return sorted(dests)

    def _act_maneuver(self, action: str) -> None:
        nat = self.pending["nation"]
        if action == "done":
            if self.pending["sub"] == "fleet":
                self.pending["sub"] = "army"
                self.pending["moved"] = []
                return
            self._open_flags(nat)
            return
        kind, index_s, dest = action.split(":", 2)
        index = int(index_s)
        if kind == "fleet":
            owner, region = self.fleets[index]
            if owner != nat or dest not in self._fleet_destinations(region):
                raise ValueError("That fleet move is not on a named border")
            canal = CANAL.get((region, dest))
            self.fleets[index] = (owner, dest)
            self.pending["moved"].append(index)
            self._log(f"A {LABEL[nat]} fleet moves from {region} to {dest}.")
            if canal and self.flags.get(canal) not in (None, nat):
                self.pending["battle"] = {"kind": "canal", "region": dest, "from": region, "index": index, "controller": self.flags[canal]}
                owner_seat = self.controller[self.flags[canal]]
                self.pending["ask"] = owner_seat
                self.phase = "battle"
                return
            self._maybe_battle("fleet", dest, index)
            return
        if kind == "army":
            owner, region, hostile = self.armies[index]
            if owner != nat or dest not in self._army_destinations(nat, region):
                raise ValueError("That army move is not on a named border")
            self.armies[index] = (owner, dest, False)
            self.pending["moved"].append(index)
            self._log(f"A {LABEL[nat]} army moves from {region} to {dest}.")
            home = self._home(dest)
            if home and home != nat:
                self.pending["posture"] = index
                self.phase = "battle"
                self.pending["ask"] = self.controller[nat]
                self.pending["battle"] = {"kind": "posture", "index": index, "dest": dest}
                return
            self._maybe_battle("army", dest, index)
            return
        raise ValueError("Move a unit or finish the step")

    def _maybe_battle(self, kind: str, dest: str, index: int) -> None:
        nat = self.pending["nation"]
        if kind == "fleet":
            others = sorted({owner for owner, region in self.fleets if region == dest and owner != nat})
        else:
            others = sorted({owner for owner, region, _h in self.armies if region == dest and owner != nat})
        if not others:
            self.phase = "maneuver"
            return
        self.pending["battle"] = {"kind": kind, "dest": dest, "index": index, "others": others}
        self.pending["ask"] = self.controller[nat]
        self.phase = "battle"

    def _battle_prompt(self):
        battle = self.pending["battle"]
        nat = self.pending["nation"]
        if battle["kind"] == "posture":
            return (
                {"who": self.names[self.controller[nat]], "nation": LABEL[nat], "phase": "Entry", "sentence": f"The army entered {battle['dest']}. Choose hostile or friendly."},
                [{"id": "posture", "label": "Posture", "state": "now"}],
                [
                    {"id": "hostile", "label": "Hostile", "detail": "Stands and blocks the province.", "enabled": True, "role": "secondary", "primary": False},
                    {"id": "friendly", "label": "Friendly", "detail": "Lies down and does not block.", "enabled": True, "role": "secondary", "primary": False},
                ],
            )
        if battle["kind"] == "canal":
            owner = battle["controller"]
            return (
                {"who": self.names[self.controller[owner]], "nation": LABEL[owner], "phase": "Canal", "sentence": f"Allow the fleet through the canal controlled from {owner}?"},
                [{"id": "canal", "label": "Canal", "state": "now"}],
                [
                    {"id": "allow", "label": "Yes, allow", "detail": "The fleet completes the move.", "enabled": True, "role": "primary", "primary": True},
                    {"id": "deny", "label": "No, refuse", "detail": "The fleet returns to where it was.", "enabled": True, "role": "alert", "primary": False},
                ],
            )
        return (
            {"who": self.names[self.controller[nat]], "nation": LABEL[nat], "phase": "Battle", "sentence": "Demand a fight, or offer peace."},
            [{"id": "battle", "label": "Battle", "state": "now"}],
            [{"id": "peace", "label": "Do not fight", "detail": "In this test a peace offer ends the battle without asking each defender.", "enabled": True, "role": "secondary", "primary": False}]
            + [
                {"id": f"fight:{other}", "label": f"Demand a fight against {LABEL[other]}", "detail": "Remove one unit from each side.", "enabled": True, "role": "primary", "primary": True}
                for other in battle["others"]
            ],
        )

    def _act_battle(self, action: str) -> None:
        battle = self.pending["battle"]
        nat = self.pending["nation"]
        if battle["kind"] == "posture":
            owner, dest, _h = self.armies[battle["index"]]
            hostile = action == "hostile"
            if action not in ("hostile", "friendly"):
                raise ValueError("Choose hostile or friendly")
            self.armies[battle["index"]] = (owner, dest, hostile)
            self._log(f"The army in {dest} is {'hostile' if hostile else 'friendly'}.")
            self.pending.pop("battle")
            self._maybe_battle("army", dest, battle["index"])
            return
        if battle["kind"] == "canal":
            if action == "deny":
                owner, _dest = self.fleets[battle["index"]]
                self.fleets[battle["index"]] = (owner, battle["from"])
                self._log("The canal controller denies the passage.")
            elif action == "allow":
                self._log("The canal controller allows the passage.")
            else:
                raise ValueError("Allow or deny the canal")
            self.pending.pop("battle")
            self.phase = "maneuver"
            return
        if action == "peace":
            self._log("Peace is offered. The units remain together.")
            self.pending.pop("battle")
            self.phase = "maneuver"
            return
        if action.startswith("fight:"):
            other = action.split(":", 1)[1]
            self._remove_one(nat, battle["dest"], battle["kind"])
            self._remove_one(other, battle["dest"], battle["kind"])
            self._log(f"{LABEL[nat]} and {LABEL[other]} each lose one unit in {battle['dest']}.")
            self.pending.pop("battle")
            self.phase = "maneuver"
            return
        raise ValueError("Fight or offer peace")

    def _remove_one(self, nat: str, region: str, kind: str) -> None:
        if kind == "fleet":
            for index, (owner, reg) in enumerate(self.fleets):
                if owner == nat and reg == region:
                    self.fleets.pop(index)
                    self.supply_f[nat] += 1
                    return
        else:
            for index, (owner, reg, _h) in enumerate(self.armies):
                if owner == nat and reg == region:
                    self.armies.pop(index)
                    self.supply_a[nat] += 1
                    return

    def _open_flags(self, nat: str) -> None:
        self.pending = {"nation": nat, "passed": self.pending.get("passed", False)}
        self.phase = "flags"

    def _flag_prompt(self):
        nat = self.pending["nation"]
        gov = self.controller[nat]
        legal = [{"id": "done", "label": "Finish flags", "detail": "Leave the rest empty.", "enabled": True, "role": "primary", "primary": True}]
        if self.supply_flag[nat] > 0:
            for row in self._map():
                if row["kind"] == "home":
                    continue
                if row["flag"] == nat:
                    continue
                occupants = {a["nation"] for a in row["armies"]} | set(row["fleets"])
                if occupants == {nat}:
                    legal.append({
                        "id": f"flag:{row['name']}",
                        "label": f"Place flag in {row['name']}",
                        "detail": "This nation alone occupies it.",
                        "enabled": True,
                        "role": "choice",
                        "region": row["name"],
                        "primary": False,
                    })
        return (
            {"who": self.names[gov], "nation": LABEL[nat], "phase": "Flags", "sentence": "Place a flag on a region this nation occupies alone, or finish."},
            [{"id": "flags", "label": "Flags", "state": "now"}],
            legal,
        )

    def _act_flags(self, action: str) -> None:
        nat = self.pending["nation"]
        if action == "done":
            self._after_space()
            return
        if not action.startswith("flag:") or self.supply_flag[nat] < 1:
            raise ValueError("That flag cannot be placed")
        region = action.split(":", 1)[1]
        self.flags[region] = nat
        self.supply_flag[nat] -= 1
        self._log(f"{LABEL[nat]} places a flag in {region}.")

    def _next_nation(self) -> None:
        if self.over:
            return
        self.pending = None
        self.rondel_choice = None
        self.phase = "rondel"
        self.turn = (self.turn + 1) % 6
        self._skip_unowned()

    def act(self, seat: int, action: str) -> dict:
        if action.startswith("gift:"):
            return self._gift(seat, action)
        if self.over:
            raise ValueError("The game is over")
        if self.phase == "bond-pick":
            if not action.startswith("city:"):
                raise ValueError("Choose a city")
            self.act_city(seat, action)
            return self.view(seat)
        if self.phase == "tax-confirm":
            self._require_tax(seat, action)
            return self.view(seat)
        if self.phase == "production-confirm":
            self._require_production(seat, action)
            return self.view(seat)
        return self._act_dispatch(seat, action)

    def _act_dispatch(self, seat: int, action: str) -> dict:
        if self.over and not action.startswith("gift:"):
            raise ValueError("The game is over")
        if action.startswith("gift:"):
            return self._gift(seat, action)
        handler = {
            "draft": self._require_draft,
            "rondel": self._require_rondel,
            "swiss-veto": self._require_veto,
            "investor-buy": self._require_invest,
            "import": self._require_import,
            "maneuver": self._require_maneuver,
            "battle": self._require_battle,
            "flags": self._require_flags,
        }.get(self.phase)
        if handler is None:
            raise ValueError(f"No action in {self.phase}")
        handler(seat, action)
        return self.view(seat)

    def _require_draft(self, seat, action):
        if seat != self._draft_seat():
            raise ValueError(f"It is {self.names[self._draft_seat()]}'s choice")
        self._act_draft(seat, action)

    def _require_rondel(self, seat, action):
        nat = self._active_nation()
        if seat != self.controller[nat]:
            raise ValueError("Only the government moves the rondel")
        self._act_rondel(seat, action)

    def _require_veto(self, seat, action):
        if seat != self.pending["ask"][0]:
            raise ValueError("Waiting for a Swiss Bank holder")
        self._act_veto(action)

    def _require_invest(self, seat, action):
        if seat != self.pending["buyer"]:
            raise ValueError("Waiting for the investor")
        self._act_invest(seat, action)

    def _require_import(self, seat, action):
        if seat != self.controller[self.pending["nation"]]:
            raise ValueError("Only the government imports")
        self._act_import(action)

    def _require_maneuver(self, seat, action):
        if seat != self.controller[self.pending["nation"]]:
            raise ValueError("Only the government maneuvers")
        self._act_maneuver(action)

    def _require_battle(self, seat, action):
        if seat != self.pending["ask"]:
            raise ValueError("Waiting for the battle decision")
        self._act_battle(action)

    def _require_flags(self, seat, action):
        if seat != self.controller[self.pending["nation"]]:
            raise ValueError("Only the government places flags")
        self._act_flags(action)
