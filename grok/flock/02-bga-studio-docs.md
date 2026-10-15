# BGA Studio documentation notes

Every statement below comes from a page retrieved during this task. Wording in quotation marks is copied from those pages. Nothing here describes a particular board game.

Raw copies are in `C:\Users\ryanh\Dropbox\Ryan\AI-SI-Grok-Tools\BoardGameAreana - Imperial 2030\grok\source-docs\`.

## 1. Pages opened

| URL | Result | Approximate text |
| --- | --- | --- |
| https://en.doc.boardgamearena.com/index.php?title=Studio&action=raw | Succeeded (HTTP 200). This is the Studio article wikitext used below. | about 9,100 characters |
| https://en.doc.boardgamearena.com/api.php?action=parse&page=Studio&prop=wikitext&format=json | Succeeded. Same Studio wikitext inside JSON (`parse.title` = Studio, `pageid` 49). | about 9,400 characters |
| https://en.doc.boardgamearena.com/Studio | Succeeded. HTML title: "Studio - Board Game Arena". | about 43,000 characters of HTML |
| https://en.doc.boardgamearena.com/Studio#Great.2C_I.27m_in.21_..._How_should_I_start.3F | Same Studio article as the row above. The start section is in the raw wikitext. | included in the Studio article |
| https://en.doc.boardgamearena.com/ | Succeeded. Rendered page title is "Help", heading "Help". | about 142,000 characters of HTML |
| https://en.doc.boardgamearena.com/index.php?title=Main_Page&action=raw | Succeeded. Entire body is `#REDIRECT [[Help]]`. | 18 characters |
| https://en.doc.boardgamearena.com/index.php?title=Help&action=raw | Succeeded. Player help index, not a Studio start guide. | about 56,500 characters |
| https://boardgamearena.com/forum/viewtopic.php?f=12&t=15232 | Succeeded as HTML, but the topic text is not in the response. Title is " • Board Game Arena". An iframe has `data-forum-url` `https://forum.boardgamearena.com/viewtopic.php?f=12&t=15232&lang=en`. | about 1.9 million characters of shell HTML |
| https://forum.boardgamearena.com/viewtopic.php?f=12&t=15232&lang=en | Succeeded. Title: "Welcome, advice and licences - Board Game Arena". One post body was extracted. | about 250,000 characters of HTML; about 2,700 characters of post text |
| https://en.doc.boardgamearena.com/index.php?title=First_steps_with_BGA_Studio&action=raw | Succeeded | about 6,700 characters |
| https://en.doc.boardgamearena.com/index.php?title=How_to_join_BGA_developer_team%3F&action=raw | Succeeded | about 5,100 characters |
| https://en.doc.boardgamearena.com/index.php?title=Tutorial_reversi&action=raw | Succeeded | about 48,900 characters |
| https://en.doc.boardgamearena.com/index.php?title=Tutorial_hearts&action=raw | Succeeded | about 66,200 characters |
| https://en.doc.boardgamearena.com/index.php?title=Create_a_game_in_BGA_Studio:_Complete_Walkthrough&action=raw | Succeeded | about 47,700 characters |
| https://en.doc.boardgamearena.com/index.php?title=Studio_file_reference&action=raw | Succeeded | about 4,500 characters |
| https://en.doc.boardgamearena.com/index.php?title=Main_game_logic:_Game.php&action=raw | Succeeded | about 116,000 characters |
| https://en.doc.boardgamearena.com/index.php?title=Main_game_logic:_yourgamename.game.php&action=raw | Succeeded. Body is `#REDIRECT [[Main game logic: Game.php]]`. | 39 characters |
| https://en.doc.boardgamearena.com/index.php?title=State_classes:_State_directory&action=raw | Succeeded | about 29,700 characters |
| https://en.doc.boardgamearena.com/index.php?title=Game_database_model:_dbmodel.sql&action=raw | Succeeded | about 8,700 characters |
| https://en.doc.boardgamearena.com/index.php?title=Game_interface_logic:_Game.js&action=raw | Succeeded | about 97,900 characters |
| https://en.doc.boardgamearena.com/index.php?title=Game_interface_logic:_yourgamename.js&action=raw | Succeeded. Body is `#REDIRECT [[Game interface logic: Game.js]]`. | 43 characters |
| https://en.doc.boardgamearena.com/index.php?title=Game_art:_img_directory&action=raw | Succeeded | about 8,100 characters |
| https://en.doc.boardgamearena.com/index.php?title=Game_interface_stylesheet:_yourgamename.css&action=raw | Succeeded. Not fully read past retrieval. | about 9,400 characters |
| https://en.doc.boardgamearena.com/index.php?title=Game_layout:_view_and_template:_yourgamename.view.php_and_yourgamename_yourgamename.tpl&action=raw | Succeeded | about 8,700 characters |
| https://en.doc.boardgamearena.com/index.php?title=Your_game_mobile_version&action=raw | Succeeded. Not fully read past retrieval. | about 7,100 characters |
| https://en.doc.boardgamearena.com/index.php?title=Translations&action=raw | Succeeded | about 21,900 characters |
| https://en.doc.boardgamearena.com/index.php?title=Options_and_preferences:_gameoptions.json,_gamepreferences.json&action=raw | Succeeded | about 23,500 characters |
| https://en.doc.boardgamearena.com/index.php?title=Game_statistics:_stats.json&action=raw | Succeeded | about 5,800 characters |
| https://en.doc.boardgamearena.com/index.php?title=Game_statistics:_stats.inc.php&action=raw | Succeeded. Body is `#REDIRECT [[Game statistics: stats.json]]`. | 41 characters |
| https://en.doc.boardgamearena.com/index.php?title=Game_material_description:_material.inc.php&action=raw | Succeeded | about 7,500 characters |
| https://en.doc.boardgamearena.com/index.php?title=Game_meta-information:_gameinfos.jsonc&action=raw | Succeeded | about 15,100 characters |
| https://en.doc.boardgamearena.com/index.php?title=Game_replay&action=raw | Succeeded. Not fully read past retrieval. | about 2,100 characters |
| https://en.doc.boardgamearena.com/index.php?title=BGA_game_Lifecycle&action=raw | Succeeded | about 2,300 characters |
| https://en.doc.boardgamearena.com/index.php?title=BGA_Game_licenses&action=raw | Succeeded | about 8,400 characters |
| https://en.doc.boardgamearena.com/index.php?title=Pre-release_checklist&action=raw | Succeeded | about 10,100 characters |
| https://en.doc.boardgamearena.com/index.php?title=Post-release_phase&action=raw | Succeeded | about 11,500 characters |
| https://en.doc.boardgamearena.com/index.php?title=Tools_and_tips_of_BGA_Studio&action=raw | Succeeded. Named on the Studio page as development-environment tips. | about 16,200 characters |
| https://en.doc.boardgamearena.com/index.php?title=BGA_Studio_Guidelines&action=raw | Succeeded. Headings were listed; the body was not read through. | about 18,600 characters |
| https://en.doc.boardgamearena.com/images/5/58/1-why-developing.pdf | Succeeded. Pages 1–3 read. | 219,681 bytes |
| https://en.doc.boardgamearena.com/images/1/1e/2-8-steps-to-realize.pdf | Succeeded. All 10 pages read. | 358,640 bytes |
| https://en.doc.boardgamearena.com/images/7/79/3-thebgaframework.pdf | Succeeded. Pages 1–6 read. | 310,241 bytes |
| https://en.doc.boardgamearena.com/images/9/98/4-gamestates.pdf | Succeeded. Pages 1–4 read. Later pages of this PDF were not read. | 533,451 bytes |
| https://en.doc.boardgamearena.com/images/7/76/5-guidelines.pdf | Succeeded. Pages 1–3 read. Later pages were not read. | 629,738 bytes |

