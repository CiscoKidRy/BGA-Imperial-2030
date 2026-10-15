# SDLC plan: Imperial 2030 on Board Game Arena

This is a plan. No Studio project and no game code exist yet.

The confidence figures are interview judgments from the sources in `SOURCE-LOG.md`. They are not measurements.

```
-------- GATE STATUS --------
Gate         | Status | Conf | Notes
-------------|--------|------|------
G1 SCOPE     | OPEN   | 75%  | Target game is Imperial 2030 on BGA. The 2026-10-15 license check did not list it, so a live release still needs a license that is not on the list.
G2 USERS     | OPEN   | 85%  | Website login as CiscoKidRyan0 succeeded. Publisher and designer join at BGA's review steps.
G3 INPUTS    | OPEN   | 55%  | Geekitems, 28 files, and 35 videos are listed. The rules PDF was not retrieved.
G4 OUTPUTS   | OPEN   | 60%  | This repo and the notes exist. The playable adaptation does not.
G5 CONSTRAINTS | OPEN | 80%  | Licensing and project lists were opened. Imperial 2030 is on neither. The website password is in Credential Manager, not in the email.
G6 EDGE CASES | OPEN  | 25%  | Rule exceptions are not known until the rulebook is read. BGA requires a zombie method per state in the current walkthrough.
G7 SUCCESS   | OPEN   | 60%  | BGA's own lifecycle defines alpha, publisher approval, beta, and gold. No playtest of this adaptation has been run.
-----------------------------
AGGREGATE: about 63% (Target: 95%)
BLOCKING QUESTIONS: 1
READY TO WRITE GAME CODE: NO
-----------------------------
```

## Game identity retrieved

From `bgg-geekitems-54138.json`, field names as returned:

- name: Imperial 2030
- yearpublished: 2009
- minplayers 2, maxplayers 6
- minplaytime 120, maxplaytime 180, minage 12
- short_description: "Use money to manipulate countries into warring with each other for your own profit."
- designer: Mac Gerdts (objectid 6045)
- artist: Alexander Jung (objectid 12123)
- publisher with primarylink 1: PD-Verlag (objectid 8401)
- other publishers in that array: Cranio Creations, Egmont Polska, The Game Master BV, Hobby World, Pensamento Coletivo, Rio Grande Games, Wargames Club Publishing
- categories: Economic, Nautical, Political
- mechanics: Area Majority / Influence, Area Movement, Investment, Ownership, Rondel, Stock Holding, Victory Points as a Resource
- reimplements: Imperial (objectid 24181)
- website on the item: http://RioGrandeGames.com/Game/346-Imperial-2030 titled "Imperial 2030 -- Homepage on the Rio Grande website."

The item description says Imperial 2030 was released at Essen 2009 by PD-Games and Rio Grande Games, and lists these comparisons with Imperial: new wooden bits, the Swiss Bank, a new 30 million bond, more neutral territory, fewer home provinces, and control of the Panama and Suez canals. The publisher string in that sentence is "PD-Games". The publisher link name is "PD-Verlag". Both are copied as returned.

The geekitems `wiki` field, and the wiki page fetch, state these differences and no others:

- Nations: United States, Europe, Russia, China, India and Brazil.
- Home provinces: 4 per nation, maximum 4 factories. Sea regions 11 versus 9. Neutral regions 27 versus 15. The western and eastern sea regions are adjacent.
- Canals: fleets and transported troops may use Panama and Suez. A nation that controls Colombia may deny the Panama Canal. A nation that controls North Africa may deny the Suez Canal.
- Rondel: moving more than 3 spaces costs $1M plus $1M times the nation's Power Factor.
- Bonds: a $30M bond that pays $9M interest.
- Taxation: the success bonus is a fixed amount from the Tax Chart and is taken from the nation's treasury, so a short treasury can reduce what the player receives.
- Swiss Bank: a player who controls no government receives one. A Swiss Bank can force a nation to stop on Investor when that nation tries to pass Investor, if the treasury can pay all interest.

Rank, rating, and weight were not retrieved. The XML API returned HTTP 403.

## BoardGameGeek material to use locally

Do not commit these files. The walkthrough says to put rules and reference documents in the project and exclude them from version control.

Files API: 28 files, one page. Full rows are in `grok/flock/03-bgg-imperial-2030-catalog.md`.

English-language files whose titles or descriptions name rules, setup, or scoring:

