# Resume

Date of this session: 2026-10-15.

Read this file, then `SESSION-INSTRUCTIONS.md`, then `SDLC-PLAN.md`.

## What was requested

Build Imperial 2030, BoardGameGeek thing 54138, as a Board Game Arena Studio game. Keep revisions in git on GitHub and in this Dropbox folder. Before each commit, a counsel of agents reviews the change. The publish sequence is commit, push, pull request with a description, then merge.

## What is done

- RSA key created and SFTP key login tested. See the connection note in the keys folder. The remote home directory was `/` and contained no project folder. The user said the public key is uploaded. Tools and tips says that disables password SFTP.
- FileZilla Site Manager entry `BGA Studio` uses that key, host, port, and user. The user reported a live listing of `/` that was empty, and that FileZilla did not ask for the website password. A separate Site Manager entry named MacMini was not edited.
- Two BGA Studio emails were saved under `source-email/` (not in git). The welcome email is the one with SFTP and database values. The later email is a password-set link and was not opened.
- The Studio website password is in Windows Credential Manager, target `BGA Developer`. A login as CiscoKidRyan0 succeeded on 2026-10-15. The password was not written into this repository.
- Licensing and project data were retrieved the same day. Imperial 2030 is not in either list. This account's managed-games array is empty. The numbers and the other titles that matched a search for "imperial" are in `SDLC-PLAN.md` step 2.
- BGA Studio wiki pages and four of the five linked presentations were read to the extent recorded in `SOURCE-LOG.md`.
- BoardGameGeek identity, files, videos, and image captions were retrieved to the extent recorded in `SOURCE-LOG.md` and `flock/03-bgg-imperial-2030-catalog.md`.
- This repository and the working agreement in `README.md` were created. The repository is public. Revisions use GitHub only.
- The user rejected a Reversi tutorial as the next step. No tutorial project was created.
- A private Studio project named `imperialtwothousandthirty` was created on 15 October 2026. The form allows letters only, so the year could not be digits in the name. `bgg_id` 54138 is set. The generated folder is in this directory. Studio's creation commit is SVN revision 340706. `prod-version` is `-not deployed-`. No alpha request was sent. The code is still the generated skeleton.
- On 2026-10-15 the BoardGameGeek login in Credential Manager, target `BoardGameGeek.com`, user `cisco_kid`, downloaded the 28 files for thing 54138. They are under `reference/bgg/`, which git ignores. English rules file 50631 was read. All 217 gallery images were reviewed. The interface plan is `grok/ui-design-2026-10-15.md`. It is in this repository and it is not in the Studio game code.
- A local playtest, not a Studio upload, is in `playtest/`. `engine.py` runs the experienced setup. `server.py` serves `index.html` at `http://127.0.0.1:8765/`. Ten unit tests passed before pull request #5. The screen is now an original board arranged like empty-board photo 574713: scoring track on top, map in the middle, rondel in the South Pacific, tax chart on the ocean, and six nation trays. The publisher photo is not in git. A browser check on 2026-10-15 started a game, hid the other players' cash, rejected a click that was not a legal region, and did not scroll sideways at 390 pixels. The map only offers borders named in the booklet or the Quick Intro.
- Ava and Bo wrote `grok/counsel/2026-10-15-playtest-ava.md` and `grok/counsel/2026-10-15-playtest-bo.md`. The referee note is `grok/counsel/2026-10-15-playtest-referee.md`. Cy and Dee did not write notes. One-step rondel confirms say "space". Ava and Bo played before that wording was loaded.

## What is blocked

The license list does not contain Imperial 2030. The walkthrough says not to start a project until BGA has the licence, or the game will not be published. The license page allows a Studio project and says live submission is rejected without a license. The pre-release checklist requires a license even for alpha. On 15 October 2026 a license email was sent from ryanhocking@gmail.com to studio@boardgamearena.com. Gmail id `1a1402a52478094f`. The copy is `grok/sent/2026-10-15-studio-license.txt`. No reply has been retrieved.

The private project exists so Studio can be learned. Do not request alpha, do not deploy, and do not change it to public, until the reply to message `1a1402a52478094f` says it may be published. The English rules PDF has been read. The local playtest uses those rules. Do not copy them into Studio `Game.js` until a playtest counsel accepts that change.

## Next session

1. Read `SDLC-PLAN.md` gate table.
2. Do not create a Reversi or other tutorial project.
3. Do not open the password-set link in message `1a13ff0aa56e26e9` unless the user asks.
4. Keep the Studio project private. Do not send a second license email unless the user asks. The next learning steps are the copyright header, `gameinfos.jsonc` fields from the geekitems record, and Express Start in Manual mode.
5. The local test screen is `playtest/index.html`, served by `playtest/server.py`. Studio `Game.js` is still the skeleton. The rules PDFs stay out of git. Do not deploy.