The Help article's "Games" section is a long list of per-game help links. Those links were not opened. The BGA developer terms PDF linked from "How to join" (`http://en.doc.boardgamearena.com/images/0/02/BGA_TC_Dev_en.pdf`) was not retrieved.

## 2. Start-here steps

### 2a. Current Studio page order

Source of the section title and the steps: https://en.doc.boardgamearena.com/index.php?title=Studio&action=raw

The heading is "Great, I'm in! ... How should I start?" The page does not number these items. The order below is the order on that page.

1. "If you didn't already, check the presentations at the top of this page to get the basics."
   Source: https://en.doc.boardgamearena.com/index.php?title=Studio&action=raw
2. "Then, you should checkout the First steps with BGA Studio to make sure that runs fine."
   Source: https://en.doc.boardgamearena.com/index.php?title=Studio&action=raw
3. "After that, we strongly advise you to take one of these game creation tutorials:" Tutorial reversi ("recommended", "closest to the actual BGA implementation and maintained by the BGA team") or Tutorial hearts.
   Source: https://en.doc.boardgamearena.com/index.php?title=Studio&action=raw
4. "Then start editing files and see what happens! ;)"
   Source: https://en.doc.boardgamearena.com/index.php?title=Studio&action=raw
5. "Once you're done with tutorials, you can start a real game (or join existing project)" and the link "Create a game in BGA Studio: Complete Walkthrough".
   Source: https://en.doc.boardgamearena.com/index.php?title=Studio&action=raw
6. "If you have any questions, please check out the Studio FAQ or Contact BGA Studio."
   Source: https://en.doc.boardgamearena.com/index.php?title=Studio&action=raw

The same page says, before that section: "Please see this page: How to join BGA developer team?"

### 2b. Numbered list from the "8 steps" PDF

Source for every item in this list: https://en.doc.boardgamearena.com/images/1/1e/2-8-steps-to-realize.pdf

The Studio page links this PDF as "The 8 steps to create a board game on Board Game Arena". The PDF's join step is an email. The current "How to join" wiki page, retrieved the same day, says to use a form on the Studio site. Both texts are recorded. This file does not decide which one applies.

1. "1 : Check you can do it". "To realize a game on BGA, you need" to know PHP, SQL, HTML and CSS (including "absolute/relative positionning"), and Javascript. "We are using the Dojo framework on BGA, but only a few methods are necessary".
   Source: https://en.doc.boardgamearena.com/images/1/1e/2-8-steps-to-realize.pdf
2. "2 : Tell us !" "Tell us you want to join the Studio developers team. Just write an email to « contact (at) boardgamearena.com » saying that you volunteer to create a game on the platform."
   Source: https://en.doc.boardgamearena.com/images/1/1e/2-8-steps-to-realize.pdf
3. "3 : Volunteer for a game". "When you see a board game that you want to adapt, you just have to volunteer to realize it." "First and most important rule : choose a game you love to play!" "Second rule : choose a simple game for your first realization".
   Source: https://en.doc.boardgamearena.com/images/1/1e/2-8-steps-to-realize.pdf
4. "4 : Setup your environment". "you don't have to setup such a development environment, we've created one for you!" "BGA Studio (studio.boardgamearena.com) is a website just like BGA". "To start, we create 10 player accounts for you" and "the skeleton of a game".
   Source: https://en.doc.boardgamearena.com/images/1/1e/2-8-steps-to-realize.pdf
5. "5 : Develop your game". Resources listed: "BGA games examples", "BGA Studio wiki documentation", "BGA developers forum". "we won't do any support on languages-related issues."
   Source: https://en.doc.boardgamearena.com/images/1/1e/2-8-steps-to-realize.pdf
6. "6 : Test your game". "it's also a test plateform where you can invite friends". "When you register to Studio, you get 10 accounts".
   Source: https://en.doc.boardgamearena.com/images/1/1e/2-8-steps-to-realize.pdf
7. "7 : Submit your game". "BGA team review": "Once you submit your game, BGA team try the game with you and check if the adaptation is good enough for publisher review." "Publisher review": "the game publishers gives the final « GO » for the adaptation."
   Source: https://en.doc.boardgamearena.com/images/1/1e/2-8-steps-to-realize.pdf
8. "8 : Launch!" "« Silent launch »" "During a first period of 2-5 days, your game will be made available on Board Game Arena without any advertisement." Then "Beta phase": "the game is officially published on the plateform in « Beta » state. The game will remains in Beta state until there's no more major bugs."
   Source: https://en.doc.boardgamearena.com/images/1/1e/2-8-steps-to-realize.pdf