| filepage | filename | What the listing says |
| --- | --- | --- |
| 47882 | Imperial 2030 English Rules.pdf | Filename only. Posted 2009-10-08. Download returned HTTP 403 |
| 47881 | Imperial 2030 Quick Intro.pdf | Filename only. Download returned HTTP 403 |
| 197755 | Imperial 2030 - rules in brief v1.pdf | Description says it is a 1–2 page refresher, not a rulebook replacement |
| 133712 | Imperial-2030.pdf | Description says it is a page and a half for experienced players of Risk, Diplomacy, 18xx, or rondel economic games |
| 53936 | Imperial2030_PlayerAid_Version1.0.xls | Description says it summarizes setup and turn order |
| 262361 | Imperial 2030 scoring sheet.pdf | Description says the sheet includes options from the manual. That description is a player's note, not the rulebook |
| 97688 | Score Imperial 2030.xlsx | Description says to fill in Power Points, interests, and cash |
| 87818 | Imperial2030_ScoreSheet_EN.docx | Score sheet |
| 53841 | Imperial_2030_-_Integrated_Scoresheet v1.1.pdf | Score sheet |
| 51497 | imperial_2030_result_sheet.pdf | Description says it sums points |

Videos API: 35 videos, one page. Titles and hosts are in the flock catalog. Two titles that name a rules explanation:

- "Peaky Boardgamer Episode #87 - Imperial 2030 - Full rules explanation (English)" — YouTube `vEPzqVDfGvk`
- "Imperial 2030 - Einfach Losspielen (Brettspiel Regeln)" — YouTube `cZs1BTJv82o`

The videos were not watched in this session.

Images:

- `gallery=game` returned 144 images. Captions are in `grok/source-docs/bgg-image-captions.txt`.
- The flock catalog records 217 for the images request without a gallery filter. Pages 3 and 4 of that request were not saved.

Captions that name components, from the 144-image gallery file: game board (image 574713), components overview (972214), rondel (935173, 576979, 596378), setup (935582), Swiss Bank (935203), all components (1479127), upgrade kit (747778), bonds (581741), money (580048, 1027168), factories (596379), rules cover (576980), unpunched sheets (602507, 602505, 602506), Rio Grande box (717054). These captions are labels on photographs. They are not rules.

One file description, file 349597, says the Spanish rondel was uploaded with permission of Mac Gerdts. That sentence is the uploader's description.

## BGA facts that control the schedule

### Access, from the welcome email and the SFTP test

- Studio site: https://studio.boardgamearena.com/
- SFTP: `1.studio.boardgamearena.com` port 2022, user `CiscoKidRyan`. Key login worked. Home directory had no project folder.
- FileZilla Site Manager entry `BGA Studio` was read from `%APPDATA%\FileZilla\sitemanager.xml` on 2026-10-15. Stored fields: Host `1.studio.boardgamearena.com`, Port `2022`, Protocol `1`, User `CiscoKidRyan`, Logontype `5`, Keyfile `C:\Users\ryanh\Dropbox\Ryan\Key SSH API Private Public Security RSA\bga-development-rsa-key`, LocalDir this Dropbox folder. The entry comment says the remote home is `/`. The stored RemoteDir value is `1 0`. This session did not write that file. The user reported that FileZilla was connected with the key, did not ask for the Credential Manager password, and that a listing of `/` succeeded and was empty. The same file has a second entry named MacMini. Its host and user are not copied here, and that entry was not edited.
- PhpMyAdmin: https://studio.boardgamearena.com/db/ with the database user named in the email.
- Ten studio usernames: CiscoKidRyan0 through CiscoKidRyan9. The email says to log in as CiscoKidRyan0. It does not contain their website password. It links to the lost-password page.
- The website password is in Windows Credential Manager, target `BGA Developer`, stored user `ciscokidryan0`. A login with that secret on 2026-10-15 returned `success` true and `username` CiscoKidRyan0. The secret is not in this repository.
- A password-set email arrived the same day. Its link was not opened.
- First steps says an SSH key can be uploaded in the control panel to avoid sending the password. The key that authenticated is the one documented in the keys folder. Fingerprint `SHA256:OuGrjcHp67UzVMIF7h/fRgLOu6TOHoDPt+OxiE7eCzM`. The user said that public key is uploaded.
- Tools and tips, retrieved raw, says: "IMPORTANT NOTE: The ssh port is 2022" and "If you uploaded ssh key - PASSWORD method is automatically disabled, you can no longer use password". Password SFTP was not tested after the key was uploaded. SFTP continues to use the key.

