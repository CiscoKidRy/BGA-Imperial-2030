# Public GitHub examples of Board Game Arena games

Checked on 2026-10-15. Every repository below was kept only after its GitHub HTML page returned HTTP 200 and the page title contained the repository name. Root file names and README text come from the GitHub API for that same repository. No repository was cloned, and no game source file is copied here.

## How they were found

These GitHub search pages were opened in HTTP:

- https://github.com/search?q=boardgamearena+states.inc.php&type=code — HTTP 200, title `Code search results · GitHub`
- https://github.com/search?q=%22produced+on+the+BGA+studio+platform%22&type=repositories — HTTP 200, title `Repository search results · GitHub`
- https://github.com/search?q=%22BGA+framework%22+game.php&type=code — HTTP 200, title `Code search results · GitHub`

Those HTML responses are GitHub's search shell. The repository names came from the GitHub search API for the same subjects, then each repository page was opened. A separate web-search connector was not available in this session.

API counts from that search, first page only unless noted:

| Query | API `total_count` | What was used |
| --- | --- | --- |
| `boardgamearena filename:states.inc.php` (code) | 251 | First 100 file hits, 96 repositories on that page |
| `"produced on the BGA studio platform"` (code) | 3296 | First 100 file hits, 46 repositories on that page. The phrase is the usual studio header, so one game produces many hits. |
| `boardgamearena` in name, description, or readme (repositories) | 427 | First 100 repositories |
| `topic:boardgamearena` (repositories) | 112 | First 50 repositories |
| `"produced on the BGA studio platform"` (repository search) | 0 | The phrase is in source files, not in repository name or description |

The eight candidates supplied in the task were opened even when they were not on the first search page. Fifty further repositories from those search hits were opened. All 58 pages loaded. No name was added that failed to open.

## Counts

- Candidate repositories opened and kept: 8
- Additional repositories opened and kept: 50
- Additional repositories that are games: 50
- Tools: 1 (`danielholmes/bga-workbench`)
- Shared libraries: 1 (`elaskavaia/bga-sharedcode`)
- Verified repositories in this file: 58

`states.inc.php` at the repository root is listed only when that filename was in the root listing. Several games keep the BGA tree in a subdirectory or generate `*.view.php` from TypeScript, so a short file list does not mean the game is absent.

## BGA license file on PhilipDavis/BGA-Fled

The blob page https://github.com/PhilipDavis/BGA-Fled/blob/main/LICENCE_BGA returned HTTP 200. The title was `BGA-Fled/LICENCE_BGA at main · PhilipDavis/BGA-Fled · GitHub`. The visible HTML meta description is only GitHub's default "Contribute to PhilipDavis/BGA-Fled" line. The license body is in the page payload as `rawLines`, which is the text GitHub renders for the file. The raw URL https://raw.githubusercontent.com/PhilipDavis/BGA-Fled/main/LICENCE_BGA returned HTTP 200 with the same text.

> Board Game Arena (BGA) License
>
> Developers producing software and associated documentation files
> (the "Software") to create a game adaptation on the BGA studio platform agree
> that the Software:
>  - can be used on Board Game Arena (BGA) to run the game, with no limitations
>  whatsoever;
>  - can be modified by BGA site administrators to fit the purpose of the site, to
>  fix bugs or in the purpose of re-factoring;
>  - can be freely reused and adapted by developers for other games on the BGA
> studio platform.
>
> BGA will give credit to the developer of a published game through the game
> description page, by referencing his BGA user name and his real name, unless the
>  developer explicitly requests anonymity.
>
> Developers can also publish the code they contributed under any licence they
> have an interest in, as long as they include the following mention as a code
> comment:
>    “This code has been produced on the BGA studio platform for use on
>     http://boardgamearena.com”.
>
> All rights on the idea and graphics of a game stay with the licensor and
> author(s) respectively.

Many other repositories in this list also have a root file named `LICENCE_BGA`. Only this file was opened and quoted.

## Candidate repositories


### elaskavaia/bga-sharedcode

- **URL:** https://github.com/elaskavaia/bga-sharedcode
- **Page check:** HTTP 200. Title: GitHub - elaskavaia/bga-sharedcode: Mirror of bga sharedcode project - to share code and resource for bga developers · GitHub
- **Description:** Mirror of bga sharedcode project - to share code and resource for bga developers
- **Kind:** Shared library. The README calls it a mirror of the BGA sharedcode project for developers. The root is also laid out as a BGA project named `sharedcode`.
- **License:** Eclipse Public License 1.0 (`EPL-1.0`). Root license files seen: `LICENSE`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `sharedcode.action.php`, `sharedcode.game.php`, `sharedcode.view.php`, `sharedcode_sharedcode.tpl`, `states.inc.php`, `version.php`.
- **README:**

> Mirror of bga sharedcode project - to share code and resource for bga developers

### danielholmes/bga-workbench

- **URL:** https://github.com/danielholmes/bga-workbench
- **Page check:** HTTP 200. Title: GitHub - danielholmes/bga-workbench: Set of tools to work with a BoardGameArena project · GitHub
- **Description:** Set of tools to work with a BoardGameArena project
- **Kind:** Tool. The README describes command-line tooling for Board Game Arena projects, not a playable game.
- **License:** MIT License (`MIT`). Root license files seen: `LICENSE`.
- **BGA files at repository root:** None at the repository root. Other root names seen: `Dockerfile`, `LICENSE`, `README.md`, `Vagrantfile`, `bin`, `composer.json`, `composer.lock`, `etc`, `phpunit.xml`, `resources`, `src`, `tests`.
- **README:**

> Deploying to BGA Studio
> 
> ```bash
> bgawb build --deploy
> ```
> 
> Continuous Deployment to Studio. Watches development files and deploys them as they change.
> 
> ```bash
> bgawb build --deploy --watch
> ```

### koenheltzel/bga-sevenwondersduel