### 2c. "How to join" then "how to start" after registration

Source: https://en.doc.boardgamearena.com/index.php?title=How_to_join_BGA_developer_team%3F&action=raw

1. "Go to https://studio.boardgamearena.com/"
2. "Find section 'Join the BGA Studio developers team'."
3. "Fill the form and submit".
4. "To register, you must agree with BGA Terms & Conditions for developers."
5. "Once registered, you will get this by email:" SFTP login/password, database login/password, and "ten logins with numeric suffixes from 0 to 9".
6. "Then... well that's all, you can start!" and a link back to "Great, I'm in! ... How should I start?"

### 2d. First steps, "Let's code!" numbered list

Source: https://en.doc.boardgamearena.com/index.php?title=First_steps_with_BGA_Studio&action=raw

1. "To launch your game from Studio go to CONTROL PANEL -> Manage games -> <your_game> -> <your_game_page> -> Play" or `https://studio.boardgamearena.com/studiogame?game=<your_game>`.
2. "Press Create to create a table".
3. "Select number of players and select Training mode in game configuration panel".
4. "Click Express start. Do not use 'Start game' buttons in studio". "When using Express start your game launches with the maximum number of players specified using your own dev player accounts (dev0, dev1, dev2, etc)." "for Solo mode you do actually want to use Start Game instead of Express start".
5. "Game will open with an empty canvas".
6. "Edit the <your_game>.js file (tutorial: modules/js/Game.js), and add a sentence in the HTML part of the line `this.bga.gameArea.getElement().insertAdjacentHTML`, then save".
7. "Go back to your browser and refresh, check that the game zone has updated."
8. "Click the red arrow next to a test account's name in the player panel".
9. "Open the menu ... and choose 'Express STOP'."

Commit steps on the same page:

1. "Enter your commit comment (such as 'My first commit') then hit the 'Submit' button".
2. "Check the log for errors", which "should end with" "Transmitting file data .", "Committed revision #revision number#.", "HAL says: done."

The same page also says: "NOTE: committing the code is currently not working until admin commits it manually the first time."

## 3. Project files and the role the file-reference page gives

Source unless noted: https://en.doc.boardgamearena.com/index.php?title=Studio_file_reference&action=raw

| File or directory | Role sentence from that page |
| --- | --- |
| `img/` | "This directory contains the images for your game (the game art)." |
| `gameinfos.jsonc` | "In this file you describe the meta-information for your game: game name, publisher name, number of player, etc..." |
| `dbmodel.sql` | "File for creating specific database tables that you will need to persist data during the game (for example a table for cards)." |
| `gameoptions.json`, `gamepreferences.json` | "File for describing your game options (or game variants)." |
| `<gamename>.css` | "CSS styles specific to your game." |
| `modules/php/Game.php` | "This is the main file for your game logic." The next sentence is: "Here you initialize the game, persist data, implement the rules and notify changes to the client interface." |
| `modules/js/Game.js` | "This is the main file for your game interface." The page then says it defines "which actions on the page will generate calls to the server" and "what happens when you get a notification for change from the server". |
| `<gamename>.view.php`, `<gamename>_<gamename>.tpl` | "Files are used to set up the page layout ('view') for the game." The same page says "These files are deprecated". |
| `material.inc.php` | "File used to describe all the game material (cards with their description, dices, tokens...)." The same page says "This file is deprecated". |
| `modules/php/States` | "The classes describing the states of your game." |
| `states.inc.php` | "This file describes the game states machine of your game (all the game states properties, and the transitions to get from one state to another)." The same page says "This file is deprecated". |
| `stats.json` | "File used to list statistics that you want to update during the game to be presented to players at the end of the game." |
| `modules/` | "Modules directory can contain additional php files which can be included in main game.php via include or require. It also can contain addition js files." |
| `misc/` | "Directory containing files you would like to keep with project but not needed on production server." Same sentence block: "Total limit is 1 Mb for this directory." |
| other files outside `modules/` | "You can use other files but they won't be checked in source control and published in production." |

The options page gives a split the file-reference page does not: "In `gameoptions.json`, you can define your game options (i.e. game variants)." "In `gamepreferences.json`, you can define user preferences." Source: https://en.doc.boardgamearena.com/index.php?title=Options_and_preferences:_gameoptions.json,_gamepreferences.json&action=raw

The pre-release checklist, not the file-reference page, says: "Fonts should be placed to 'fonts' directory" and "Sounds should be placed to 'sounds' directory". Source: https://en.doc.boardgamearena.com/index.php?title=Pre-release_checklist&action=raw

The walkthrough says rules PDFs go in `doc/` and are excluded from version control, and that `misc/` "will hold up to 1 Mb". Source: https://en.doc.boardgamearena.com/index.php?title=Create_a_game_in_BGA_Studio:_Complete_Walkthrough&action=raw

## 4. Architecture facts the retrieved docs state

### Languages and versions

- "How to join" says a non-experienced developer is "required to know or learn 6 languages: JavaScript, PHP, SQL, HTML, CSS and English". Source: https://en.doc.boardgamearena.com/index.php?title=How_to_join_BGA_developer_team%3F&action=raw
- Studio "Software Versions": "Dojo Toolkit 1.15 - deprecated, avoid at all cost"; "PHP: 8.4"; "SQL: MySQL 5.7 (prod) - on studio 8.0"; "Font Awesome: 4.7" and "Font Awesome: 6.4.0". Source: https://en.doc.boardgamearena.com/index.php?title=Studio&action=raw
- The walkthrough says: "BGA has a modern framework (2024+) that uses PHP state classes, TypeScript (encouraged but not mandatory), JSON config files, and attribute-based action declarations." It says `states.inc.php`, `material.inc.php`, `gameoptions.inc.php`, `stats.inc.php`, and "heavy Dojo usage" are "the old patterns." Source: https://en.doc.boardgamearena.com/index.php?title=Create_a_game_in_BGA_Studio:_Complete_Walkthrough&action=raw
- The 8-steps PDF still says "We are using the Dojo framework on BGA". Source: https://en.doc.boardgamearena.com/images/1/1e/2-8-steps-to-realize.pdf

### Server / client split