### Start path

The Studio page "Great, I'm in!" says to read the five presentations, then First steps, then a tutorial. It recommends Tutorial reversi, "closest to the actual BGA implementation and maintained by the BGA team", and also links Tutorial hearts. After the tutorials it links the complete walkthrough.

First steps says the first project should be a tutorial, created from Control Panel / Manage games or https://studio.boardgamearena.com/studio#new-tutorial, with a name like "tutorialbob". It says it is too early to create a real game, and points to the walkthrough section "Select a First Game" if the developer does not want to wait.

The walkthrough introduction says not to create a new game until at least one tutorial is complete.

Those three pages are why an earlier draft asked whether the next Studio project should be Reversi. On 2026-10-15 the user rejected that question as the next step. This plan does not create a Reversi project. The sentences above stay here as the retrieved BGA text. They are not an instruction to open a tutorial project.

The 8-steps PDF, page 4, says the second rule is to choose a simple game for a first adaptation, and that complex games are kept for experienced developers. The PDF does not classify Imperial 2030.

### License, before a real project

`BGA_Game_licenses` says:

- A copyright owner must authorize an adaptation of a commercial game.
- Games that are not public domain are on BGA because that authorization was granted.
- The available-license list is https://studio.boardgamearena.com/licensing and is restricted to registered developers.
- Developers may start any Studio project. Submission to go live is rejected at review if BGA does not hold the license. Public-domain games are the stated exception.
- Before creating a project, check https://studio.boardgamearena.com/projects so two people do not start the same game.
- For a game the page calls popular, "lets say top 1000 on bgg", check the forum or Discord before going further, because BGA may already have asked and been refused, or the game may already be in development.
- A first BGA game should be one already on the license list. The page says this because some developers request a license and do not finish.
- To release, the publisher must approve during alpha. Without publisher support the game stays private.
- The first action for a licensed game is to request the image files. The walkthrough says the button is "Request Art Files" on the license page.

The walkthrough "Select a First Game" says: "Don't start a project until you are sure BGA have the licence for this game, or it will never be published!"

Imperial 2030's BGG rank was not retrieved, so the "top 1000" branch is not decided from the data in this session. The license list and the project list were opened on 2026-10-15. The result is in step 2.

### Lifecycle, from `BGA_game_Lifecycle`

| Step | How the page says you reach it | What the page says happens |
| --- | --- | --- |
| Initial | Join the developer team | Join a team or create a project |
| Assigned | Choose a game | Development can start |
| Pre-alpha | Some code exists | Framework help and advice |
| Alpha | Pre-release checklist, then say development is finished | BGA review against the guidelines. Publisher review with the publisher, the designer, BGA, and the developer. Alpha testers can play and give approvals. Invited non-alpha testers can play but cannot give approvals |
| Public beta | Publisher approval, plus enough reviewer approvals. 10+ approvals is recommended. A well-received game, preferably rating at least 4.5, with no pending bugs, may pass by administrative discretion | All players can play. Bugs are fixed under Post-release phase |
| Gold | Stable on BGA. The publisher emails publishers@boardgamearena.com to request the official release | A launch date is chosen and the game is announced |

The 8-steps PDF uses different names for the last steps: BGA team review, publisher review and the publisher's "GO", a silent launch of 2–5 days, then beta until there are no major bugs. Both documents were retrieved. The lifecycle table is the wiki. The PDF is the presentation linked from the Studio page.

The walkthrough adds, after the implementation sections: Private alpha (request button; admins check that the game starts and has something to show), Public alpha (request button after the pre-release checklist), and Beta (request button after reviewer approvals and publisher approval).

### Platform the current wiki says to use

From the Studio raw page, "Software Versions":

- PHP 8.4
- MySQL 5.7 in production, MySQL 8.0 on Studio
- Dojo Toolkit 1.15 is marked "deprecated, avoid at all cost"
- Font Awesome 4.7 and 6.4.0 are both listed

The file-reference page names the current files and marks others deprecated:

