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
- No Studio game project was created. No game code was written. The English rules PDF was not downloaded.

## What is blocked

The license list does not contain Imperial 2030. The walkthrough says not to start a project until BGA has the licence, or the game will not be published. The license page allows a Studio project and says live submission is rejected without a license. The pre-release checklist requires a license even for alpha. On 15 October 2026 a license email was sent from ryanhocking@gmail.com to studio@boardgamearena.com. Gmail id `1a1402a52478094f`. The copy is `grok/sent/2026-10-15-studio-license.txt`. No reply has been retrieved.

The English rules file on BoardGameGeek returned HTTP 403. The BGG rank was not retrieved.

Do not create an Imperial 2030 project on Studio, and do not write rules code, until the reply to message `1a1402a52478094f` says to create it, or until the title appears on the licensing list.

## Next session

1. Read `SDLC-PLAN.md` gate table.
2. Do not create a Reversi or other tutorial project.
3. Do not open the password-set link in message `1a13ff0aa56e26e9` unless the user asks.
4. Wait for the reply to the studio@ license email before creating the Imperial project. Do not send a second copy unless the user asks.
5. The English rules PDF is still the next source to obtain. It is not in git.