- Game.php: "This is the main class that implements the 'server' callbacks. As it is a server it cannot initiate any data communicate with the game client (running in browser) and only can respond to client using notifications." "Your php class instance won't be in memory between two callbacks". Source: https://en.doc.boardgamearena.com/index.php?title=Main_game_logic:_Game.php&action=raw
- Game.js: "This is the main file for your game interface." It defines "Which actions on the page will generate calls to the server" and "What happens when you get a notification for a change from the server". Source: https://en.doc.boardgamearena.com/index.php?title=Game_interface_logic:_Game.js&action=raw
- Framework PDF, pages read: the framework is for a game "played in realtime", "played by several human players", "played from an internet browser", with "rules enforcement (ie : no possibility to cheat)." Server side has "The game database", "The game logic", and "The game resources" ("images, stylesheets"). Client side is "the user interface (UI)." Source: https://en.doc.boardgamearena.com/images/7/79/3-thebgaframework.pdf
- Active versus current player, Game.php: "The active player is the player whose turn it is". "The current player is the player who sent the request". Source: https://en.doc.boardgamearena.com/index.php?title=Main_game_logic:_Game.php&action=raw

### State types

Source: https://en.doc.boardgamearena.com/index.php?title=State_classes:_State_directory&action=raw

"You can use 4 types of game states:"

- `StateType::ACTIVE_PLAYER`: "One player is active and must play ('activeplayer' if using the old array notation)."
- `StateType::MULTIPLE_ACTIVE_PLAYER`: "Multiple players can be active and must play ('multipleactiveplayer' if using the old array notation)."
- `StateType::PRIVATE`: "During multiactive states players can independently move to different private parallel states ('private' if using the old array notation)."
- `StateType::GAME`: "No player is active. This is a transitional state to do something automatic specified by the game rules ('game' if using the old array notation)."

Also from that page: "Number 1 is reserved for the first game state". "Number 99 is reserved for the last game state". "Only game, id and type are mandatory". "At least one of your game states (any one) must specify" `updateGameProgression: true`. Initial state is the class returned from `setupNewGame`. "If you don't return anything its state 2 (*to be confirmed*)".

The game-states PDF, pages read, says a state machine decides status-bar text, which actions are allowed, which players are "active", automatic server actions, client interface adaptations, and "what are the next possible game states." Source: https://en.doc.boardgamearena.com/images/9/98/4-gamestates.pdf

The state-classes page says to read that presentation "but ignore the code snippets, they are outdated".

### Database

Source: https://en.doc.boardgamearena.com/index.php?title=Game_database_model:_dbmodel.sql&action=raw

- "you specify the database schema of your game."
- "you can't change the database schema during the game."
- "By default, BGA creates four tables for your game: global, stats, gamelog, and player."
- "You MUST NOT MODIFY the schemas of the global, stats, or gamelog tables, and any bga_ prefixed table".
- "You may add columns to the player table" but "must not alter existing columns".
- "Always add IF NOT EXISTS". "Always set ENGINE=InnoDB DEFAULT CHARSET=utf8mb4".
- "all CREATE/ALTER tables and views should be in dbmodel.sql."
- "if size of all table (including system tables) exceeds 64Mb it will stop working."

Game.php: "BGA uses database transactions." "your database changes WON'T BE APPLIED to the database until your request ends normally". "if your game logic detects that something is wrong ... throw an exception and all changes to the game situation will be removed." Source: https://en.doc.boardgamearena.com/index.php?title=Main_game_logic:_Game.php&action=raw

### Notifications

Source: https://en.doc.boardgamearena.com/index.php?title=Main_game_logic:_Game.php&action=raw

- "Everything which players see, including all changes which happen on frontend (including setup), are done via notfications."
- "Notifications are queued, i.e. sent at the very end of the action, when it ends normally."
- "There are conceptually two types of notification: public ... private".
- Public method named on the page: `bga->notify->all(...)`. "NO private data must be sent with this method".
- "the total notification size is now limited to 128K."

Game.js: "When something happens on the server side, your game interface Javascript logic received a notification." `setupPromiseNotifications` registers functions "starting with `notif_`". The notification object attributes listed include `type`, `log`, `args`, `bIsTableMsg`, `move_id`, `table_id`, `time`, `uid`. Source: https://en.doc.boardgamearena.com/index.php?title=Game_interface_logic:_Game.js&action=raw

### Views

Source: https://en.doc.boardgamearena.com/index.php?title=Game_layout:_view_and_template:_yourgamename.view.php_and_yourgamename_yourgamename.tpl&action=raw

- "IMPORTANT NOTE: These files are deprecated, you shouldn't need to use it if you generate the template from the JS file."
- "There are two files involved in overall game layout: yourgamename.view.php and yourgamename_yourgamename.tpl."
- "Your view and your template are supposed to generate only the BASE layout of the game."
- "You shouldn't try to setup the current game situation in the view: this is the role of your Javascript code."
- "BGA is using the phplib template system".

The walkthrough says: "In the modern framework, you generate all HTML from JavaScript/TypeScript — there is no template engine (`.tpl` / `.view.php` files are no longer used)." Source: https://en.doc.boardgamearena.com/index.php?title=Create_a_game_in_BGA_Studio:_Complete_Walkthrough&action=raw

### Statistics and options, short

- `stats.json`: "you are describing game statistics, that will be displayed at the end of the game." "There are 2 types of statistics: table statistics ... player statistics". Types: "int", "float", and "bool". "Statistics IDs must be >=10". "(Number of table statistics) + (Number of player statistics × Maximum number of players) should not exceed ~930, or the game will crash." Source: https://en.doc.boardgamearena.com/index.php?title=Game_statistics:_stats.json&action=raw
- Options are "selected by the table creator and usually correspond to game variants". Preferences are "personal choices of each player only visible to that specific player". Source: https://en.doc.boardgamearena.com/index.php?title=Options_and_preferences:_gameoptions.json,_gamepreferences.json&action=raw

### Translations

Source: https://en.doc.boardgamearena.com/index.php?title=Translations&action=raw