- **URL:** https://github.com/koenheltzel/bga-sevenwondersduel
- **Page check:** HTTP 200. Title: GitHub - koenheltzel/bga-sevenwondersduel: 7 Wonders Duel board game (+ expansions) implemented for BoardGameArena · GitHub
- **Description:** 7 Wonders Duel board game (+ expansions) implemented for BoardGameArena
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `sevenwondersduel.action.php`, `sevenwondersduel.game.php`, `sevenwondersduel.view.php`, `sevenwondersduel_sevenwondersduel.tpl`, `states.inc.php`, `version.php`.
- **README:**

> 7 Wonders Duel (+ Agora & Pantheon) implementation for BoardGameArena. https://boardgamearena.com/gamepanel?game=sevenwondersduel
> 
> This project was done in assignment of BoardGameArena and using licensed material from Repos Production with their agreement & cooperation.
> 
> I'm releasing the source code so this game can stay maintained as I no longer have time for BoardGameArena development.

### ishermandom/bga-42

- **URL:** https://github.com/ishermandom/bga-42
- **Page check:** HTTP 200. Title: GitHub - ishermandom/bga-42: Texas 42 domino game implementation for BoardGameArena · GitHub
- **Description:** Texas 42 domino game implementation for BoardGameArena
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** BSD 3-Clause "New" or "Revised" License (`BSD-3-Clause`). Root license files seen: `LICENCE_BGA`, `LICENSE`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `texasfortytwo.action.php`, `texasfortytwo.game.php`, `texasfortytwo.view.php`, `texasfortytwo_texasfortytwo.tpl`, `version.php`.
- **README:**

> A BoardGameArena implementation for Texas 42.
> 
> The README does not describe deployment. Its only setup section is editor formatting: "When writing code, please autoformat using the atom-beautify package." It then points PHP-CS-Fixer at `.php-cs-fixer.php` in the base directory.

### PhilipDavis/BGA-Fled

- **URL:** https://github.com/PhilipDavis/BGA-Fled
- **Page check:** HTTP 200. Title: GitHub - PhilipDavis/BGA-Fled: Fled game on Board Game Arena · GitHub
- **Description:** Fled game on Board Game Arena
- **Kind:** Game, from the description on the repository page. There is no README text to classify it further.
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `fled.action.php`, `fled.game.php`, `fled.view.php`, `fled_fled.tpl`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `version.php`.
- **README:**

No README text was on the default branch, so there is no paragraph to quote about deployment or structure.

### bga-his/bga-hereistand

- **URL:** https://github.com/bga-his/bga-hereistand
- **Page check:** HTTP 200. Title: GitHub - bga-his/bga-hereistand: Here I Stand for Board Game Arena · GitHub
- **Description:** Here I Stand for Board Game Arena
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** No license is shown on the repository page.
- **BGA files at repository root:** None at the repository root. Other root names seen: `Makefile`, `README.md`, `hereistand`, `vassal_coords.xml`, `xsync.sh`.
- **README:**

> This is a rather complex game and so the initial design tried to make room for all of it with an complex design.
> 
> ```
> hereistand
>   \img
>     \svg - All tokens are currently just SVGs,
>   \misc
>     \tests - A goal was to decouple all logic from the database to allow for test driven development on a local machine, tests are here
>   \modules - The PHP and JS module system are heavily used, code is here
>     \css - SASS is compiled into the main CSS file as part of the build process
>     \js - Methods for showing Gamestate to client and setting clickables
>     \php
>       \Core - A few base classes for the game
>         \Actions change DB as State
>         \Game
>         \Globals
>         \Notifications
>         \Preferences
>         \Stats
>       \Helpers - Utility classes, used elsewhere
>       \Managers - Database managers for various objects
>       \Models - Classes representing other game concepts
> ```
> 
> The quote stops before a later line that was cut off in the fetched README excerpt. The usual `states.inc.php` name was not at the repository root; the root directory `hereistand` is where this tree starts. Code search had already shown `hereistand/states.inc.php` inside that directory.

### danielholmes/battle-for-hill-218

- **URL:** https://github.com/danielholmes/battle-for-hill-218
- **Page check:** HTTP 200. Title: GitHub - danielholmes/battle-for-hill-218: Battle for Hill 218 game implemented for BoardGameArena · GitHub
- **Description:** Battle for Hill 218 game implemented for BoardGameArena
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** MIT License (`MIT`). Root license files seen: `LICENSE`.
- **BGA files at repository root:** `battleforhill.action.php`, `battleforhill.game.php`, `battleforhill.view.php`, `battleforhill_battleforhill.tpl`, `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `version.php`.
- **README:**

> This deploys to BGA studio only and allows you to test on there. Deployment to live BGA is then done manually through the studio interface.
> 
> ```
> vagrant ssh
> composer deploy
> ```
> 
> Continuous deployment is `bgawb build --deploy --watch` inside the same Vagrant machine. The README says the project uses BoardGameArena Workbench, and the root contains `bgaproject.yml.dist`.

### thoun/glow

- **URL:** https://github.com/thoun/glow
- **Page check:** HTTP 200. Title: GitHub - thoun/glow · GitHub
- **Description:** No description is set on the repository page.
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `glow.action.php`, `glow.game.php`, `material.inc.php`, `states.inc.php`.
- **README:**

> This project is an adaptation for BoardGameArena of game Glow edited by Bombyx.
> 
> Also add one auto-FTP upload extension (for example https://marketplace.visualstudio.com/items?itemName=lukasz-wronski.ftp-sync) and configure it. The extension will detected modified files in the workspace, including builded ones, and upload them to remote server.

## Additional game repositories


These 50 were on the search result pages above and are not in the candidate list. Each GitHub page loaded. They are games, not tools or shared libraries.


### 0-wiz-0/bga-abandonallartichokes

- **URL:** https://github.com/0-wiz-0/bga-abandonallartichokes
- **Page check:** HTTP 200. Title: GitHub - 0-wiz-0/bga-abandonallartichokes: Abandon All Artichokes implementation for Board Game Arena · GitHub
- **Description:** Abandon All Artichokes implementation for Board Game Arena
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** MIT License (`MIT`). Root license files seen: `LICENCE`, `LICENCE_BGA`.
- **BGA files at repository root:** `abandonallartichokes.action.php`, `abandonallartichokes.game.php`, `abandonallartichokes.view.php`, `abandonallartichokes_abandonallartichokes.tpl`, `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `version.php`.
- **README:**

