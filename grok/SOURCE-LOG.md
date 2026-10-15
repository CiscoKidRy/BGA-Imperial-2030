# Source log

Retrieved 2026-10-15. This list is the boundary for the SDLC plan. A later session adds a new row when it opens a new source.

## Email

Saved under `source-email/`, not committed.

| Message | Date in the header | Subject | What was read |
| --- | --- | --- | --- |
| 1a13dc3b90d959dd | Thu, 15 Oct 2026 06:13:19 +0200 | [BGA Studio] Welcome on BGA Studio | Plain text and HTML, entire files |
| 1a13ff0aa56e26e9 | Thu, 15 Oct 2026 16:21:39 +0200 | [BGA Studio] Board Game Arena password set | Plain text and HTML, entire files. The link was not opened |

Gmail search for Studio, SFTP, and `studio.boardgamearena.com` returned these two messages and no others.

## BGA pages whose raw wiki text was retrieved

- https://en.doc.boardgamearena.com/index.php?title=Studio&action=raw
- https://en.doc.boardgamearena.com/index.php?title=First_steps_with_BGA_Studio&action=raw
- https://en.doc.boardgamearena.com/index.php?title=BGA_Game_licenses&action=raw
- https://en.doc.boardgamearena.com/index.php?title=BGA_game_Lifecycle&action=raw
- https://en.doc.boardgamearena.com/index.php?title=Studio_file_reference&action=raw
- https://en.doc.boardgamearena.com/index.php?title=Create_a_game_in_BGA_Studio:_Complete_Walkthrough&action=raw — full text saved as `grok/source-docs/walkthrough-fetched.txt`. The first 30,720 characters were read in session. Headings through "After the alpha stage" were listed from the file. The body after "Implement Game Setup" was not read line by line except the headings and the sections from "Wrap Up" to the end.

## BGA pages that did not return the article

- https://en.doc.boardgamearena.com/Studio — HTML shell, title only
- https://boardgamearena.com/forum/viewtopic.php?f=12&t=15232 redirected to a page shell. The post text was retrieved from https://forum.boardgamearena.com/viewtopic.php?f=12&t=15232&lang=en. The post says to email studio@boardgamearena.com about the license except for smaller learning projects.
- https://en.doc.boardgamearena.com/index.php?title=Pre-release_checklist&action=raw — license-to-alpha sentence, image size limits, and the Request ALPHA status button were read
- https://en.doc.boardgamearena.com/index.php?title=Tools_and_tips_of_BGA_Studio&action=raw — port 2022 and the note that an uploaded SSH key disables password login were read
- https://studio.boardgamearena.com/licensing — opened 2026-10-15 after a website login. The page is a script shell. The data call was `POST /licensing/licensing/getLicensingPageData.html`.
- https://studio.boardgamearena.com/projects — opened the same way. The data call was `POST /projects/projects/getProjectsPageData.html`.
- Managed games for the logged-in account: `POST /studio/studio/getManagedGamesPageData.html`. The `games` array was empty and `userConfirmedBeingDev` was false.
- Login call: `POST /account/auth/loginUserWithPassword.html` as the Credential Manager user `ciscokidryan0`. The response `username` was CiscoKidRyan0 and `success` was true. The password was not saved.

## FileZilla site entry

Read from `%APPDATA%\FileZilla\sitemanager.xml` on 2026-10-15. The file was not modified. The `BGA Studio` server element stores Host `1.studio.boardgamearena.com`, Port `2022`, Protocol `1`, User `CiscoKidRyan`, Logontype `5`, the `bga-development-rsa-key` path, and this Dropbox folder as LocalDir. Its comment says the remote home is `/`. RemoteDir is stored as `1 0`. The user said a live key connection listed `/` and the folder was empty. A second server element named MacMini is in the same file. Its host and user were not copied into this repository.

## Presentation PDFs linked from the Studio page

Saved under `grok/source-docs/`, not committed.

| File | Pages extracted |
| --- | --- |
| 2-8-steps-to-realize.pdf | 1–10. Page 10 is the closing slide |
| 4-gamestates.pdf | 1–23. Page 23 is the summary slide |
| 5-guidelines.pdf | 1–8 only. Later pages were not extracted |
| 3-thebgaframework.pdf | 1–22. Extraction stops during "Making a move". Later pages were not extracted |
| 1-why-developing.pdf | Downloaded. Not extracted |

## SFTP

2026-10-15. Key login to `CiscoKidRyan@1.studio.boardgamearena.com` port 2022 succeeded. `pwd` returned `/`. `ls -la` showed that directory and no project folder. Password login was not tried.

## BoardGameGeek

| Request | Result |
| --- | --- |
| `https://api.geekdo.com/api/geekitems?objectid=54138&objecttype=thing` | HTTP 200. Saved as `grok/source-docs/bgg-geekitems-54138.json`. Identity fields checked in that file |
| `https://api.geekdo.com/api/files?objectid=54138&objecttype=thing&pageid=1&showcount=100` | HTTP 200. 28 files, one page |
| `https://api.geekdo.com/api/videos?objectid=54138&objecttype=thing&pageid=1&showcount=100` | HTTP 200. 35 videos, one page |
| images API with `gallery=game` | HTTP 200. `pagination.total` 144. Three pages saved. Captions in `bgg-image-captions.txt` |
| images API without `gallery`, as recorded by the flock catalog | `pagination.total` 217. Pages 3 and 4 of that request were not saved |
| `https://boardgamegeek.com/xmlapi2/thing?id=54138&stats=1` | HTTP 403. No rank, rating, or weight |
| HTML game page and file download URLs for the English rules and quick intro | HTTP 403. The PDFs were not saved |
| Wiki HTML `thing:54138:moreinfo` | A later fetch returned the differences text. An earlier direct download returned HTTP 403. The same differences text is in the geekitems `wiki` field |

The file-by-file catalog is `grok/flock/03-bgg-imperial-2030-catalog.md`.

## GitHub code pages opened far enough to quote

- https://raw.githubusercontent.com/PhilipDavis/BGA-Fled/main/LICENCE_BGA — full short license text
- Search results that returned repository file lists for elaskavaia/bga-sharedcode, danielholmes/bga-workbench, koenheltzel/bga-sevenwondersduel, ishermandom/bga-42, PhilipDavis/BGA-Fled, bga-his/bga-hereistand, danielholmes/battle-for-hill-218, and thoun/glow

Those repositories were not cloned.