- "Localization for BGA games happens largely on the CLIENT. Games must be developed in English".
- "Once your game enters Beta, the BGA player community will" translate it.
- Server strings that must be translated are wrapped in `clienttranslate()`. Client strings use `_()`.
- "A string used as the message for notify->all or notify->player will automatically have its translation displayed on the client" if wrapped in `clienttranslate()`.
- Pre-game option strings use `totranslate()`, not `clienttranslate()`.

## 5. Asset and art rules the docs state

Source unless noted: https://en.doc.boardgamearena.com/index.php?title=Game_art:_img_directory&action=raw

- "Requesting graphics assets is a 2nd thing you should do after getting the game license."
- Ask for "printed SQUARE materials (cards, boards)" in "pdf, jpg, png". "PDF cannot have watermarks, cut or bleed marks."
- "non NON-SQUARE tokens (i.e hex) in PNG".
- "For all assets that have text on them (numbers don't count): We need ENGLISH or NO TEXT version."
- "Game metadata images are images of game box, banner, title, etc. These images are no longer stored in project directory." They are "managed through the Game Metadata Manager."
- "You must upload in img directory all images of your game interface."
- "images file names should not contain spaces or parentheses."
- "by default, ALL images of your img root directory are loaded on a player's browser". "don't publish images that are not useful in your img". Subdirectories "won't be preloaded by default".
- "General recommendation it to have no more than dozen of image files, 2Mb max each."
- Formats: "webp images should be used whenever possible." "jpg images should be used for non-transparent images." "png images should be used for images with transparency". "gif images can be used for animated images" but "not recommended". "svg images can be really efficient for icons".
- "png and jpg images are automatically converted to webp during deployment."
- "Do not make any CSS image sprite with dimensions that exceed 4096x4096 pixels". "the maximum image size should be 4096x4096".
- "use higher resolution images than needed" and CSS `background-size`.

Pre-release checklist, same topic: "Each image should not exceed 4Mb". "Total size should not exceed 15Mb". "Space around the box has to be transparent, not white." "If you use extra fonts, they should be freeware". Source: https://en.doc.boardgamearena.com/index.php?title=Pre-release_checklist&action=raw

Walkthrough: "you don't commit original publisher graphics files". Source: https://en.doc.boardgamearena.com/index.php?title=Create_a_game_in_BGA_Studio:_Complete_Walkthrough&action=raw

Guidelines PDF, pages read: "Fidelity to the original game is an absolute requirement." "Don't try to create a video game: make your game interface as close as possible to how the original board game looks like." "If a player knows the real board game, he should be able to play your adaptation with no learning." Source: https://en.doc.boardgamearena.com/images/7/76/5-guidelines.pdf

## 6. Publishing, review, and license statements

### Lifecycle table

Source: https://en.doc.boardgamearena.com/index.php?title=BGA_game_Lifecycle&action=raw

Quoted cells:

- Initial: "You can choose to join an existing team / create a new project".
- Assigned: "You choose a game" / "You can start the development of the game".
- Pre-alpha: "You've started to write some code" / "You develop the game. During this phase, we can assist you with the framework and give you some advice."
- Alpha: "Follow Pre-release checklist, then tell us that your development is finished" / "'BGA review': we are reviewing your game and checking that it respects BGA guidelines. If not, we will ask you (and help you) to fix it." "Publisher review: the publisher, the designer, we and you can test the game together and separately."
- Public beta: "The adaptation should be approved by the publisher while receiving enough approvals from reviewers before requesting beta." "Having 10+ approvals is recommended, but if the game is well-received (preferably game rating ≥4.5) and there are no pending bugs and issues the game may pass as administrative discretion." "All players can play!"
- Gold: "The game is stable on BGA. The publisher must send a mail to publishers@boardgamearena.com to request the official release". "We find together a good launch date for the game, we announce the game on BGA news."

### License page, quoted

Source: https://en.doc.boardgamearena.com/index.php?title=BGA_Game_licenses&action=raw

- "Almost all games on the Board Game Arena platform are adaptations of existing commercial 'real' board games. In order to host an adaptation of one of these board games on a website, the copyright owners must first grant a license/authorisation to this website."
- "Yes, for all games that are not in the public domain, BGA has been granted an authorisation to create and host an online version."
- "We allow developers to start any project in the Studio. But when you submit your project to go live on BGA, it will be rejected during the review process if BGA doesn't hold a proper license for the game." "Exception: games in the public domain are of course not concerned."
- "To release the implementation as a public game, the publisher must approve the game during alpha test phase. Without publisher support your game will remain private indefinitely."
- "The copyright owners have to give an license/authorisation to BGA." "Publishers do not have to pay anything to BGA for this, they just need to give their 'go.'"
- "We will only make accessible published games that can be bought somewhere, or will be in a near future." "Any other games like prototypes, self-published, print-n-play, ... can be coded on the Studio. But on the production side, it will not go further than private alpha".
- "as a rule of thumb, we do not ask more than one game to a publisher at a time."

### Pre-release checklist, quoted

Source: https://en.doc.boardgamearena.com/index.php?title=Pre-release_checklist&action=raw

- "If you think your game is ready to be reviewed by by BGA admins and/or Publisher (aka go to Alpha stage) please consult this checklist first".
- "BGA must have a license for the game for a project to be moved to production, even to alpha."
- "Click on the Request ALPHA status button". "You cannot deploy yourself from the 'manage game' page until this first ALPHA deploy has been done by the admins."
- "The implementation must be approved by the publisher (if not a public domain game)".
- "Click on the Request BETA status button".

### Walkthrough release headings

Source: https://en.doc.boardgamearena.com/index.php?title=Create_a_game_in_BGA_Studio:_Complete_Walkthrough&action=raw

- Private alpha: "create a build and click on the 'Request PRIVATE ALPHA status' button and admins will check your game starts, has something to show, and push it to private alpha."
- Alpha: "create a build and click on the 'Request PUBLIC ALPHA status' button".
- Beta: "When your game has enough reviewers approvals, and the publisher has approved it too, you can 'Request BETA status'."

### Post-release

Source: https://en.doc.boardgamearena.com/index.php?title=Post-release_phase&action=raw

- "Your game is now on BGA: congrats!" "you're still allowed to modify your game."
- Submit path: "Commit & build a new version now", then "Deploy to production".
- "Some changes will break the games in progress". Examples named: "Changes in the database schema", "New global variable or game option accessed during the game", "Change ID of existing game states", "Changing flow of game states".
- "Do not change option IDs once the game is in production".