> This repository contains the source code for the Board Game Arena implementation of Gamewright's card game Abandon All Artichokes. The README does not describe deployment.

### AbelTiborToth/bga-coatl

- **URL:** https://github.com/AbelTiborToth/bga-coatl
- **Page check:** HTTP 200. Title: GitHub - AbelTiborToth/bga-coatl: Board Game Arena adaptation of the game Cóatl · GitHub
- **Description:** Board Game Arena adaptation of the game Cóatl
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `coatl.action.php`, `coatl.game.php`, `coatl.view.php`, `coatl_coatl.tpl`, `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `version.php`.
- **README:**

> This project is an adaptation for Board Game Arena of the game Cóatl published by Synapses Games. The README does not describe deployment.

### alberto-bottarini/bga-florenza

- **URL:** https://github.com/alberto-bottarini/bga-florenza
- **Page check:** HTTP 200. Title: GitHub - alberto-bottarini/bga-florenza: BoardGameArena - Florenza: The Card Game · GitHub
- **Description:** BoardGameArena - Florenza: The Card Game
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** MIT License (`MIT`). Root license files seen: `LICENSE`.
- **BGA files at repository root:** `dbmodel.sql`, `florenzacardgame.action.php`, `florenzacardgame.game.php`, `florenzacardgame.view.php`, `florenzacardgame_florenzacardgame.tpl`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `version.php`.
- **README:**

> Implementation of Florenza: The Card Game by Placentia Games for BoardGameArena platform. The README does not describe deployment or structure.

### AndyKerrison/bga-eruption

- **URL:** https://github.com/AndyKerrison/bga-eruption
- **Page check:** HTTP 200. Title: GitHub - AndyKerrison/bga-eruption: BoardGameArena implementation of Eruption · GitHub
- **Description:** BoardGameArena implementation of Eruption
- **Kind:** Game, from the description on the repository page. There is no README text to classify it further.
- **License:** No license is shown on the repository page.
- **BGA files at repository root:** `akeruption.action.php`, `akeruption.game.php`, `akeruption.view.php`, `akeruption_akeruption.tpl`, `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `version.php`.
- **README:**

No README text was on the default branch, so there is no paragraph to quote about deployment or structure.

### AndyKerrison/bga-tichu

- **URL:** https://github.com/AndyKerrison/bga-tichu
- **Page check:** HTTP 200. Title: GitHub - AndyKerrison/bga-tichu: For BoardGameArena implementation of Tichu · GitHub
- **Description:** For BoardGameArena implementation of Tichu
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** No license is shown on the repository page.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `tichu.action.php`, `tichu.game.php`, `tichu.view.php`, `tichu_tichu.tpl`, `version.php`.
- **README:**

> For BoardGameArena implementation of Tichu. That heading is the whole README. It does not describe deployment or structure.

### AntonioSoler/bga-incangold

- **URL:** https://github.com/AntonioSoler/bga-incangold
- **Page check:** HTTP 200. Title: GitHub - AntonioSoler/bga-incangold: Incan Gold implementation in php + css + js + sql for BGA · GitHub
- **Description:** Incan Gold implementation in php + css + js + sql for BGA
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** MIT License (`MIT`). Root license files seen: `LICENSE`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `incangold.action.php`, `incangold.game.php`, `incangold.view.php`, `incangold_incangold.tpl`, `material.inc.php`, `states.inc.php`, `version.php`.
- **README:**

> Incan Gold implementation in php + css + js + sql for BGA. The README credits Eagle-Gryphon Games for licensed material and names people who helped with tips, debugging, and playtest. It does not describe deployment.

### AntonioSoler/bga-santorini

- **URL:** https://github.com/AntonioSoler/bga-santorini
- **Page check:** HTTP 200. Title: GitHub - AntonioSoler/bga-santorini: 🎲 Santorini implementation for Board Game Arena · GitHub
- **Description:** 🎲 Santorini implementation for Board Game Arena
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `santorini.action.php`, `santorini.game.php`, `santorini.view.php`, `santorini_santorini.tpl`, `states.inc.php`.
- **README:**

> Santorini implementation for Board Game Arena. Languages: PHP JS SQL CSS. The README does not describe how the project is uploaded. It says the work uses licensed material from Roxley Games and SpinMaster with their agreement.

### bennygui/barenpark-public