| Path | Role on that page |
| --- | --- |
| img/ | Game art. A graphics change needs Ctrl+F5. Marketing graphics and deletes need the control panel |
| gameinfos.jsonc | Name, publisher, player count, and other meta information |
| dbmodel.sql | Tables for data that changes during a game. A change restarts the game. A production change needs a migration |
| gameoptions.json, gamepreferences.json | Options and preferences. A change needs the control panel reload |
| gamename.css | Styles. A change needs Ctrl+F5 |
| modules/php/Game.php | Rules, persistence, notifications. A change does not require reload |
| modules/js/Game.js | Client actions and notification display. A change needs F5 |
| modules/php/States | State classes |
| stats.json | End-of-game statistics. A change needs the control panel reload |
| modules/ | Extra PHP and JS. Checked into version control |
| misc/ | Files kept with the project and not needed in production. Checked in. Limit 1 Mb |
| view.php and tpl | Deprecated. The page says the template should be generated from JS |
| material.inc.php | Deprecated |
| states.inc.php | Deprecated if state classes are used |

The presentations still teach `states.inc.php`, an HTML view, and Dojo. Those statements are in the PDFs that were read. New work follows the wiki's deprecation notes.

The framework PDF, pages 1–22, describes this split: MySQL holds the current game, PHP enforces the rules, and the browser receives images, CSS, HTML, and JavaScript. `setupNewGame` initializes the database. `getAllDatas` returns what that player is allowed to see. The client `setup` applies that data. A click calls a server action. Pages after 22 of that PDF were not extracted.

The state-machine PDF, pages 1–23, says to specify a finite-state machine. State types are activeplayer, multipleactiveplayer, game, and manager. gameSetup is id 1 and gameEnd is id 99, and the PDF says not to edit those two. A game-type state is unstable and must move itself to another state. `possibleactions` plus `checkAction` is the cheat check. `args` sends state-specific data to the client. `updateGameProgression` calls `getGameProgression`. The PDF's closing advice is to design the machine on paper from the rules before coding.

Guidelines PDF, pages 1–3, states three rules: a player who knows the physical game should be able to play the adaptation without learning it again; fidelity to the original is an absolute requirement; the interface should stay close to the physical game rather than become a video game. Pages 4–8 add: do not hide elements in menus, the layout is fluid down to a 1024px width, group off-board elements in `whiteblock` divs, and put resources, summaries, the first-player marker, and the standard score counter in the player panel. Pages after 8 were not extracted.

### Version control, from BGA and from this project

First steps says Studio commit is done from Control Panel / Manage Games / the game / Commit my modifications now, and that commit does not work until an admin commits the first time. It recommends another repository, and points at the Tools page.

The walkthrough "Hook version control system" says to commit at the start of a real game, that a GitHub project is allowed, and that publisher graphics and a file containing the SFTP password must not be committed. It cites a hacking attempt on Studio in June 2020 that used passwords found on GitHub.

This project's sequence is in `README.md`: counsel review, commit, push, pull request with the template, merge. The local history is the Dropbox folder. The remote is https://github.com/CiscoKidRy/BGA-Imperial-2030.

The code comment required by the `LICENCE_BGA` file retrieved from PhilipDavis/BGA-Fled is: "This code has been produced on the BGA studio platform for use on http://boardgamearena.com". That file also says BGA may run and modify the software, other Studio developers may reuse it, and rights in the idea and graphics stay with the licensor and the authors.

### Examples opened, not cloned

These public repositories returned file lists or READMEs in search. They are examples of shape, not sources for Imperial 2030 rules.

| Repository | What the opened page showed |
| --- | --- |
| https://github.com/elaskavaia/bga-sharedcode | Shared library. EPL-1.0. Classic file set including states.inc.php, material.inc.php, dbmodel.sql |
| https://github.com/danielholmes/bga-workbench | Tools: `bgawb init`, `bgawb build --deploy`, `bgawb validate` |
| https://github.com/koenheltzel/bga-sevenwondersduel | Game. Uses `Bga\GameFramework\Table` and `Deck` |
| https://github.com/ishermandom/bga-42 | Game. BSD-3-Clause. Classic file set plus tests |
| https://github.com/PhilipDavis/BGA-Fled | Game. Contains `LICENCE_BGA` |
| https://github.com/bga-his/bga-hereistand | Game. README describes modules for states, actions, and managers |
| https://github.com/danielholmes/battle-for-hill-218 | Game. README says it deploys to Studio with the workbench and that live release is manual in the Studio interface |
| https://github.com/thoun/glow | Game. Uses `Bga\GameFramework\Table` and modules under `modules/php` |

The walkthrough links the sharedcode `dbmodel.sql` and `modules/tokens.php` as an example of a token table with `token_key`, `token_location`, and `token_state`.

## Steps in order