### Forum post retrieved

Source: https://forum.boardgamearena.com/viewtopic.php?f=12&t=15232&lang=en

The extracted post is by "Een", "24 April 2020", topic "Welcome, advice and licences". Quoted:

- "Except for smaller learning projects, please check with us about the license by sending an email at studio@boardgamearena.com ."
- "Start small!"
- "Please take the time to read the guidelines".
- "Please set the correct 'bgg_id' ... in the gameinfos.inc.php".

### Code ownership sentence from the join page

"The code you wrote will remain with BGA and they can do whatever they want with it (but you can also do whatever you want with your own copy)". Source: https://en.doc.boardgamearena.com/index.php?title=How_to_join_BGA_developer_team%3F&action=raw

The developer terms PDF linked from that page was not retrieved, so its clauses are not quoted here.

## 7. SSH keys, SFTP host, SFTP port

Stated on the pages opened:

- "How to join": the registration email contains "one login / password to access files through SFTP". It does not name a host or port. Source: https://en.doc.boardgamearena.com/index.php?title=How_to_join_BGA_developer_team%3F&action=raw
- First steps: "From the initial email from the Studio you get: the name of the SFTP server to connect to; your SFTP login and password". "this is NOT the same login/password as dev account". "You can also upload your ssh key via studio control panel to avoid password exchange https://studio.boardgamearena.com/controlpanel". This page does not print a host name or a port. Source: https://en.doc.boardgamearena.com/index.php?title=First_steps_with_BGA_Studio&action=raw
- Tools and tips, "File Sync": "IMPORTANT NOTE: The ssh port is 2022". "IMPORTANT NOTE 2: If you uploaded ssh key - PASSWORD method is automatically disabled, you can no longer use password". Examples use host `1.studio.boardgamearena.com` and port `2022`: `sftp://1.studio.boardgamearena.com:2022`, `sshfs -p 2022 myusernamehere@1.studio.boardgamearena.com:`, and `lftp sftp://myuser:mypassword@1.studio.boardgamearena.com:2022/`. Source: https://en.doc.boardgamearena.com/index.php?title=Tools_and_tips_of_BGA_Studio&action=raw

The Studio article itself does not mention SSH, SFTP, a host, or a port.

## 8. Open questions these pages did not answer

These are unanswered by the pages opened. They are not answered here.

- The pages say the SFTP server name, SFTP login, SFTP password, and database login/password are in the welcome email. They do not contain those values.
- Tools and tips uses `1.studio.boardgamearena.com` inside examples. First steps says the server name comes from the email and does not say that every account uses that host. The pages do not say whether that hostname is mandatory.
- The pages do not state a database hostname, a database port, or a PhpMyAdmin URL beyond "Go to game database" inside a running Studio game and the Reversi tutorial's `https://studio.boardgamearena.com/db/`. The Reversi page says the PhpMyAdmin username and password are in the welcome email. Those values are not on the pages.
- The 8-steps PDF says to join by emailing contact@boardgamearena.com. The current join page says to use the form on https://studio.boardgamearena.com/. The pages do not say which instruction replaces the other.
- The developer terms PDF was linked and not retrieved, so what "agree with BGA Terms & Conditions for developers" requires is not in these notes.
- The game-states PDF and the guidelines PDF were only partly read (pages 1–4 and 1–3). Later pages of those two PDFs were not retrieved into these notes.
- The Help main page is a list of player game-help articles. It does not say how a Studio project is published.
- The forum shell at https://boardgamearena.com/forum/viewtopic.php?f=12&t=15232 did not include the post text. The frame page yielded one post. These notes do not establish whether later replies exist in a different HTML shape.
- Studio file reference says `states.inc.php` and the view/template files are deprecated, and the walkthrough says they are not used. The state-classes page still says "If you don't return anything its state 2 (*to be confirmed*)". The pages do not resolve that confirmation.
- `game-interface-stylesheet`, `your-game-mobile-version`, `game-replay`, and the body of `BGA Studio Guidelines` (wiki) were retrieved and not read through, so rules that exist only in those unread bodies are not in this file.

## Headings and the instructions under them

### Studio

Source: https://en.doc.boardgamearena.com/index.php?title=Studio&action=raw

- "What is Board Game Arena Studio?" — "a platform to build online board game adaptations". "open to any gamer with software development skills". Website: https://studio.boardgamearena.com
- "Discover BGA Studio in 5 presentations" — five linked decks: why use Studio, the 8 steps, the framework at a glance, the game state machine, and developer guidelines, each with a PDF on en.doc.boardgamearena.com.
- "How to join the BGA developer team?" — "Please see this page: How to join BGA developer team?"
- "Great, I'm in! ... How should I start?" — presentations, then First steps, then Tutorial reversi or Tutorial hearts, then edit files, then the complete walkthrough. Search tip: enter `Category:Studio` plus the search words.
- "BGA Studio documentation" / "BGA Studio Framework reference" — "functions and methods available to build your game", then the file, server, client, and other-component links listed in the raw file.
- "BGA Studio game components reference" — "useful tools you can use in your game adaptations", with one-line roles for Counter, Scrollmap, Stock (deprecated), Zone, Draggable, ExpandableSection, Anti-Stock, bga-zoom, bga-animations, bga-cards, bga-dice, bga-autofit, bga-score-sheet, bga-jump-to, ItemManager, Deck (deprecated), and PlayerCounter and TableCounter.
- "BGA Studio user guide" — lifecycle, licenses, walkthrough, pre-release checklist ("Go throught this list if you think you done development"), post-release, guidelines, tutorials checklist, tools, cookbook, FAQ, and sharing links.
- "Software Versions" — the versions in section 4.
- "PHP Extensions Used" — a space-separated list "as of Apr 1, 2026", including Core, curl, gd, mysqli, pdo_sqlite, redis, zip, Zend OPcache, and others in the raw file.
- "Other resources" — development forum, Studio bug tracker, Discord invite, developer blogs, mainsite releases topic, and Contact BGA Studio.
- Note at the top: "Please DO NOT translate Studio Documentation".

### How to join