- **URL:** https://github.com/bennygui/barenpark-public
- **Page check:** HTTP 200. Title: GitHub - bennygui/barenpark-public: Bärenpark for BGA · GitHub
- **Description:** Bärenpark for BGA
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `barenpark.action.php`, `barenpark.game.php`, `barenpark.view.php`, `barenpark_barenpark.tpl`, `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `version.php`.
- **README:**

> This is the implementation of Bärenpark for BGA: https://boardgamearena.com/gamepanel?game=barenpark. The README does not describe deployment.

### bennygui/earth-public

- **URL:** https://github.com/bennygui/earth-public
- **Page check:** HTTP 200. Title: GitHub - bennygui/earth-public: Earth for BGA · GitHub
- **Description:** Earth for BGA
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `earth.action.php`, `earth.game.php`, `earth.view.php`, `earth_earth.tpl`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `version.php`.
- **README:**

> This is the implementation of Earth for BGA, with the Abundance expansion: https://boardgamearena.com/gamepanel?game=earth. The README does not describe deployment.

### bennygui/theisleofcats-public

- **URL:** https://github.com/bennygui/theisleofcats-public
- **Page check:** HTTP 200. Title: GitHub - bennygui/theisleofcats-public: The Isle of Cats for BGA · GitHub
- **Description:** The Isle of Cats for BGA
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `theisleofcats.action.php`, `theisleofcats.game.php`, `theisleofcats.view.php`, `theisleofcats_theisleofcats.tpl`, `version.php`.
- **README:**

> This is the implementation of The Isle of Cats for BGA: https://boardgamearena.com/gamepanel?game=theisleofcats. The README does not describe deployment.

### bga-devs/bga-heat

- **URL:** https://github.com/bga-devs/bga-heat
- **Page check:** HTTP 200. Title: GitHub - bga-devs/bga-heat · GitHub
- **Description:** No description is set on the repository page.
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `states.inc.php`.
- **README:**

> This project is an adaptation for BoardGameArena of game Heat edited by Days of Wonder.
> 
> Also add one auto-FTP upload extension (for example https://marketplace.visualstudio.com/items?itemName=lukasz-wronski.ftp-sync) and configure it. The extension will detected modified files in the workspace, including builded ones, and upload them to remote server.

### bga-devs/bga-memoir

- **URL:** https://github.com/bga-devs/bga-memoir
- **Page check:** HTTP 200. Title: GitHub - bga-devs/bga-memoir · GitHub
- **Description:** No description is set on the repository page.
- **Kind:** Game. There is no README and no About text. The root contains BGA game entry-point filenames, which is the basis for this label.
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `memoir.action.php`, `memoir.game.php`, `memoir.view.php`, `memoir_memoir.tpl`, `states.inc.php`, `version.php`.
- **README:**

No README text was on the default branch, so there is no paragraph to quote about deployment or structure.

### drasill/bga-coinche

- **URL:** https://github.com/drasill/bga-coinche
- **Page check:** HTTP 200. Title: GitHub - drasill/bga-coinche: Coinche (belote card game) implementation for BoardGameArena · GitHub
- **Description:** Coinche (belote card game) implementation for BoardGameArena
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** MIT License (`MIT`). Root license files seen: `LICENCE_BGA`, `LICENSE`.
- **BGA files at repository root:** `coinche.action.php`, `coinche.game.php`, `coinche.view.php`, `coinche_coinche.tpl`, `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `version.php`.
- **README:**

> Coinche game implementation on BGA (Board Game Arena). The fetched README has that one-line description and does not explain deployment.

### drasill/bga-solar-storm

- **URL:** https://github.com/drasill/bga-solar-storm
- **Page check:** HTTP 200. Title: GitHub - drasill/bga-solar-storm: Solar Storm (boardgame) implementation for BoardGameArena · GitHub
- **Description:** Solar Storm (boardgame) implementation for BoardGameArena
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `solarstorm.action.php`, `solarstorm.game.php`, `solarstorm.view.php`, `solarstorm_solarstorm.tpl`, `states.inc.php`, `version.php`.
- **README:**

> `Readme.md` is present and empty. Git reports size 0 and the empty-blob sha `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`. There is no deployment paragraph. A separate `Build.md` is in the root; it was not opened for this note.

### elaskavaia/bga-mars