Each implementation step ends with a counsel review, a commit, a push, a pull request, and a merge. No step below the license check writes game rules.

### 1. Access — done in this session

Recorded in the keys folder and in `RESUME.md`.

### 2. License and existing project — checked 2026-10-15, title absent

Signed in at https://studio.boardgamearena.com/ as CiscoKidRyan0, using the Credential Manager secret named in the access section. The calls were `POST /licensing/licensing/getLicensingPageData.html`, `POST /projects/projects/getProjectsPageData.html`, and `POST /studio/studio/getManagedGamesPageData.html`. Each returned `status` 1.

Recorded from those responses:

- The licensing `games` array had 2265 entries. The count fields were `licenses-available` 1175, `licenses-published` 925, and `licenses-refused` 140. The response does not say that those three counts partition the array.
- No licensing entry had `game-name` Imperial 2030 or `game-bgg-id` 54138. No entry had `game-bgg-id` 24181, the geekitems id of the earlier game Imperial.
- The same array does contain Concordia, `game-bgg-id` 124361, designer Mac Gerdts, publisher PD-Verlag, `license-refused` 0, `published` 0. That row is a different game. It shows the designer and publisher strings are present for other titles.
- Names containing "imperial" were Imperial Settlers (`game-bgg-id` 154203) and Imperial Steam (`game-bgg-id` 338760) on the licensing list, and projects `imperialsettlers`, `imperialsteam`, and `imperialminers` on the project list. None of those is Imperial 2030.
- The projects `games` array had 2662 entries. None had `name` or `licensing-game-name` Imperial 2030, and none had the name `imperial2030`.
- Managed games for this account was an empty array. `userConfirmedBeingDev` was false.
- The licensing response's `developer-username` was CiscoKidRyan.
- The licensing `games` array has no Imperial 2030 entry. Request Art Files was not checked as its own control. Unavailability is only an inference from that missing entry.

If a project is already active, the license page says to propose joining it instead of starting another. No Imperial 2030 project was in the list.

The title is absent, so do not create it yet. These retrieved instructions are in force together:

- The license page allows a Studio project and says live submission is rejected without a license.
- The walkthrough says not to start until the license is certain, or the game will never be published.
- The pre-release checklist says: "BGA must have a license for the game for a project to be moved to production, even to alpha."
- The welcome forum post at https://forum.boardgamearena.com/viewtopic.php?f=12&t=15232&lang=en says: "Except for smaller learning projects, please check with us about the license by sending an email at studio@boardgamearena.com." It also says "Start small!" and gives Through the Ages as the example of a game not to start with. It says to set `bgg_id` from the BoardGameGeek URL. The current file reference names `gameinfos.jsonc`. The 2020 post names `gameinfos.inc.php`. Use the field the generated project actually contains. For this game the id in the URL and in geekitems `objectid` is 54138.

On 15 October 2026 the user asked to send that email. It was sent from ryanhocking@gmail.com to studio@boardgamearena.com at 10:24:37 -0500. Gmail message id `1a1402a52478094f`. The subject is "License check for Imperial 2030 (BoardGameGeek 54138)". The sent text is `grok/sent/2026-10-15-studio-license.txt`. A read-back of that message showed label SENT and the same body. No reply has been retrieved. Do not create the Imperial project until that reply says to create it, or the title appears on the licensing list.

### 3. Read the rulebook — blocked on the download

Get `Imperial 2030 English Rules.pdf` from file page https://boardgamegeek.com/filepage/47882/imperial-2030-english-rulespdf or from a copy the user already owns. Save it under `reference/`. Do not commit it.

Only after that file is read: write a rules outline that quotes the rulebook, then a paper state list. The state-machine PDF says to do that before code. The walkthrough "Reduce the Rules" says to ship a smaller first version: no expansion, basic rules if the book has advanced rules, one player count if the book has special counts. Which pieces can be deferred is unknown until the book is read.

Use the English quick intro, the rules-in-brief PDF, and the setup player aid as checks against the rulebook. Do not prefer them to the rulebook. The scoring-sheet description mentions house options. Those are not rules unless the rulebook says them.

Watch the two rules videos only as a check, and write down where they differ from the book.

### 4. Tutorial — not the next step

Do not create a Reversi project or another tutorial project. The user answered the earlier question on 2026-10-15 by asking why Reversi was proposed. The reason is the Studio text quoted under "Start path". That text stays in the plan. It does not authorize a tutorial project.