Source: https://en.doc.boardgamearena.com/index.php?title=How_to_join_BGA_developer_team%3F&action=raw

- "Is this right for me" — it is right if you like board games and programming, want to fix bugs, want a public-domain game, or were hired to adapt a game. It is not the place for an unpublished prototype as a public BGA game, for a non-board-game, or for expecting "a lot of money". Required skills are the six languages plus OOP, web, database, file sync, and image tools. "Nothing is really expected" from a volunteer, but a published game's bugs are "generally expected" to be fixed by the author. "The code you wrote will remain with BGA".
- "How to create BGA Studio development account" — the form steps in section 2c. Email subject to search: "Welcome on BGA Studio". Resend link: `https://studio.boardgamearena.com/account?page=welcomeemail`.
- "Ok, I registered, how to start?" — "you can start!" and the link to the Studio start section.

### First steps

Source: https://en.doc.boardgamearena.com/index.php?title=First_steps_with_BGA_Studio&action=raw

- "Connect to the BGA Studio website" — go to http://studio.boardgamearena.com and log in with the "first dev account (ex: myusername0, password was sent in welcome email)".
- "Create a new game project" — "Manage Games" then "Create a new TUTORIAL project", or https://studio.boardgamearena.com/studio#new-tutorial . "your project name should be something like 'tutorialbob'". "At this stage it is too early to create a real game".
- "Set up dev environment ide, editor and File Sync" — use the email's SFTP server name and SFTP login. Download the project. "You have to setup AUTOMATED sync". "manually ftp'ing files would be no-starter." SSH key upload is optional, via the control panel.
- "Let's code!" — the numbered list in section 2d.
- "Commit your changes" — commit from "Control Panel / Manage Games / Your game / Commit my modifications now". The note says the first commit "is currently not working until admin commits it manually".
- "That's all!" — "select one of the tutorials".

### Complete walkthrough, level-2 headings

Source: https://en.doc.boardgamearena.com/index.php?title=Create_a_game_in_BGA_Studio:_Complete_Walkthrough&action=raw

- "Introduction" — "not a tutorial, but step by step instructions". Finish a tutorial first. "Don't bother trying to create a new game until you have completed at least one of the tutorials."
- "Select a First Game" — choose from "Available Licenses" or "Public Domain". "Don't start a project until you are sure BGA have the licence for this game, or it will never be published to BGA!" Check current projects before creating one.
- "Create a project" — create it, express-start it, change client text to confirm sync, set status to "development started" or "waiting for the license" or "waiting for graphics".
- "Development Tools" — editor ( "VSCode is recommended for TypeScript projects" ), browser dev tools, file sync, BGA web tools, image tools, version control, and "npm, TypeScript compiler, SCSS compiler, rollup/esbuild".
- "Hook version control system" — commit at the start. Do not commit "original publisher graphics" or "a file with your sftp password".
- "Obtain game graphics" — use "Request Art Files" on the license page, or the scavenger-hunt list (generic assets, BoardGameGeek images, web images, PDF extraction).
- "Obtain game documentation" — English rules PDF and other documents, placed in `doc/` and excluded from version control.
- "Update game info and box graphics" — edit `gameinfos.jsonc` from BoardGameGeek data and set metadata images. "Always use 'Express Start'".
- "Fix source copyright" — replace the placeholder copyright with your name in "about 10 files".
- "Reduce the Rules" — "start the game with *reduced* rules". Skip expansions, advanced rules, and "cool animations" at first.
- "Design Game Elements" — map pieces to instance, type, super type, and player color. Database holds instances. "In the new framework, material data lives in a PHP class (e.g. `Material.php`)".
- "Create Initial Layout and Game Graphics" — generate HTML from JS/TS in `setup()`. Use `bga.gameArea.getElement()`. Finish layout, SCSS, player panels, and Material.php before real graphics if needed.
- "Create Database Schema" — "Do it sooner than later". "Anything more complex then one table with 5 columns or two tables will only going to make it harder". Static data stays in Material.php. Dynamic data is the database.
- "Implement Game Setup" — "`setupNewGame` ... is called once when game table is created. LOGGING does not work in this function." The page says to add `setupNewGameTables()` and return a state class.
- "Implement one time game model synchronization" — `getAllDatas` returns what the current player may see. Client `setup()` renders it.
- "Create State Machine" — "game states are defined as PHP classes extending `GameState`" in `modules/php/States/`. "There is no `states.inc.php` file at all." Actions use `#[PossibleAction]`. "If you find yourself with machine with more than 20 states its probably not the way to go."
- "Handle Turn Order" — clockwise natural order needs nothing special. Do not use the `player_no` column for a custom order.
- "Hook User Input" — click handlers in `onEnteringState`, cleanup in `onLeavingState`, then `bga.actions.performAction()`.
- "Implement Notification handling and Animation" — `bga.notifications.setupPromiseNotifications()`. "you should not get carried away with animation". "in general, you should not use any sounds effects beside already provided by framework."
- "Wrap Up" — game progression, per-state `zombie()`, `stats.json`, logs, tiebreaker aux score, translation markers, tooltips.
- "Private alpha" — "Request PRIVATE ALPHA status", then fill rules links and web links on the game page.
- "Alpha" — go through the pre-release checklist, then "Request PUBLIC ALPHA status".
- "Beta" — "Request BETA status" after reviewer approvals and publisher approval.
- "Level Up" — `gameoptions.json`, `gamepreferences.json`, theming, scoring board, animations.
- "After the alpha stage" — see Post-release phase.

### Tutorial reversi, level-2 headings

Source: https://en.doc.boardgamearena.com/index.php?title=Tutorial_reversi&action=raw

The first instruction block under each heading was taken from that file. Code samples under the headings are in the raw file and are not copied here.