- **URL:** https://github.com/elaskavaia/bga-mars
- **Page check:** HTTP 200. Title: GitHub - elaskavaia/bga-mars · GitHub
- **Description:** No description is set on the repository page.
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`, `LICENSE`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `terraformingmars.action.php`, `terraformingmars.game.php`, `terraformingmars.view.php`, `terraformingmars_terraformingmars.tpl`, `version.php`.
- **README:**

> Bga project for tm game. Only usable when you develop games for https://boardgamearena.com. It uses typescript and scss.
> 
> To have auto-upload in vscode: Install SFTP and configure, see https://en.doc.boardgamearena.com/Setting_up_BGA_Development_environment_using_VSCode
> 
> Structures of project: `src` is the TypeScript and CSS source; `src/css` holds scss files; `src/*.ts` are the game scripts; `src/Zain.ts` is the only Dojo file and includes everything; `modules/*` holds PHP server-side classes and modules; `modules/tests/*` holds phpunit tests.

### Fnordistan/trickoftherails

- **URL:** https://github.com/Fnordistan/trickoftherails
- **Page check:** HTTP 200. Title: GitHub - Fnordistan/trickoftherails: For the BoardGameArena implementation of Trick of the Rails · GitHub
- **Description:** For the BoardGameArena implementation of Trick of the Rails
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `trickoftherails.action.php`, `trickoftherails.game.php`, `trickoftherails.view.php`, `trickoftherails_trickoftherails.tpl`, `version.php`.
- **README:**

> The README is only the heading `# trickoftherails`. It does not describe deployment or structure.

### FransBongers/bga-pax-pamir

- **URL:** https://github.com/FransBongers/bga-pax-pamir
- **Page check:** HTTP 200. Title: GitHub - FransBongers/bga-pax-pamir: Implementation of Pax Pamir 2nd edition for Board Game Arena · GitHub
- **Description:** Implementation of Pax Pamir 2nd edition for Board Game Arena
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** MIT License (`MIT`). Root license files seen: `LICENCE_BGA`, `LICENSE.md`.
- **BGA files at repository root:** `dbmodel.sql`, `material.inc.php`, `paxpamir.action.php`, `paxpamir.game.php`, `states.inc.php`.
- **README:**

> Pax Pamir implementation for Board Game Arena. The README says the adaptation includes licensed material from the Wehrlegig Games edition, used with permission, and that the project is tested with BrowserStack. It does not describe deployment.

### FransBongers/bga-pax-renaissance

- **URL:** https://github.com/FransBongers/bga-pax-renaissance
- **Page check:** HTTP 200. Title: GitHub - FransBongers/bga-pax-renaissance: Pax Renaissance for Board Game Arena · GitHub
- **Description:** Pax Renaissance for Board Game Arena
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `material.inc.php`, `paxrenaissance.action.php`, `paxrenaissance.game.php`, `states.inc.php`.
- **README:**

> Pax Renaissance implementation for Board Game Arena. The README says the adaptation includes licensed material used with permission and that copyrights remain with the owners. It does not describe deployment.

### hellp/bga-pi

- **URL:** https://github.com/hellp/bga-pi
- **Page check:** HTTP 200. Title: GitHub - hellp/bga-pi: Board Game Arena implementation of Martin Wallace’ deduction game “P.I.” (Treefrog Games). My first project using BGA’s framework. · GitHub
- **Description:** Board Game Arena implementation of Martin Wallace’ deduction game “P.I.” (Treefrog Games). My first project using BGA’s framework.
- **Kind:** Game, from the description on the repository page. There is no README text to classify it further.
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENSE`, `LICENSE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `pi.action.php`, `pi.game.php`, `pi.view.php`, `pi_pi.tpl`, `states.inc.php`, `version.php`.
- **README:**

No README text was on the default branch, so there is no paragraph to quote about deployment or structure.

### JoeProgram/bga-copenhagen

- **URL:** https://github.com/JoeProgram/bga-copenhagen
- **Page check:** HTTP 200. Title: GitHub - JoeProgram/bga-copenhagen: Copenhagen on Board Game Arena · GitHub
- **Description:** Copenhagen on Board Game Arena
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** MIT License (`MIT`). Root license files seen: `LICENCE_BGA`, `LICENSE`.
- **BGA files at repository root:** `copenhagen.action.php`, `copenhagen.game.php`, `copenhagen.view.php`, `copenhagen_copenhagen.tpl`, `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `version.php`.
- **README:**

> This project builds off the default Board Game Arena framework.
> 
> File structure, back end, from the README: `states.inc.php` defines a state machine of how the game works; `copenhagen.action.php` defines the URLs the client is allowed to call and does basic sanitization; `copenhagen.game.php` is the controller, processes client requests, modifies the database, and transitions states; `dbmodel.sql` holds the game state, and the README says every game instance on Board Game Arena has its own database; `material.inc.php` stores global data and magic numbers. On the front end, `copenhagen_copenhagen.tpl` is the HTML, `copenhagen.view.php` fills that template from server data, and `copenhagen.js` holds client logic and AJAX calls.

### jordijansen/bga-canvas

- **URL:** https://github.com/jordijansen/bga-canvas
- **Page check:** HTTP 200. Title: GitHub - jordijansen/bga-canvas: Status: LIVE · GitHub
- **Description:** Status: LIVE
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `canvas.action.php`, `canvas.game.php`, `canvas.view.php`, `canvas_canvas.tpl`, `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `version.php`.
- **README:**

> The README is only `# bga-canvas` and `Status: DEVELOPMENT`. The repository description on the GitHub page says `Status: LIVE`. Neither text describes deployment or structure.

### Lucas-C/tablut

- **URL:** https://github.com/Lucas-C/tablut
- **Page check:** HTTP 200. Title: GitHub - Lucas-C/tablut: Implémentation du jeu Tablut pour BoardGameArena · GitHub
- **Description:** Implémentation du jeu Tablut pour BoardGameArena Archived on GitHub.
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** MIT License (`MIT`). Root license files seen: `LICENSE`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `tablut.action.php`, `tablut.game.php`, `tablut.view.php`, `tablut_tablut.tpl`, `version.php`.
- **README:**

> Tablut board game implementation for BoardGameArena.
> 
> Deploying to Studio:
> 
> ```
> cp bgaproject.yml.dist bgaproject.yml
> # then fill in sftp properties
> composer bgaw-deploy
> ```
> 
> Continuous deployment is `composer bgaw-watch`. The repository is archived. The README also shows a four-state game state machine as an image under `docs/`.

### marcuda/bga-saintpetersburg

- **URL:** https://github.com/marcuda/bga-saintpetersburg
- **Page check:** HTTP 200. Title: GitHub - marcuda/bga-saintpetersburg: Saint Petersburg on boardgamearena.com · GitHub
- **Description:** Saint Petersburg on boardgamearena.com
- **Kind:** Game, from the description on the repository page. There is no README text to classify it further.
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`.
- **README:**

No README text was on the default branch, so there is no paragraph to quote about deployment or structure.

### MartinGoulet/bga-wizards-grimoire

- **URL:** https://github.com/MartinGoulet/bga-wizards-grimoire
- **Page check:** HTTP 200. Title: GitHub - MartinGoulet/bga-wizards-grimoire: Wizards of the Grimoire for Board Game Arena · GitHub
- **Description:** Wizards of the Grimoire for Board Game Arena
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** MIT License (`MIT`). Root license files seen: `LICENCE_BGA`, `License.md`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `states.inc.php`, `wizardsgrimoire_wizardsgrimoire.tpl`.
- **README:**

> The fetched README says "This project is tested with BrowserStack". It does not describe deployment or the file layout.

### micahstairs/bga-innovation

- **URL:** https://github.com/micahstairs/bga-innovation
- **Page check:** HTTP 200. Title: GitHub - micahstairs/bga-innovation · GitHub
- **Description:** No description is set on the repository page.
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** MIT License (`MIT`). Root license files seen: `LICENSE`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `innovation.action.php`, `innovation.game.php`, `material.inc.php`, `states.inc.php`.
- **README:**

> In order to test changes to the game, you need to be able to copy the code out of our GitHub repository and into a personal BGA project and then back again.
> 
> Create a BGA developer account on https://studio.boardgamearena.com/. Create your own BGA Studio project for Innovation at https://studio.boardgamearena.com/studio. Make sure to suffix the new project name with your username (e.g. `InnovationJohnSmith`). Clone this repository onto your computer (`git clone https://github.com/micahstairs/bga-innovation.git innovation`). You'll make your life easier if the directory is named `innovation` instead of `bga-innovation`. Clone https://github.com/elaskavaia/bga-sharedcode onto your computer.

### ModProg/Doppelkopf

- **URL:** https://github.com/ModProg/Doppelkopf
- **Page check:** HTTP 200. Title: GitHub - ModProg/Doppelkopf: Doppelkopf on BGA · GitHub
- **Description:** Doppelkopf on BGA
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `dk.action.php`, `dk.game.php`, `dk.view.php`, `dk_dk.tpl`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `version.php`.
- **README:**

> Doppelkopf on BGA. Try here: https://studio.boardgamearena.com/lobby?game=3060. That studio lobby link is the only setup note. The README does not describe file layout.

### npatron/bga-homesteaders

- **URL:** https://github.com/npatron/bga-homesteaders
- **Page check:** HTTP 200. Title: GitHub - npatron/bga-homesteaders: Create homesteaders board game for BoardGameArena · GitHub
- **Description:** Create homesteaders board game for BoardGameArena
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `homesteaders.action.php`, `homesteaders.game.php`, `homesteaders.view.php`, `homesteaders_homesteaders.tpl`, `material.inc.php`, `states.inc.php`, `version.php`.
- **README:**

> Create homesteaders board game for BoardGameArena. The project is only setup (as written) to work on BoardGameArena, but much of the logic could be adaptable for other platforms.

### Oliboy50/bga-velonimo

- **URL:** https://github.com/Oliboy50/bga-velonimo
- **Page check:** HTTP 200. Title: GitHub - Oliboy50/bga-velonimo: Velonimo boardgame adaptation for Board Game Arena · GitHub
- **Description:** Velonimo boardgame adaptation for Board Game Arena
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** GNU General Public License v3.0 (`GPL-3.0`). Root license files seen: `LICENCE_BGA`, `LICENSE.md`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `velonimo.action.php`, `velonimo.game.php`, `velonimo.view.php`, `velonimo_velonimo.tpl`, `version.php`.
- **README:**

> Board Game Arena adaptation of a card game named Velonimo.
> 
> The README's build note for art is "Create sprite of cards": make `cards.png` with ImageMagick `montage` from the 180x251 card images, tiled 7x9. It does not describe how the PHP project is uploaded to Studio.

### pottibot/bga-eriantys

- **URL:** https://github.com/pottibot/bga-eriantys
- **Page check:** HTTP 200. Title: GitHub - pottibot/bga-eriantys: Adaptation of the board game Eriantys for the BoardGameArena online platform · GitHub
- **Description:** Adaptation of the board game Eriantys for the BoardGameArena online platform
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `eriantys.action.php`, `eriantys.game.php`, `eriantys.view.php`, `eriantys_eriantys.tpl`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `version.php`.
- **README:**

> Adaptation of the board game Eriantys, designed by Leo Colovini, for the BoardGameArena online platform. This work is done using licensed material from Cranio Creations. All images and names copyrights belong to them. The README does not describe deployment.

### quietmint/bga-coupcitystate

- **URL:** https://github.com/quietmint/bga-coupcitystate
- **Page check:** HTTP 200. Title: GitHub - quietmint/bga-coupcitystate: 🎲 Coup: City State implementation for Board Game Arena · GitHub
- **Description:** 🎲 Coup: City State implementation for Board Game Arena
- **Kind:** Game, from the description on the repository page. There is no README text to classify it further.
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `coupcitystate.action.php`, `coupcitystate.game.php`, `coupcitystate.view.php`, `coupcitystate_coupcitystate.tpl`, `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`.
- **README:**

No README text was on the default branch, so there is no paragraph to quote about deployment or structure.

### quietmint/bga-hardback

- **URL:** https://github.com/quietmint/bga-hardback
- **Page check:** HTTP 200. Title: GitHub - quietmint/bga-hardback: 🎲 Hardback implementation for Board Game Arena · GitHub
- **Description:** 🎲 Hardback implementation for Board Game Arena
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `hardback.action.php`, `hardback.game.php`, `hardback.view.php`, `hardback_hardback.tpl`, `material.inc.php`, `states.inc.php`.
- **README:**

> Hardback implementation for Board Game Arena. The README lists licensed material and fonts. It does not describe deployment. A root script named `bga-sync.sh` was visible, but its contents were not copied.

### quietmint/bga-taluva

- **URL:** https://github.com/quietmint/bga-taluva
- **Page check:** HTTP 200. Title: GitHub - quietmint/bga-taluva: 🎲 Taluva implementation for Board Game Arena · GitHub
- **Description:** 🎲 Taluva implementation for Board Game Arena
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `material.inc.php`, `states.inc.php`, `taluva.action.php`, `taluva.game.php`, `taluva.view.php`, `taluva_taluva.tpl`.
- **README:**

> Taluva implementation for Board Game Arena. Languages: PHP JS SQL CSS. The README does not describe deployment. It says the work uses licensed material from Ferti Games with their agreement.

### robinzigmond/bga-oracleofdelphi

- **URL:** https://github.com/robinzigmond/bga-oracleofdelphi
- **Page check:** HTTP 200. Title: GitHub - robinzigmond/bga-oracleofdelphi: online implementation of Oracle of Delphi boardgame for Board Game Arena, using BGA framework. NOTE: image directory not on Github out of respect for publisher&#39;s copyright · GitHub
- **Description:** online implementation of Oracle of Delphi boardgame for Board Game Arena, using BGA framework. NOTE: image directory not on Github out of respect for publisher's copyright
- **Kind:** Game, from the description on the repository page. There is no README text to classify it further.
- **License:** No license is shown on the repository page.
- **BGA files at repository root:** None at the repository root. Other root names seen: `oracleofdelphi`.
- **README:**

No README text was on the default branch, so there is no paragraph to quote about deployment or structure.

### sebastien-prudhomme/bga-assyria

- **URL:** https://github.com/sebastien-prudhomme/bga-assyria
- **Page check:** HTTP 200. Title: GitHub - sebastien-prudhomme/bga-assyria: Assyria implementation for Board Game Arena website · GitHub
- **Description:** Assyria implementation for Board Game Arena website
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** MIT License (`MIT`). Root license files seen: `LICENCE_BGA`, `LICENSE`.
- **BGA files at repository root:** `assyria.action.php`, `assyria.game.php`, `assyria.view.php`, `assyria_assyria.tpl`, `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `version.php`.
- **README:**

> Assyria implementation for Board Game Arena website. That is the entire README. It does not describe deployment or internal structure.

### ShaPhi7/loveletter

- **URL:** https://github.com/ShaPhi7/loveletter
- **Page check:** HTTP 200. Title: GitHub - ShaPhi7/loveletter: Implementation of Love Letter for boardgamearena.com · GitHub
- **Description:** Implementation of Love Letter for boardgamearena.com
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `loveletter.action.php`, `loveletter.game.php`, `loveletter.view.php`, `material.inc.php`, `states.inc.php`, `version.php`.
- **README:**

> Source code for the Love Letter game on boardgamearena.com. Please note LICENCE_BGA.
> 
> Please note that none of the code in the original commit was authored by ShaPhi7. Please be aware that images are not present. The README does not describe deployment. A root directory named `bga-sharedcode` was visible.

### sumpfork/seas_of_havoc_boardgamearena

- **URL:** https://github.com/sumpfork/seas_of_havoc_boardgamearena
- **Page check:** HTTP 200. Title: GitHub - sumpfork/seas_of_havoc_boardgamearena: Boardgame Arena implementation of Seas of Havoc · GitHub
- **Description:** Boardgame Arena implementation of Seas of Havoc
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `seasofhavoc.game.php`.
- **README:**

> This is the implementation of the boardgame Seas of Havoc for Board Game Arena.
> 
> The credits section says game design is by Sébastien Bernier-Wong and Peter Gorniak, published by Rock Manor Games, and that "This credit also has to be visible to players, not only here: keep it on the game's BGA page." The README does not describe deployment.

### Syarwin/bga-bang

- **URL:** https://github.com/Syarwin/bga-bang
- **Page check:** HTTP 200. Title: GitHub - Syarwin/bga-bang · GitHub
- **Description:** No description is set on the repository page.
- **Kind:** Game. There is no README and no About text. The root contains BGA game entry-point filenames, which is the basis for this label.
- **License:** MIT License (`MIT`). Root license files seen: `LICENSE`.
- **BGA files at repository root:** `bang.action.php`, `bang.game.php`, `bang.view.php`, `bang_bang.tpl`, `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`.
- **README:**

No README text was on the default branch, so there is no paragraph to quote about deployment or structure.

### Syarwin/bga-barrage

- **URL:** https://github.com/Syarwin/bga-barrage
- **Page check:** HTTP 200. Title: GitHub - Syarwin/bga-barrage · GitHub
- **Description:** No description is set on the repository page.
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `barrage.action.php`, `barrage.game.php`, `barrage.view.php`, `barrage_barrage.tpl`, `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `version.php`.
- **README:**

> The file named `README` is a French bug-and-todo list, not a deploy guide. It opens with "bug" and "Essentiel", including "ajuster le layout sur écran plus petit" and "ajouter un slider pour ajuster la taille des action boards". It does not describe how the project is uploaded.

### Syarwin/bga-kingdombuilder

- **URL:** https://github.com/Syarwin/bga-kingdombuilder
- **Page check:** HTTP 200. Title: GitHub - Syarwin/bga-kingdombuilder · GitHub
- **Description:** No description is set on the repository page.
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `kingdombuilder.action.php`, `kingdombuilder.game.php`, `kingdombuilder.view.php`, `kingdombuilder_kingdombuilder.tpl`, `material.inc.php`, `states.inc.php`, `version.php`.
- **README:**

> The README is only the heading `# bga-kingdombuilder`. It does not describe deployment or structure.

### Syarwin/bga-welcometo

- **URL:** https://github.com/Syarwin/bga-welcometo
- **Page check:** HTTP 200. Title: GitHub - Syarwin/bga-welcometo · GitHub
- **Description:** No description is set on the repository page.
- **Kind:** Game. There is no README and no About text. The root contains BGA game entry-point filenames, which is the basis for this label.
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `version.php`, `welcometo.action.php`, `welcometo.game.php`, `welcometo.view.php`, `welcometo_welcometo.tpl`.
- **README:**

No README text was on the default branch, so there is no paragraph to quote about deployment or structure.

### TacoV/TheQuacksOfQuedlinburg

- **URL:** https://github.com/TacoV/TheQuacksOfQuedlinburg
- **Page check:** HTTP 200. Title: GitHub - TacoV/TheQuacksOfQuedlinburg: Code for the Board Game Arena adaptation of The Quacks Of Quedlinburg · GitHub
- **Description:** Code for the Board Game Arena adaptation of The Quacks Of Quedlinburg Archived on GitHub.
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `thequacksofquedlinburg.action.php`, `thequacksofquedlinburg.game.php`, `thequacksofquedlinburg.view.php`, `thequacksofquedlinburg_thequacksofquedlinburg.tpl`, `version.php`.
- **README:**

> This repos was a start for implementing the game in Board Game Arena. Hoever, the publisher has denied them the license, therefore, this project will be discontinued. The repository is archived. The README does not describe deployment.

### thoun/abyss

- **URL:** https://github.com/thoun/abyss
- **Page check:** HTTP 200. Title: GitHub - thoun/abyss · GitHub
- **Description:** No description is set on the repository page.
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `abyss.action.php`, `abyss.game.php`, `abyss.view.php`, `abyss_abyss.tpl`, `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `version.php`.
- **README:**

> This project is an adaptation for BoardGameArena of game Abyss edited by Bombyx.
> 
> Also add one auto-FTP upload extension (for example https://marketplace.visualstudio.com/items?itemName=lukasz-wronski.ftp-sync) and configure it. The extension will detected modified files in the workspace, including builded ones, and upload them to remote server.

### thoun/ancientknowledge

- **URL:** https://github.com/thoun/ancientknowledge
- **Page check:** HTTP 200. Title: GitHub - thoun/ancientknowledge · GitHub
- **Description:** No description is set on the repository page.
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `ancientknowledge.action.php`, `ancientknowledge.game.php`, `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`.
- **README:**

> This project is an adaptation for BoardGameArena of game Ancient Knowledge edited by Iello.
> 
> Also add one auto-FTP upload extension (for example https://marketplace.visualstudio.com/items?itemName=lukasz-wronski.ftp-sync) and configure it. The extension will detected modified files in the workspace, including builded ones, and upload them to remote server.

### thoun/azul

- **URL:** https://github.com/thoun/azul
- **Page check:** HTTP 200. Title: GitHub - thoun/azul · GitHub
- **Description:** No description is set on the repository page.
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`.
- **README:**

> This project is an adaptation for BoardGameArena of game Azul edited by Plan B.
> 
> Also add one auto-FTP upload extension (for example https://marketplace.visualstudio.com/items?itemName=lukasz-wronski.ftp-sync) and configure it. The extension will detected modified files in the workspace, including builded ones, and upload them to remote server.

### thoun/knarr

- **URL:** https://github.com/thoun/knarr
- **Page check:** HTTP 200. Title: GitHub - thoun/knarr · GitHub
- **Description:** No description is set on the repository page.
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`.
- **README:**

> This project is an adaptation for BoardGameArena of game Knarr edited by Bombyx.
> 
> Also add one auto-FTP upload extension (for example https://marketplace.visualstudio.com/items?itemName=lukasz-wronski.ftp-sync) and configure it. The extension will detected modified files in the workspace, including builded ones, and upload them to remote server.

### thoun/lineit

- **URL:** https://github.com/thoun/lineit
- **Page check:** HTTP 200. Title: GitHub - thoun/lineit · GitHub
- **Description:** No description is set on the repository page.
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `lineit.action.php`, `lineit.game.php`, `lineit_lineit.tpl`, `material.inc.php`, `states.inc.php`.
- **README:**

> This project is an adaptation for BoardGameArena of game Line-It edited by Gigamic.
> 
> Also add one auto-FTP upload extension (for example https://marketplace.visualstudio.com/items?itemName=lukasz-wronski.ftp-sync) and configure it. The extension will detected modified files in the workspace, including builded ones, and upload them to remote server.

### thoun/splendorduel

- **URL:** https://github.com/thoun/splendorduel
- **Page check:** HTTP 200. Title: GitHub - thoun/splendorduel · GitHub
- **Description:** No description is set on the repository page.
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `dbmodel.sql`, `gameinfos.inc.php`, `states.inc.php`.
- **README:**

> This project is an adaptation for BoardGameArena of game Splendor Duel edited by Space Cowboys.
> 
> Also add one auto-FTP upload extension (for example https://marketplace.visualstudio.com/items?itemName=lukasz-wronski.ftp-sync) and configure it. The extension will detected modified files in the workspace, including builded ones, and upload them to remote server.

### utecht/BGA_tigriseuphrates

- **URL:** https://github.com/utecht/BGA_tigriseuphrates
- **Page check:** HTTP 200. Title: GitHub - utecht/BGA_tigriseuphrates: Board Game Arena implementation of Tigris and Euphrates · GitHub
- **Description:** Board Game Arena implementation of Tigris and Euphrates
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** No license is shown on the repository page.
- **BGA files at repository root:** None at the repository root. Other root names seen: `Makefile`, `README.md`, `art`, `tigriseuphrates`.
- **README:**

> BGA Implementation of Tigris and Euphrates.
> 
> Note: Artwork in this repo is low quality placeholder artwork scrounged from the internet. I make no claims of ownership.
> 
> The README does not describe deployment. The game tree is the root directory `tigriseuphrates`, not the usual filenames at the repository root.

### Whebon/dale-of-merchants

- **URL:** https://github.com/Whebon/dale-of-merchants
- **Page check:** HTTP 200. Title: GitHub - Whebon/dale-of-merchants: Board Game Arena adaptation of Dale Of Merchants · GitHub
- **Description:** Board Game Arena adaptation of Dale Of Merchants
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `daleofmerchants.action.php`, `daleofmerchants.view.php`, `daleofmerchants_daleofmerchants.tpl`, `dbmodel.sql`, `gameinfos.inc.php`, `states.inc.php`.
- **README:**

> Dale of Merchants is a cute deck-building game, originally published by Snowdale Design in 2015 and remastered in 2026. This implementation supports 33 of the 36 animalfolk decks from the six-part Dale of Merchants series. Play Dale of Merchants with 1 – 4 players for free on Board Game Arena. Production version: V0.1.17. The README does not describe how the author uploads the project.

### yansnow78/bga_cacao

- **URL:** https://github.com/yansnow78/bga_cacao
- **Page check:** HTTP 200. Title: GitHub - yansnow78/bga_cacao · GitHub
- **Description:** No description is set on the repository page.
- **Kind:** Game, from the README (and the repository description, when one is set).
- **License:** Other. GitHub shows this when it does not map the repo license to a standard SPDX id. Root license files seen: `LICENCE_BGA`.
- **BGA files at repository root:** `cacao.action.php`, `cacao.game.php`, `cacao.view.php`, `cacao_cacao.tpl`, `dbmodel.sql`, `gameinfos.inc.php`, `material.inc.php`, `states.inc.php`, `version.php`.
- **README:**

> Cacao implementation in php + css + js + sql for BGA. The README says the work uses licensed material from ABACUSSPIELE with their agreement. It does not describe deployment.

Searches were not exhausted past the first API page. The code query for the studio header reported 3296 hits, so more public games exist than the 50 additional repositories opened here. This file stops at the repositories whose pages were actually opened.
