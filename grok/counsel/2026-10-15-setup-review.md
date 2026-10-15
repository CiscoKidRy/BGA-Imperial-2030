# Counsel review, 2026-10-15

Reviewed the setup notes against the email files, the wiki fetches, and the geekitems JSON.

## Kept

- Welcome email facts used in the plan match the saved plain text and HTML: host, port 2022, SFTP user, database URL, ten studio usernames, and the lost-password link. Password values are not in the committed files.
- SFTP key login was observed. Remote `/` had no project folder.
- Geekitems fields in the plan were checked in `grok/source-docs/bgg-geekitems-54138.json` before that dump was left untracked.
- License, lifecycle, first steps, file reference, and walkthrough statements match the raw pages read in this session.
- These three lines were fetched again before they were added:
  - Tools and tips: SSH port 2022, and an uploaded SSH key disables password login.
  - Pre-release checklist: a license is required even to move to alpha. Image limits 4Mb and 15Mb.
  - Forum post `f=12&t=15232`: email studio@boardgamearena.com about the license except for smaller learning projects.

## Corrected

`grok/flock/01-email-word-for-word.md` first marked "SSH public key mentioned? YES" and "Game name mentioned? YES". The message bodies do not mention an SSH key or Imperial 2030. The words "ssh" and "public key" are in the dump header's search query. The correction is in that file.

## Not re-checked one by one

`grok/flock/04-github-bga-examples.md` lists repositories the GitHub pass reported as HTTP 200. This review did not open all of those repositories again. The eight repositories named in `SDLC-PLAN.md` were seen in search results during this session. The `LICENCE_BGA` text was fetched from the raw URL.