- "Introduction" — build Reversi. Before starting: read the presentations, know the rules, know "PHP, SQL, HTML, CSS, Javascript", and set up the environment. Read-only access: `https://studio.boardgamearena.com/projects?game=reversi` with "Already published" checked.
- "Create your first game" — create the tutorial project, Play, "Simple game", "Real time", "Manual", "Express Start". "Always use the 'Express Start' button". End with "Express Stop".
- "Editing the game information (Optional)" — "fix the warnings on the project page (missing BGG_ID and presentation)."
- "Make sure the IDE is properly configured" — an intentional bad property should be underlined. If not, see the VS Code setup page.
- "Make it look like Reversi" — "players with a 1024px screen width must be able to play." "the width of the play area can be 750px (in the worst case)." Build the board in CSS.
- "The Tokens" — add tokens after the board. The page notes that "tokens" and "discs" are used interchangeably.
- "The database" — "To design the database model of our game, you will need to access the database. You won't need to do anything in database UI, yet."
- "Setup the initial game position" — "you must launch the game with two players". `setupNewGame` places "4 tokens on the board."
- "State Machine" — "this is the heart of your game logic." The page points at the state-machine presentation and a diagram file `reversi6.jpg`.
- "The rules" — implement `getPossibleMoves` in PHP to list legal coordinates and to check a chosen spot.
- "Display allowed moves" — add `getArgs` on `modules/php/States/PlayDisc.php` and handle it in a JS state class.
- "Let's play" — click a `possibleMove`, send it to the server, check it, apply the rules, jump to the next player, then update the client.
- "Make the move appear automatically" — subscribe to `playDisc` and `turnOverDiscs` with promise-based notifications.
- "Implement the zombie mode" — "When a player leave the table, a Zombie (bot) will play for the leaver". The tutorial says to "random play one of the possible moves".
- "Add a debug function to help up test the code" — a `debug_` function "can be triggered in the Studio with a special menu" and uses `$this->debug->playUntil`.
- "Optional: add unit tests" — follow the Testing by developer PHP section. The page says the example run "should be 4/4 OK".
- "After the tutorial" — do the other tutorial or the complete walkthrough.

### Tutorial hearts, level-2 headings

Source: https://en.doc.boardgamearena.com/index.php?title=Tutorial_hearts&action=raw

- "Introduction" — build Hearts. Requirements match Reversi, plus "access to your ftp home folder" so the published hearts sources can be copied locally. "please do not use the hearts project code as a base."
- "Hearts Rules" — four players, "fewest points", hearts are 1 point, "Queen of Spades (13 points)", 13 cards, pass three cards, "2 of Clubs starts".
- "Create your first game" — project name `heartsYOURNAME`, or reuse the First Steps project. Express-start with 4 players in turn-based mode, change the `.js` text, express-stop. "The browser caches images." Changed images need "full reload" (Ctrl+F5).
- "Hook version control system" — commit or at least back up. The page links `https://github.com/elaskavaia/bga-heartsla` and says "Different revisions represent different steps".
- "Update game infos and box graphics" — edit `gameinfos.jsonc` from BoardGameGeek. The page says "Original release 1850".
- "Layout and Graphics" — copy the card sprite from `https://x.boardgamearena.net/data/others/cards/FULLREZ_CARDS_ORIGINAL_NORMAL.jpg` into `img/cards.jpg`, then add player-table and hand divs.
- "Game Interface with BGA Cards" — client component is BgaCards. Server side "we will use ItemManager". The sprite is "a 15x4 grid".
- "Game Database and Game Initialization" — "define our cards with ItemManager".
- "Full Game Model Synchronization" — fix `getAllDatas` "to return all possible data we need to reconstruct the game."
- "State Machine" — read the state-machine presentation and "ignore all the source snippets in this presentation, as framework changed".
- "Client - Server Interactions" — click sends ajax, server updates the database and sends a notification, client animates from the notification.
- "Zombie turn" — implement `zombie` in `PlayerTurn.php`, then use the bug menu function "playAutomatically".
- "Scoring and End of game handling" — the tutorial's simplified rule is "score -1 point per heart" and "game will end when somebody goes -100 or below."
- "Clean Up" — remove template leftovers and the old deal-from-`setupNewGame` debug code. Dealing moves to the `stNewHand` handler.
- "Rule Enforcements" — put card queries in `CardManager.php` and send valid ids privately through state args.
- "Fix first player with 2 of clubs" — replace the FIXME in `NewHand.php`. "location_arg is the player id when a card is in location 'hand'."
- "Spectator support" — "hide the hand control" when `isCurrentPlayerSpectator()` is true. "Click Test Spectator".
- "Improve UI" — "We need to fix a few things in the UI still." Subsections in the file are center player areas, card-play animations, card sorting, and tooltips.
- "Game progresstion" — `getGameProgression` returns `-1 *` the minimum player score so that "close to -100" is "close to 100% game completion".
- "Additional stuff" — not implemented in the tutorial: starting-suit marker, start at 100 and end at 0 or below, Queen of Spades and 26-point reverse scoring, statistics, card-exchange states, and an option to start at 75 instead of 100.
- "After the tutorial" — the other tutorial or the complete walkthrough.

### Documentation main page (Help)

Source: https://en.doc.boardgamearena.com/index.php?title=Help&action=raw

- "An issue? A question?" — "Frequently asked questions is the most complete source of help for BGA." Forums "are also helpful".
- "Games" — "Red game names need game help/summaries written for them." The body is a list of `Gamehelp...` links. Those pages were not opened.
- "About available games and their content" — this heading is present. Its body was not read past the heading list.

### Presentations, pages actually read

- Why PDF: "1 : To reach a critical mass of players" ("more than 40.000 players") and "2 : To get digital rights" ("We are negociating with digital right owners for you"). Later reasons in that PDF were not read. Source: https://en.doc.boardgamearena.com/images/5/58/1-why-developing.pdf
- Framework PDF pages 1–6: intro, "Clients & server", "The server side", "The client side", as quoted in section 4. Later pages were not read. Source: https://en.doc.boardgamearena.com/images/7/79/3-thebgaframework.pdf
- Game-states PDF pages 1–4: "Why a game state machine?", "What is a game state machine?" (example names `gameSetup`, `playerTurn`, `nextPlayer`, `gameEnd`), and "Game state & BGA". Later pages were not read. Source: https://en.doc.boardgamearena.com/images/9/98/4-gamestates.pdf
- Guidelines PDF pages 1–3: "Why guidelines?" and "General guidelines", quoted in section 5. Later pages were not read. Source: https://en.doc.boardgamearena.com/images/7/76/5-guidelines.pdf