Get read-only copies of published projects from https://studio.boardgamearena.com/projects with "Get readonly access" when a concrete pattern is needed. First steps says the folder then appears in the SFTP home and is read-only.

### 5. Create the Imperial project — only if step 2 allows it

Create it from Control Panel / Manage games. Do not upload a handmade skeleton first. The First steps page says the project folder appears in the SFTP home after creation.

Download that folder into this Dropbox directory. Set automated sync. First steps says manual copying is a non-starter.

Set the project status text to the combination the walkthrough lists that matches the facts at the time: "development started", "waiting for the license", "waiting for graphics".

Put the developer name in the copyright header, as the walkthrough shows. Use Ryan Hocking and ryanhocking@gmail.com unless the user names a different credit. The `LICENCE_BGA` text says a published game is credited with the BGA username and the real name unless anonymity is requested. Anonymity was not requested.

Fill `gameinfos.jsonc` from the geekitems fields above. The walkthrough says to do that from the BoardGameGeek page, and to add the box image through the Game Metadata Manager. A box image from BoardGameGeek is publisher art. Keep it out of GitHub. If the license page provides Request Art Files, use that button and wait. The walkthrough's scavenger hunt is the path it gives when original graphics are not provided.

### 6. Implement, in the walkthrough's order

The headings retrieved from the walkthrough, after the graphics and documentation steps:

1. Initial layout and pieces, generated from the client. CSS stand-ins until art arrives.
2. Database. The walkthrough's euro example is one token table: key, location, state. Add a table only when the rules need data that table cannot hold.
3. `setupNewGame` / `setupNewGameTables` from the rulebook's setup section.
4. One-time model synchronization to the client (`getAllDatas` in the framework PDF).
5. State machine on paper, then state classes. The PDF's types and the ids 1 and 99 still apply where the current template uses them. Confirm against the generated project rather than pasting the PDF's `states.inc.php` if the template has deprecated that file.
6. Turn order.
7. User actions with `checkAction`.
8. Notifications and animation. The guidelines that were read say not to hide material and not to add video-game behavior. The walkthrough says to postpone animation until the basic game works.
9. Wrap-up from the walkthrough: `getGameProgression`, a `zombie()` method on each state class, `stats.json`, logs, tiebreak and its metadata text, translation markers, tooltips on imaged components.

Express start is the test button. First steps says not to use the ordinary Start game button in Studio except for solo, where Express start has issues. Imperial 2030's minimum in the geekitems response is 2 players, so solo is not indicated by that field.

### 7. Release gates — only after the game matches the rulebook

1. Private alpha request, when there is something to show.
2. Pre-release checklist at https://en.doc.boardgamearena.com/index.php?title=Pre-release_checklist&action=raw. Retrieved limits include: each image at most 4Mb, total images at most 15Mb unless an exception is noted, box art with transparent space rather than white, extra fonts freeware with a license note in `fonts/`, sounds in `sounds/`. The same page says the first alpha deploy is done by admins after "Request ALPHA status", and that you cannot deploy from the manage-game page until that happens. Read the rest of that page at the time of the request. The copy saved by the docs pass is in `grok/flock/02-bga-studio-docs.md`.
3. Public alpha request.
4. Publisher review. The lifecycle page says the adaptation should be approved by the publisher.
5. Beta request after that approval and the reviewer approvals the lifecycle page describes.
6. Gold when the publisher emails publishers@boardgamearena.com.

## Decisions recorded 2026-10-15

1. Imperial 2030 is not on the licensing `games` array and has no project on the projects array. The check is step 2.
2. Reversi is not the next project. The question existed because First steps and the walkthrough say to finish a tutorial first. The user rejected that as this project's next step.
3. This GitHub repository is public. Revisions use GitHub only.

## Still open

1. The reply from studio@boardgamearena.com to the 15 October 2026 license email. The sent copy is `grok/sent/2026-10-15-studio-license.txt`. No reply has been retrieved. The Imperial project stays uncreated until that reply says to create it, or the title appears on the licensing list.

## Assumptions not made

- No claim that BGA holds a license that is missing from the retrieved list. The licensing `games` array returned on 2026-10-15 does not contain Imperial 2030.
- No claim that the BGG rank is inside or outside the top 1000.
- No claim that the short description or the differences list is the full rules.
- No claim that the password-set email was requested by the user. It was not used.
- No GitLab project. The user said to use GitHub only. The repository is public.
- No game code, and no project folder created by hand on the SFTP server.
