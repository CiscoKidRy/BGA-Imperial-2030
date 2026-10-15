# Session instructions

Use these rules whenever work on this game resumes.

## Sources

- State a Board Game Arena or Imperial 2030 fact only when a file in this folder or a page opened in that session states it.
- Keep the URL or file path next to the fact.
- If a page fails, write that it failed. Do not fill the gap.
- The five presentation PDFs and the current wiki disagree where the wiki marks Dojo, `states.inc.php`, `material.inc.php`, and the view/template files as deprecated. Follow the current wiki for new code. Keep the PDF statement in the notes with the page that was read.
- Do not treat the BoardGameGeek short description, the wiki "differences" list, or a file description as the rulebook.

## Secrets

- SFTP password, database password, and the password-set code stay in `source-email/` or in the keys folder.
- Do not commit them, do not put them in a pull request, and do not paste them into a status note.
- The private key stays in `C:\Users\ryanh\Dropbox\Ryan\Key SSH API Private Public Security RSA\bga-development-rsa-key`.

## Revisions

- Edit in `C:\Users\ryanh\Dropbox\Ryan\AI-SI-Grok-Tools\BoardGameAreana - Imperial 2030`.
- Publish with the sequence in `README.md`: counsel review, commit, push, pull request, merge.
- When a Studio project exists, also use Control Panel / Manage Games / Commit my modifications now, after the first admin commit the First steps page describes.
- Publisher graphics and rule PDFs stay in `reference/` or `grok/source-docs/` and out of git.

## Counsel

Every review uses more than one agent. Each agent reads the change and the cited sources. The written review goes in `grok/counsel/` and is committed with the change, without secrets. A finding that a sentence is unsupported gets the sentence removed or sourced before merge.

## Studio

- SFTP host and port from the welcome email, confirmed by a successful key login on 2026-10-15: `1.studio.boardgamearena.com` port `2022`, user `CiscoKidRyan`.
- Create a project from Control Panel / Manage games. Do not invent a project folder on the server by hand. The First steps page says the folder appears after the project is created.
- First steps says the first project should be a tutorial. The walkthrough says to finish at least one tutorial before a real game, and names Reversi as the tutorial maintained by the BGA team.
- Test with Express start in Manual mode, using the ten studio accounts named in the welcome email. The welcome email says to log in as CiscoKidRyan0.

## Copyright

Board Game Arena's license page says an adaptation of a game that is not public domain is rejected at review if BGA does not hold the license. Imperial 2030 is a 2009 published game in the geekitems response. It is not marked public domain in any page read in this session. The code license text retrieved from https://raw.githubusercontent.com/PhilipDavis/BGA-Fled/main/LICENCE_BGA says rights in the idea and graphics stay with the licensor and the authors. That text is from that repository file, not from a BGA legal page fetched in this session.
