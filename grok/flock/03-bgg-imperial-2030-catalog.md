# BoardGameGeek catalog: Imperial 2030 (thing 54138)

Retrieved 2026-10-15. This file lists only fields returned by the requests below. HTML tags in description and wiki text were removed for reading; the wording is otherwise the site text. Nothing here was filled in from memory after a failed or truncated response.

## Retrieval log

| Request | Result |
| --- | --- |
| `https://api.geekdo.com/api/geekitems?objectid=54138&objecttype=thing` | HTTP 200. Source for identity, description, credits, and the `wiki` field. |
| `https://api.geekdo.com/api/files?objectid=54138&objecttype=thing&pageid=1&showcount=100` | HTTP 200. `config.numitems` 28, `config.endpage` 1. |
| `https://api.geekdo.com/api/images?objectid=54138&objecttype=thing&pageid=1&showcount=100&galleries=true` | HTTP 400 body: `{"title":"Invalid galleries","type":"about:blank"}`. |
| `https://api.geekdo.com/api/images?objectid=54138&objecttype=thing&pageid=1&showcount=100` | HTTP 200. `pagination.total` 217, `pagination.perPage` 60 (the API did not return 100), `pagination.pageid` 1, `config.endpage` 4. |
| `https://api.geekdo.com/api/images?objectid=54138&objecttype=thing&pageid=2&showcount=100` | HTTP 200. 60 images, `pagination.pageid` 2, `pagination.total` 217. No image id overlap with page 1. |
| `https://api.geekdo.com/api/videos?objectid=54138&objecttype=thing&pageid=1&showcount=100` | HTTP 200. `config.numitems` 35, `config.endpage` 1. |
| `https://boardgamegeek.com/xmlapi2/thing?id=54138&stats=1` | HTTP 403. Cloudflare "Just a moment..." challenge page. No thing XML was retrieved, so ranks, ratings, and weight are not listed. |
| `https://boardgamegeek.com/boardgame/54138/imperial-2030` | HTTP 403. Cloudflare challenge. The HTML game page was not retrieved. |
| `https://boardgamegeek.com/wiki/page/thing:54138:moreinfo` | HTTP 403. Cloudflare challenge. The HTML wiki page was not retrieved. The differences text below is the `wiki` field on the geekitems JSON, not a successful fetch of that wiki URL. |
| `https://boardgamegeek.com/boardgame/54138/imperial-2030/files` | Not retrieved as HTML. The files API above is the list that was retrieved. |
| `https://boardgamegeek.com/boardgame/54138/imperial-2030/images` | Not retrieved as HTML. The images API above is the list that was retrieved. |
| `https://boardgamegeek.com/boardgame/54138/imperial-2030/videos` | Not retrieved as HTML. The videos API above is the list that was retrieved. |

Image pages 3 and 4 were not requested. Images 101–217 are omitted on purpose. The image order is the API default: no `sort` parameter was sent. `config.sorttypes` lists Hot and Recent, but the payload does not name which sort was applied.

## 1. Identity

Source object: `item` in the geekitems response. Labels below are the JSON field names.

- **name**: Imperial 2030
- **primaryname.name**: Imperial 2030 (nameid 147759, sortindex 1, primaryname flag 1)
- **alternatenames**:
  - nameid 628194: Империал 2030
  - nameid 197103: 大国崛起 2030 (大國崛起 2030)
- **yearpublished**: 2009
- **label**: Board Game
- **subtype**: boardgame
- **canonical_link**: https://boardgamegeek.com/boardgame/54138/imperial-2030
- **minplayers**: 2
- **maxplayers**: 6
- **minplaytime**: 120
- **maxplaytime**: 180
- **minage**: 12
- **short_description**: Use money to manipulate countries into warring with each other for your own profit.

No separate `playingtime` field was in the item keys returned.

**description** (HTML removed; `<strong>` and `<br />` are not kept):

> Imperial 2030 is a game on its own, based on the rules of Imperial.  The six powers (USA, Europe, Russia, China, India, and Brazil) develop their industrial basis and build up armies and fleets.  They fight over control of neutral land and sea areas in order to become the most powerful nation worldwide.
>
> In this game it is not the players who take turns, but the six powers, one after another.  The players are just internationally operating investors who act in the background.  By giving money to the six powers, which all have their own treasuries, the players influence the politics.  The biggest investor in each nation gains control of that nation's government and decides what the nation will do.  As control of a government can change with each new investment, players may control several governments at the same time.  As investors, players should not get too attached to their preferred nation, but rather focus on where their investments have the best rates of return.  Essentially the game is about money, and not about military domination!
>
> Imperial 2030 was released at Essen 2009 by PD-Games and Rio Grande Games. Compared to "Imperial" there will be some new features:
> - new wooden bits
> - the Swiss Bank
> - a new 30 million bond to invest in
> - more neutral territory, generating higher taxation
> - fewer home provinces
> - control of canals (Panama and Suez).
>
> For those who already owned Imperial, there was the opportunity to get only the new map and bonds at Essen '09, as it can be played with the old wooden bits as well.

**boardgamedesigner** (1):
- Mac Gerdts — objectid 6045 — href `/boardgamedesigner/6045/mac-gerdts`

**boardgameartist** (1):
- Alexander Jung — objectid 12123 — href `/boardgameartist/12123/alexander-jung`
- The same object also returned `canonical_link`: `https://boardgamegeek.com/boardgamedesigner/12123/alexander-jung`. That URL path says `boardgamedesigner`, which does not match `href`. Both values are copied as returned.

**boardgamepublisher** (8), in API order. `primarylink` is copied as returned:
- PD-Verlag — objectid 8401 — primarylink 1 — href `/boardgamepublisher/8401/pd-verlag`
- Cranio Creations — objectid 10768 — primarylink 0 — href `/boardgamepublisher/10768/cranio-creations`
- Egmont Polska — objectid 7496 — primarylink 0 — href `/boardgamepublisher/7496/egmont-polska`
- The Game Master BV — objectid 2862 — primarylink 0 — href `/boardgamepublisher/2862/the-game-master-bv`
- Hobby World — objectid 18852 — primarylink 0 — href `/boardgamepublisher/18852/hobby-world`
- Pensamento Coletivo — objectid 27777 — primarylink 0 — href `/boardgamepublisher/27777/pensamento-coletivo`
- Rio Grande Games — objectid 3 — primarylink 0 — href `/boardgamepublisher/3/rio-grande-games`
- Wargames Club Publishing — objectid 8759 — primarylink 0 — href `/boardgamepublisher/8759/wargames-club-publishing`

These credit arrays on the same `links` object were empty (length 0): `boardgamesolodesigner`, `boardgamedeveloper`, `boardgamegraphicdesigner`, `boardgamesculptor`, `boardgameeditor`, `boardgamewriter`, `boardgameinsertdesigner`.

**website** (same item):
- url: http://RioGrandeGames.com/Game/346-Imperial-2030
- title: Imperial 2030 -- Homepage on the Rio Grande website.

**reimplements** (1):
- Imperial — objectid 24181 — href `/boardgame/24181/imperial`

**boardgameversion** (9), names only:
- Chinese edition — objectid 27437
- Dutch edition — objectid 35062
- English edition — objectid 29187
- English/German 'Upgrade' edition — objectid 48489
- English/German first edition — objectid 24731
- Italian edition — objectid 327565
- Polish edition — objectid 324449
- Portuguese edition — objectid 376506
- Russian edition — objectid 173649

**boardgamehonor** (3):
- 2009 Meeples Choice Award Nominee — objectid 107435
- 2011 Gouden Ludo Nominee — objectid 21199
- 2011 Nederlandse Spellenprijs Nominee — objectid 13119

**boardgameaccessory** (1):
- Imperial 2030: InMyBox Organizer — objectid 462450 — href `/boardgameaccessory/462450/imperial-2030-inmybox-organizer`

**cardset** (1): `name` and `sortindex` were JSON null. objectid 106284, objecttype family, href `/cardset/106284/`. No card-set title was in the payload.

## 2. Files

Count: **28** file records in the response. `config.numitems` = 28. `config.endpage` = 1. Page count: 1. `showcount=100` was requested and the single page contained every listed file.

`config.languages` returned with the file list:
- languageid 2183: Dutch
- languageid 2184: English
- languageid 2186: Finnish
- languageid 2187: French
- languageid 2189: Greek
- languageid 2191: Hungarian
- languageid 2193: Italian
- languageid 2199: Polish
- languageid 2200: Portuguese
- languageid 2202: Russian
- languageid 2203: Spanish
- languageid 2709: Thai

### 1. Règles du jeu Imperial 2030 (format A4, DocGuillaume)

- **filepageid**: 320460
- **fileid**: 448078
- **filename**: Imperial 2030 (A4 DocGuillaume).pdf
- **file page URL**: https://boardgamegeek.com/filepage/320460/regles-du-jeu-imperial-2030-format-a4-docguillaume
- **language**: French (languageid 2187)
- **postdate**: 2026-04-13 03:11:40
- **classification**: rules document
- **why that class**: Title is "Règles du jeu" (rules of the game). Description says it is a new French translation, with spelling fixes, style changes, and added clarifications and omissions relative to the English rules.
- **description**:

> >Nouvelle traduction française
> - correction des fautes d'orthographe
> - amélioration du style
> - ajout de précisions et des omissions par rapport aux règles en anglais
> 
> >Nouvelle mise en page :
> - format A4
> - illustrations des exemples avec le matériel du jeu
> 
> Vos suggestion d'améliorations et de corrections sont les bienvenues!

### 2. Imperial 2030 Scoring Sheet

- **filepageid**: 262361
- **fileid**: 363651
- **filename**: Imperial 2030 scoring sheet.pdf
- **file page URL**: https://boardgamegeek.com/filepage/262361/imperial-2030-scoring-sheet
- **language**: English (languageid 2184)
- **postdate**: 2023-07-24 06:12:39
- **classification**: scoring sheet
- **why that class**: Title is "Imperial 2030 Scoring Sheet". Description says it is the scoring sheet the poster's group uses.
- **description**:

> This is the Imperial 2030 scoring sheet that my group uses to play the game.
> 
> This scoring sheet includes all the options that are included in the manual.  We always play the advanced rules.  In our games, we don't use the Investor Card but this option is on the scoring sheet. We use the Imperial 2030 bonus rules but you can select the Imperial bonus rules as an option.  The final published game option is a Russia start or a USA start.  This can be selected by the tick box on the left of the table.
> 
> We always have the last winner to be the next start player.  We have an option to select randomized seating.  We have recently added a 90 second timer for each move to speed up the game. The numbers in brackets are the starting funds depending on the player count.  Depending on who is playing, we may implement a few 'Regret' tokens which allow you to reverse your move before the next player, otherwise once you complete your move it's set in stone.
> 
> Sometimes we try to estimate which player was the best investor in the game and we may rank the expected finish spot before the final scoring.  This scoring sheet includes space to mark this.
> 
> I hope you find this useful.  We have printed this double sided and made a running diary of our games which number close to 100 games.

### 3. Imperial 2030

- **filepageid**: 244121
- **fileid**: 335977
- **filename**: Imperial 2030_[HUN].pdf
- **file page URL**: https://boardgamegeek.com/filepage/244121/imperial-2030
- **language**: Hungarian (languageid 2191)
- **postdate**: 2022-07-27 10:28:15
- **classification**: rules document
- **why that class**: Description says it is a corrected Hungarian-language rulebook ("szabálykönyv").
- **description**:

> A magyar nyelvű szabálykönyv javítva. A ketaklub.hu-ról letöltött file 2 oldala üres volt, azokat újraszerkesztettem, és az egészet kijavítottam.
> 
> Köszönet az eredeti fordítójának!

### 4. Imperial 2030 riassunto regolamento

- **filepageid**: 236294
- **fileid**: 324350
- **filename**: Imperial 2030 riassunto.pdf
- **file page URL**: https://boardgamegeek.com/filepage/236294/imperial-2030-riassunto-regolamento
- **language**: Italian (languageid 2193)
- **postdate**: 2022-02-21 13:02:14
- **classification**: rules document
- **why that class**: Title is "Imperial 2030 riassunto regolamento". Description says it is a textual summary of the rules ("Riassunto testuale del regolamento").
- **description**:

> Riassunto testuale del regolamento di "Imperial 2030".
> Vi prego di segnalarmi eventuali errori, verranno corretti al più presto.

### 5. Finnish player aid for Imperial 2030

- **filepageid**: 220206
- **fileid**: 299443
- **filename**: Imperial_2030_PlayerAid_FI_v1.pdf
- **file page URL**: https://boardgamegeek.com/filepage/220206/finnish-player-aid-for-imperial-2030
- **language**: Finnish (languageid 2186)
- **postdate**: 2021-04-02 18:05:30
- **classification**: player aid
- **why that class**: Title and description both call it a player aid (Finnish translation of the Imperial 2030 player aid / pikaohje).
- **description**:

> This is a finnish translation of the Imperial 2030 player aid
> 
> In finnish: suomenkielinen käännös imperial 2030 -pelin pikaohjeesta

### 6. Imperial 2030

- **filepageid**: 201008
- **fileid**: 269241
- **filename**: Imperial_2030_Rules(GR).pdf
- **file page URL**: https://boardgamegeek.com/filepage/201008/imperial-2030
- **language**: Greek (languageid 2189)
- **postdate**: 2020-05-08 01:29:30
- **classification**: rules document
- **why that class**: Description says "Greek Rules in pdf format".
- **description**:

> Greek Rules in pdf format

### 7. Imperial 2030 - rules in brief

- **filepageid**: 197755
- **fileid**: 264057
- **filename**: Imperial 2030 - rules in brief v1.pdf
- **file page URL**: https://boardgamegeek.com/filepage/197755/imperial-2030-rules-in-brief
- **language**: English (languageid 2184)
- **postdate**: 2020-03-19 20:05:43
- **classification**: rules document
- **why that class**: Title is "rules in brief". Description says these are 1–2 page rules summaries and "not a complete rulebook replacement".
- **description**:

> Rules in Brief are 1-2 page summaries meant to be a quick rules refresher - not a complete rulebook replacement. Pages are sized to be printed, trimmed, laminated, and fit in the box.  If you see any errors or find things to be unclear, I would appreciate feedback.  Thanks!

### 8. Imperial 2030 GameAid (Thai)

- **filepageid**: 134244
- **fileid**: 169192
- **filename**: Imperial2030.jpg
- **file page URL**: https://boardgamegeek.com/filepage/134244/imperial-2030-gameaid-thai
- **language**: Thai (languageid 2709)
- **postdate**: 2016-07-07 21:25:14
- **classification**: player aid
- **why that class**: Title is "Imperial 2030 GameAid (Thai)". Description begins "GameAid".
- **description**:

> GameAid ภาษาไทย เกม Imperial 2030
> วิธี Setup Turn การเล่น
> สามารถพิมพ์ด้วย CANNON SELPHY CP910 แบบ borderless ได้พอดี
> คิดว่าสามารถอัดตามร้านอัดภาพทั่วไปได้ ขนาด 4*6" ได้เช่นกัน

### 9. A quick guide to odd rules of Imperial 2030

- **filepageid**: 133712
- **fileid**: 168425
- **filename**: Imperial-2030.pdf
- **file page URL**: https://boardgamegeek.com/filepage/133712/a-quick-guide-to-odd-rules-of-imperial-2030
- **language**: English (languageid 2184)
- **postdate**: 2016-06-24 12:12:06
- **classification**: rules document
- **why that class**: Title is "A quick guide to odd rules". Description says it is "a page and a half of rules".
- **description**:

> If you're an experienced gamer - Risk, Diplomacy, 18xx and/or the Euro Roundel-Econ games - here's a page and a half of rules.  Read them, sit down at the Imperial 2030 board, play with confidence.

### 10. Imperial 2030 Thai Rule

- **filepageid**: 133630
- **fileid**: 168315
- **filename**: Imperial2030_Rules.pdf
- **file page URL**: https://boardgamegeek.com/filepage/133630/imperial-2030-thai-rule
- **language**: Thai (languageid 2709)
- **postdate**: 2016-06-22 04:18:35
- **classification**: rules document
- **why that class**: Title is "Imperial 2030 Thai Rule". Description begins "Translate and simplify rule".
- **description**:

> Translate and simplify rule
> กฎภาษาไทย แปลและมีการปรับแต่งกฎรูปแบบการจัดส่วนต่างๆของกฎเพื่อให้เข้าใจง่ายขึ้น
> แต่โดยรวมกติกาไม่เปลี่ยนแปลง

### 11. Printer friendly automated score sheet

- **filepageid**: 97688
- **fileid**: 114344
- **filename**: Score Imperial 2030.xlsx
- **file page URL**: https://boardgamegeek.com/filepage/97688/printer-friendly-automated-score-sheet
- **language**: English (languageid 2184)
- **postdate**: 2013-12-06 10:25:11
- **classification**: scoring sheet
- **why that class**: Title is "Printer friendly automated score sheet". Description says to fill in nations' Power Points and players' Interests + cash.
- **description**:

> Just fill in the nations' Power Points and players' Interests + cash.

### 12. Империал 2030 (Игровед)

- **filepageid**: 94859
- **fileid**: 110301
- **filename**: Правила настольной игры Империал 2030 (Imperial 2030).pdf
- **file page URL**: https://boardgamegeek.com/filepage/94859/imperial-2030-igroved
- **language**: Russian (languageid 2202)
- **postdate**: 2013-09-22 08:33:24
- **classification**: rules document
- **why that class**: Description is "Правила игры" (rules of the game). Title is the game name plus "(Игровед)".
- **description**:

> Правила игры

### 13. Imperial 2030 player aid em português do Brasil

- **filepageid**: 94530
- **fileid**: 127531
- **filename**: Imperial 2030 Trad v1.1.pdf
- **file page URL**: https://boardgamegeek.com/filepage/94530/imperial-2030-player-aid-em-portugues-do-brasil
- **language**: Portuguese (languageid 2200)
- **postdate**: 2013-09-13 11:46:11
- **classification**: player aid
- **why that class**: Title says "player aid em português do Brasil". Description only says "Correção de erros." The player-aid classification is from the title.
- **description**:

> Correção de erros.

### 14. Imperial 2030 - Aide de jeu

- **filepageid**: 92797
- **fileid**: 143083
- **filename**: Imperial 2030 - Aide de jeu - v1.1.pdf
- **file page URL**: https://boardgamegeek.com/filepage/92797/imperial-2030-aide-de-jeu
- **language**: French (languageid 2187)
- **postdate**: 2013-07-18 16:28:42
- **classification**: player aid
- **why that class**: Title is "Aide de jeu". Description says "Aide de jeu / résumé des règles".
- **description**:

> Aide de jeu / résumé des règles pour Imperial 2030.

### 15. Imperial2030_HojasPuntuación

- **filepageid**: 87819
- **fileid**: 100517
- **filename**: Imperial2030_HojaPuntuacion_ES.docx
- **file page URL**: https://boardgamegeek.com/filepage/87819/imperial2030-hojaspuntuacion
- **language**: Spanish (languageid 2203)
- **postdate**: 2013-02-20 14:37:01
- **classification**: scoring sheet
- **why that class**: Description says it is a score sheet ("hoja de puntuación").
- **description**:

> Se trata de una hoja de puntuación simple pero eficaz. Imprimir en papel tamaño A4 para conseguir ocho hojas de puntuación por cada impresión.

### 16. Imperial2030_ScoreSheet

- **filepageid**: 87818
- **fileid**: 100516
- **filename**: Imperial2030_ScoreSheet_EN.docx
- **file page URL**: https://boardgamegeek.com/filepage/87818/imperial2030-scoresheet
- **language**: English (languageid 2184)
- **postdate**: 2013-02-20 14:30:53
- **classification**: scoring sheet
- **why that class**: Title is "Imperial2030_ScoreSheet". Description says "This is a simple but effective score sheet."
- **description**:

> This is a simple but effective score sheet. Print this file on A4 size to get eight score sheets per printing.

### 17. Scoreblad

- **filepageid**: 85285
- **fileid**: 97197
- **filename**: Scoresheet.pdf
- **file page URL**: https://boardgamegeek.com/filepage/85285/scoreblad
- **language**: Dutch (languageid 2183)
- **postdate**: 2012-12-07 09:36:59
- **classification**: scoring sheet
- **why that class**: Title is "Scoreblad". Description says "Dutch Score Sheet".
- **description**:

> Dutch Score Sheet, based on Tiago Duarte's
> http://boardgamegeek.com/filepage/53841/imperial-2030-integr...
>
> The visible link text above is truncated in the API HTML. The anchor `href` on that same link is `http://boardgamegeek.com/filepage/53841/imperial-2030-integrated-scoresheet`.
>
> Hint: I laminated it, so I can reuse it every time with a non-permanent marker.

### 18. Samenvattingskaart

- **filepageid**: 82500
- **fileid**: 93834
- **filename**: Imperial 2030.pdf
- **file page URL**: https://boardgamegeek.com/filepage/82500/samenvattingskaart
- **language**: Dutch (languageid 2183)
- **postdate**: 2012-09-17 12:47:36
- **classification**: unspecified
- **why that class**: Title is "Samenvattingskaart" and the description calls it a summary card used so players need not keep reaching for the rules. It does not say rules document, player aid, or scoring sheet.
- **description**:

> Als het een lange tijd geleden is, kan deze samenvattingskaart je helpen bij het spelen van Imperial 2030. Zo moet je niet hele tijd grijpen naar de spelregels!

### 19. Imperial 2030 Tuckboxes

- **filepageid**: 81362
- **fileid**: 92379
- **filename**: Imp 2030 Tuckboxes.rar
- **file page URL**: https://boardgamegeek.com/filepage/81362/imperial-2030-tuckboxes
- **language**: English (languageid 2184)
- **postdate**: 2012-08-12 18:00:40
- **classification**: other
- **why that class**: Title is "Imperial 2030 Tuckboxes". Description says "Tuckboxes for Bonds, Money, & Flags."
- **description**:

> Tuckboxes for Bonds, Money, & Flags.

### 20. Imperial 2030 Reglas, Ayuda y Rondel en Español

- **filepageid**: 75691
- **fileid**: 349597
- **filename**: Imperial 2030 Rondel ES v1.pdf
- **file page URL**: https://boardgamegeek.com/filepage/75691/imperial-2030-reglas-ayuda-y-rondel-en-espanol
- **language**: Spanish (languageid 2203)
- **postdate**: 2012-02-02 05:29:27
- **classification**: rules document and player aid
- **why that class**: Title is "Imperial 2030 Reglas, Ayuda y Rondel en Español" (rules, aid, and rondel). Description only describes the Spanish rondel and a permission line.
- **description**:

> Rondel de Imperial 2030 en Español, de España, Versión 1.
> Subido con permiso de Mac Gerdts.

### 21. Карточка с описанием ронделя на русском

- **filepageid**: 74107
- **fileid**: 82920
- **filename**: imperial 2030 rondel rus.jpg
- **file page URL**: https://boardgamegeek.com/filepage/74107/kartocka-s-opisaniem-rondelia-na-russkom
- **language**: Russian (languageid 2202)
- **postdate**: 2011-12-23 01:07:05
- **classification**: unspecified
- **why that class**: Title and description call it a card describing rondel actions in Russian. They do not say rules document, player aid, or scoring sheet.
- **description**:

> Карточка с описанием действий ронделя на русском языке

### 22. Imperial 2030 player aid in Italian

- **filepageid**: 70828
- **fileid**: 78939
- **filename**: Imperial 2030 player aid.pdf
- **file page URL**: https://boardgamegeek.com/filepage/70828/imperial-2030-player-aid-in-italian
- **language**: Italian (languageid 2193)
- **postdate**: 2011-09-23 17:40:56
- **classification**: player aid
- **why that class**: Title and description both say "player aid" (Italian, based on the original layout).
- **description**:

> Imperial 2030 player aid in Italian (based on the original layout)

### 23. Rróżnice w stosunku do Imperiala

- **filepageid**: 58757
- **fileid**: 63818
- **filename**: Imperial 2030 Przegląd.pdf
- **file page URL**: https://boardgamegeek.com/filepage/58757/rroznice-w-stosunku-do-imperiala
- **language**: Polish (languageid 2199)
- **postdate**: 2010-09-06 15:08:30
- **classification**: other
- **why that class**: Title is about differences relative to Imperial. Description says "Przegląd różnic w stosunku do Imperiala" and "Differences in comparison to “Imperial“".
- **description**:

> Przegląd różnic w stosunku do Imperiala
> Differences in comparison to “Imperial“

### 24. Imperial 2030 Setup and Turn Order Player Aid

- **filepageid**: 53936
- **fileid**: 57888
- **filename**: Imperial2030_PlayerAid_Version1.0.xls
- **file page URL**: https://boardgamegeek.com/filepage/53936/imperial-2030-setup-and-turn-order-player-aid
- **language**: English (languageid 2184)
- **postdate**: 2010-03-14 20:53:52
- **classification**: player aid
- **why that class**: Title says "Player Aid". Description says it is a one-sheet summary of setup steps and turn order.
- **description**:

> This is a one-sheet document summarizing setup steps and turn order rules. Designed as a quick "refresher" for someone teaching the game or needing some assistance in game flow.

### 25. Imperial 2030 - Integrated Scoresheet

- **filepageid**: 53841
- **fileid**: 88971
- **filename**: Imperial_2030_-_Integrated_Scoresheet v1.1.pdf
- **file page URL**: https://boardgamegeek.com/filepage/53841/imperial-2030-integrated-scoresheet
- **language**: English (languageid 2184)
- **postdate**: 2010-03-11 14:07:30
- **classification**: scoring sheet
- **why that class**: Title is "Imperial 2030 - Integrated Scoresheet".
- **description**:

> Update order of flags of China and India. They are now in order.

### 26. Imperial 2030 result sheet

- **filepageid**: 51497
- **fileid**: 54958
- **filename**: imperial_2030_result_sheet.pdf
- **file page URL**: https://boardgamegeek.com/filepage/51497/imperial-2030-result-sheet
- **language**: English (languageid 2184)
- **postdate**: 2010-01-16 10:20:37
- **classification**: scoring sheet
- **why that class**: Title is "Imperial 2030 result sheet". Description says "A Result Sheet to sum up all points."
- **description**:

> A Result Sheet to sum up all points.

### 27. Imperial 2030 English Rules.pdf

- **filepageid**: 47882
- **fileid**: 50631
- **filename**: Imperial 2030 English Rules.pdf
- **file page URL**: https://boardgamegeek.com/filepage/47882/imperial-2030-english-rulespdf
- **language**: English (languageid 2184)
- **postdate**: 2009-10-08 04:30:28
- **classification**: rules document
- **why that class**: Title is "Imperial 2030 English Rules.pdf". Description repeats that filename and does not add other wording.
- **description**:

> Imperial 2030 English Rules.pdf

### 28. Imperial 2030 Quick Intro.pdf

- **filepageid**: 47881
- **fileid**: 50630
- **filename**: Imperial 2030 Quick Intro.pdf
- **file page URL**: https://boardgamegeek.com/filepage/47881/imperial-2030-quick-intropdf
- **language**: English (languageid 2184)
- **postdate**: 2009-10-08 04:29:56
- **classification**: unspecified
- **why that class**: Title and description are only "Imperial 2030 Quick Intro.pdf". They do not say rules document, player aid, or scoring sheet.
- **description**:

> Imperial 2030 Quick Intro.pdf

## 3. Images

Total count from `pagination.total`: **217**.
Listed below: **100** (the first 60 from page 1 plus the first 40 from page 2). Images 101–217 were not listed. No image binaries were downloaded.

Each row uses `imageid`, `caption` (blank if the field was empty), the image page built from `href`, and `imageurl_lg`. Individual image objects did not include a gallery, category, or license field. The config block did list gallery names (All, Game, People, Creative), category names (Box Front, Box Back, Components, Customized, Play, Miscellaneous, Uncategorized), and license filter names (Any, Copying allowed, Commercial use allowed, Modification allowed), but those filters were not attached to each image in the payload.

| # | imageid | caption | image page | imageurl_lg |
| --- | --- | --- | --- | --- |
| 1 | 9547651 | Game | https://boardgamegeek.com/image/9547651/imperial-2030 | https://cf.geekdo-images.com/hrBF9ChA-0wYPEJMz9N_ug__large/img/aGxRX_XLLbdXdVLnCW6pLtSM_5k=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic9547651.jpg |
| 2 | 9468503 | End of first play. Final score 230 to 215. This was an absolute blast! | https://boardgamegeek.com/image/9468503/imperial-2030 | https://cf.geekdo-images.com/0XTkzljOc5u8ZQhGQwxSSQ__large/img/-5dPJD81ctO0-qo0psjgdVwKISM=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic9468503.jpg |
| 3 | 9304151 | This game is not bad even at 3p. | https://boardgamegeek.com/image/9304151/imperial-2030 | https://cf.geekdo-images.com/q3wu3q6Wlw-t98BhC4UslA__large/img/rMY21A-QzVs7a215PMTwwp47vKw=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic9304151.jpg |
| 4 | 7730812 | My perspective on the board… | https://boardgamegeek.com/image/7730812/imperial-2030 | https://cf.geekdo-images.com/qzoqB5LQ6HPsIFRcyILkuA__large/img/M4a8lBh3rFHJL8H0X5qOqPJvT7c=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic7730812.jpg |
| 5 | 7701463 | 3D Printed Organiser | https://boardgamegeek.com/image/7701463/imperial-2030 | https://cf.geekdo-images.com/QfZ2KCzoFeGZl-XL4Z4HCA__large/img/tnms5vQLR75nL82K4WIraCT9kiA=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic7701463.jpg |
| 6 | 7678475 | Game in progress | https://boardgamegeek.com/image/7678475/imperial-2030 | https://cf.geekdo-images.com/lidacA59guuGPYZnjXg4-A__large/img/ROgeGKB3RyUyE_kVEr74SKauCDA=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic7678475.jpg |
| 7 | 7678473 | Game in progress | https://boardgamegeek.com/image/7678473/imperial-2030 | https://cf.geekdo-images.com/iOFax2PMF9wLvudkiEspKA__large/img/oc1_5nPhlAyfmpBHVEcCDAoVwlA=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic7678473.jpg |
| 8 | 7524695 | Mid game | https://boardgamegeek.com/image/7524695/imperial-2030 | https://cf.geekdo-images.com/mmHxg5aZmWBDjSzc_2roRg__large/img/zPR4Tdx8F6y8p9Ob10_6vzXZQds=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic7524695.jpg |
| 9 | 6926871 | Imperial 2030 | https://boardgamegeek.com/image/6926871/imperial-2030 | https://cf.geekdo-images.com/jjDzqXU4jxXXlQtzKCkoGw__large/img/qOhvnYPMidir4_1k9H_EpnAk8j4=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic6926871.jpg |
| 10 | 5637373 | Imperial 2030 Империал настольная игра Полтава Игрократия Клуб настольных игр | https://boardgamegeek.com/image/5637373/imperial-2030 | https://cf.geekdo-images.com/gdkY3F4QgSc83fEpRHuOpA__large/img/mhTe_cXoDu0D1KPxT44I8UElh1A=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic5637373.jpg |
| 11 | 5637370 | Imperial 2030 Империал настольная игра Полтава Игрократия | https://boardgamegeek.com/image/5637370/imperial-2030 | https://cf.geekdo-images.com/aATslWLT8b36xQ1kBGpAug__large/img/8th5LLfUw0cQGEClGPSHMJYDqF4=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic5637370.jpg |
| 12 | 5637369 | Imperial 2030 Империал настольная игра Полтава Игрократия | https://boardgamegeek.com/image/5637369/imperial-2030 | https://cf.geekdo-images.com/8Tj6b0OOIuUrFFQsv9SBEQ__large/img/pWCQLWOLxQ1iJg53zes5uBiEjyE=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic5637369.jpg |
| 13 | 5637368 | Imperial 2030 Империал настольная игра Полтава Игрократия | https://boardgamegeek.com/image/5637368/imperial-2030 | https://cf.geekdo-images.com/2HOmomHXDwgCWPpP-XSunw__large/img/fN7iZsIghiS2--AZbk1aLPsPWOE=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic5637368.jpg |
| 14 | 5637367 | Imperial 2030 Империал настольная игра Полтава Игрократия | https://boardgamegeek.com/image/5637367/imperial-2030 | https://cf.geekdo-images.com/We0lAxDu4dxOwGk_tzvg1Q__large/img/h-mdKeobIjmZGTmNZp1fXhufRbY=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic5637367.jpg |
| 15 | 5637366 | Imperial 2030 Империал настольная игра Полтава Игрократия | https://boardgamegeek.com/image/5637366/imperial-2030 | https://cf.geekdo-images.com/05np9Ya0ay3tVhl-62wURw__large/img/bug77Lt0iJe4tM-ljyy-VB3bOyY=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic5637366.jpg |
| 16 | 5637365 | Imperial 2030 Империал настольная игра Полтава Игрократия | https://boardgamegeek.com/image/5637365/imperial-2030 | https://cf.geekdo-images.com/VzkpwNH6HjLk1VUsh5znMg__large/img/LwxmjaeU2SCM16vet2En92p43m0=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic5637365.jpg |
| 17 | 5637364 | Imperial 2030 Империал настольная игра Полтава Игрократия | https://boardgamegeek.com/image/5637364/imperial-2030 | https://cf.geekdo-images.com/xoFT6KuXhttVlAR_Fo0JTw__large/img/sekymjV45hjxaci34EfKYKgk3L4=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic5637364.jpg |
| 18 | 5637363 | Imperial 2030 Империал настольная игра Полтава Игрократия | https://boardgamegeek.com/image/5637363/imperial-2030 | https://cf.geekdo-images.com/NTy9JaGdtRLee4Ytj2xCrw__large/img/Woonfmd60epuD21R6gAv8LgiA-Q=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic5637363.jpg |
| 19 | 5637362 | Imperial 2030 Империал настольная игра Полтава Игрократия | https://boardgamegeek.com/image/5637362/imperial-2030 | https://cf.geekdo-images.com/sUw0Tv2HIm0JGBlfka1DAw__large/img/8rR-nHsi2K37lnJQwkKUp_rM_MQ=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic5637362.jpg |
| 20 | 5637361 | Imperial 2030 Империал настольная игра Полтава Игрократия | https://boardgamegeek.com/image/5637361/imperial-2030 | https://cf.geekdo-images.com/_JKtRqez2bxQiWfVe1Vl_Q__large/img/cwGEzwatNzp-IUNXLljg2ABPMrM=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic5637361.jpg |
| 21 | 5316288 | Planning my strategy from the North Pole :D | https://boardgamegeek.com/image/5316288/imperial-2030 | https://cf.geekdo-images.com/F2Xi4cYfvlHesuqgiMZ5Dw__large/img/VfZHdawxa92XC-aPsS55tva_AVU=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic5316288.jpg |
| 22 | 4780094 | Boxed Trays | https://boardgamegeek.com/image/4780094/imperial-2030 | https://cf.geekdo-images.com/X1Rc_6rl2-r_Nba3aWmXmA__large/img/VqEaIxkxkaLfi9mDR-aU2ze5WKA=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic4780094.jpg |
| 23 | 4780093 | Money Tray | https://boardgamegeek.com/image/4780093/imperial-2030 | https://cf.geekdo-images.com/bdYLuiw439qJGXcAOcvacg__large/img/pFmp34rsm3ZkXD_d5ns0stPwt64=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic4780093.jpg |
| 24 | 4780092 | Country Tray I | https://boardgamegeek.com/image/4780092/imperial-2030 | https://cf.geekdo-images.com/7ODcplpYbKc7IAhP3w8klA__large/img/yuw54nybRjhQsv0x3-iyJ44OfOE=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic4780092.jpg |
| 25 | 4780091 | Country Tray | https://boardgamegeek.com/image/4780091/imperial-2030 | https://cf.geekdo-images.com/tawW-2lXhCkKRKp2qzkAFg__large/img/0ORN6Xivb2ebZkwErCFue2CjYYU=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic4780091.jpg |
| 26 | 4675232 | Six superpowers fighting a well-balanced battle of economy. | https://boardgamegeek.com/image/4675232/imperial-2030 | https://cf.geekdo-images.com/BuNrnOWzf2mpwOXR-P2b8A__large/img/ud2i0KfO9n1ycnnR8xVjbvo8PjE=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic4675232.jpg |
| 27 | 4472650 | Italian edition - Box front | https://boardgamegeek.com/image/4472650/imperial-2030 | https://cf.geekdo-images.com/Mc72vit-jyNdRotIWTC5Yw__large/img/s8dilqIwKOfy1_NvulxG5uITO8Q=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic4472650.jpg |
| 28 | 4171934 | Imperial 2018 | https://boardgamegeek.com/image/4171934/imperial-2030 | https://cf.geekdo-images.com/59IQyqrJIm19wZxPjX-Kww__large/img/dWRo1YQvMz6uJlni_uu9jCFswFY=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic4171934.jpg |
| 29 | 4111508 | Endgame situation | https://boardgamegeek.com/image/4111508/imperial-2030 | https://cf.geekdo-images.com/cLuZAF07b486zXkGw4IijQ__large/img/mtM-mZfQdRUrrfc8fTq_y5URaRI=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic4111508.jpg |
| 30 | 4021682 | Sun setting in the West | https://boardgamegeek.com/image/4021682/imperial-2030 | https://cf.geekdo-images.com/sDahDnuH7VAd7CenbPKRKw__large/img/h0H1wL784ARXX51HrUWl4XfjpNo=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic4021682.jpg |
| 31 | 3959270 | Match during gobcon 2018 | https://boardgamegeek.com/image/3959270/imperial-2030 | https://cf.geekdo-images.com/WbGpiXqWf_R19eIm9GqKIA__large/img/8XNPnLADxeF2zEZGNy15t918BR4=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic3959270.jpg |
| 32 | 3957592 | Close Up of a game | https://boardgamegeek.com/image/3957592/imperial-2030 | https://cf.geekdo-images.com/YZMEcc9cpV9IYXZXKymcTg__large/img/tqR3G5wrflqutVUmg07QyKsM58Q=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic3957592.jpg |
| 33 | 3912816 | Box art Imperial 2030 | https://boardgamegeek.com/image/3912816/imperial-2030 | https://cf.geekdo-images.com/QeTKW9zmJphhjrKGoDtS9w__large/img/ygezMF_V1MRTw5euUaAquwTwE5w=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic3912816.jpg |
| 34 | 3836029 | Unboxing on Picture - Brazilian Version | https://boardgamegeek.com/image/3836029/imperial-2030 | https://cf.geekdo-images.com/FtiD6KGSwkKnRWCTwTk5YQ__large/img/rwrZiZ0pIIPCKFG9p-Lg9i3oCQk=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic3836029.png |
| 35 | 3831665 | Brazilian first edition by Pensamento Coletivo | https://boardgamegeek.com/image/3831665/imperial-2030 | https://cf.geekdo-images.com/XQAfMJBSpr_yohyxIagCBA__large/img/XF71_hGEhamxHo---8AXbN8dsiY=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic3831665.png |
| 36 | 3714032 | Flags being used instead of vanilla cards | https://boardgamegeek.com/image/3714032/imperial-2030 | https://cf.geekdo-images.com/14jsbJ9Mh-ifDsNDI8vALA__large/img/3oi4V-Cur1jwCvJdDy6g-y9F6v8=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic3714032.jpg |
| 37 | 3593128 | Common rookie mistake. | https://boardgamegeek.com/image/3593128/imperial-2030 | https://cf.geekdo-images.com/j3nDXgzQO69MSsEl4Z1vTw__large/img/Ktp8Sr6kra0ryRt1B6Tj07V-EDM=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic3593128.jpg |
| 38 | 3451282 | Nynaeve, Mod XXII, Alberto, Indianino & Fedellow playing Imperial 2030 @ GobConDeluxe17 (Bologna - Italy) | https://boardgamegeek.com/image/3451282/imperial-2030 | https://cf.geekdo-images.com/5V5fZEfSHumpa-FcfW1hnw__large/img/5AauOx-BDFfPIrGLYrBHeQHx5Z4=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic3451282.jpg |
| 39 | 3451281 | Imperial + kit = Imperial 2030 | https://boardgamegeek.com/image/3451281/imperial-2030 | https://cf.geekdo-images.com/66B4EbWbtT2S0j5M1Iuyqw__large/img/jWnPhR3DK73Es4bMfX6Dm0md49A=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic3451281.jpg |
| 40 | 3447950 | USA wins, China on it's heels. | https://boardgamegeek.com/image/3447950/imperial-2030 | https://cf.geekdo-images.com/yJzfVG0eHKPhyaQJYckx8w__large/img/qNwyIu82tuXpkKOjZd0TtSY_CMY=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic3447950.jpg |
| 41 | 3446503 | 1st game for myself & 2 friends | https://boardgamegeek.com/image/3446503/imperial-2030 | https://cf.geekdo-images.com/u_hPHoHmHU-EyOet9F0a8A__large/img/XwbvT4Euw1kgwd459C3nIldoryM=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic3446503.jpg |
| 42 | 3424010 | First play - 3 players | https://boardgamegeek.com/image/3424010/imperial-2030 | https://cf.geekdo-images.com/-_IHBWqOC2GBmc5EguX3ew__large/img/ObjizHw5sAR_epNi5BID1vwfK0U=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic3424010.jpg |
| 43 | 3160647 | Imperial 2030, Egmont Polska, 2016 — box (image provided by the publisher) | https://boardgamegeek.com/image/3160647/imperial-2030 | https://cf.geekdo-images.com/Kw0f9jk6hdYwnCm6UfnCog__large/img/iJWAE5YIw5AHPYqCMXeYEhg3_WI=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic3160647.jpg |
| 44 | 3126558 | Russia Triggering End Game for 6p | https://boardgamegeek.com/image/3126558/imperial-2030 | https://cf.geekdo-images.com/Rxl82DwdlMjTxRFtp6sLhw__large/img/K_ZC_qnFCCJcxVOkwLKWpIoleSw=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic3126558.jpg |
| 45 | 3126557 | Start of Game for 6p | https://boardgamegeek.com/image/3126557/imperial-2030 | https://cf.geekdo-images.com/7jFL89M5AArPmcPO87hGIw__large/img/yzw2m42AkQpNGAby5KGoeUagSew=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic3126557.jpg |
| 46 | 2836821 | The Illuminati that dominates the world in 2030A.D. . | https://boardgamegeek.com/image/2836821/imperial-2030 | https://cf.geekdo-images.com/tnNQ6eAOxosZZEnPiGhVNQ__large/img/GiesZWJNEYG_9mj1vu7131UB6bc=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic2836821.jpg |
| 47 | 2814567 | At the start of the game after the first turns. | https://boardgamegeek.com/image/2814567/imperial-2030 | https://cf.geekdo-images.com/1hWaoRSlhaKsIgnpKIeynA__large/img/rKWbcOAyd_MMS8PkRXOZJEclksM=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic2814567.jpg |
| 48 | 2738971 | The brave Brazilian soldiers finally reached their surprise objective, many many miles from home. India is not pleased. | https://boardgamegeek.com/image/2738971/imperial-2030 | https://cf.geekdo-images.com/G1Azm0km1s_O3c0a4Cpa3A__large/img/Ag89bEvfI0KZCG0xvaqrM-jTMHs=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic2738971.jpg |
| 49 | 2595557 | 3 player game of Emperial 2030 | https://boardgamegeek.com/image/2595557/imperial-2030 | https://cf.geekdo-images.com/NvYl0GiyqUcVXMgVyirWGw__large/img/IPVPgjDmheJImRIQlJHZbtahh2s=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic2595557.jpg |
| 50 | 2534436 | Mid game play. We need to buy some bigger tables. Love a big map. | https://boardgamegeek.com/image/2534436/imperial-2030 | https://cf.geekdo-images.com/RloFrcm8N1KhSj6UHSGOKA__large/img/nckIDtC47SCIXqwuDre_sdLF2Qs=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic2534436.jpg |
| 51 | 2456691 | Things are not looking good for the ol' US of A.. | https://boardgamegeek.com/image/2456691/imperial-2030 | https://cf.geekdo-images.com/koPjO3BKW6-Y4oKSeTn2Tw__large/img/WKDh39dHx0nXp9JsRcXssWHndVs=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic2456691.jpg |
| 52 | 2320717 | Close Up from Imperial 2014 @ Spel in Anwerpen - Belgium | https://boardgamegeek.com/image/2320717/imperial-2030 | https://cf.geekdo-images.com/AVXZrpfrCv-oEEeiNYlAcA__large/img/EVD8BRwO4E94hEDkg0TD2zEfegE=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic2320717.jpg |
| 53 | 2320703 | Ruling from Brussels ... or Antwerpen @ Spel in Antwerpen - Belgium | https://boardgamegeek.com/image/2320703/imperial-2030 | https://cf.geekdo-images.com/Ftd0NTRZxGvVVezMuSQpdg__large/img/ZUiAyPZMz3Jx-rfA2ds8qSp83EM=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic2320703.jpg |
| 54 | 2083970 | Gainesville Gamer's All Day Game Thing. July 19th | https://boardgamegeek.com/image/2083970/imperial-2030 | https://cf.geekdo-images.com/6alLAHewTTdptRGsNb04sA__large/img/U8rcwYlQRFlPG1Nfro9Vq_qfSEw=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic2083970.jpg |
| 55 | 2078300 | Players after 300 minutes | https://boardgamegeek.com/image/2078300/imperial-2030 | https://cf.geekdo-images.com/RfFf7mgBjWnadraSTIFhQQ__large/img/WfPlVyjGCS_Cx9hreiTSqA4Ddkk=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic2078300.jpg |
| 56 | 2078299 | End Game | https://boardgamegeek.com/image/2078299/imperial-2030 | https://cf.geekdo-images.com/OTMwo694ijmWP5aVaSAwig__large/img/3-fEhsRfl_NvMkBYvigLEmXzUxw=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic2078299.jpg |
| 57 | 2078298 | A surprising future | https://boardgamegeek.com/image/2078298/imperial-2030 | https://cf.geekdo-images.com/JjN1z_AA37C1Tyrs6GPDAQ__large/img/ehIBHHDtObuLtt6wK3FkiCNGDIk=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic2078298.jpg |
| 58 | 1983948 | Imperial 2030 to its full glory, six players! Looking forward for the next Imperial session with that many players! | https://boardgamegeek.com/image/1983948/imperial-2030 | https://cf.geekdo-images.com/8Dhge3W7xadBrgEc8tJdiw__large/img/4dBK5jdI3cFQ773viNuaPmS7MX0=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1983948.jpg |
| 59 | 1979022 | Second game play of Imperial 2030! Now playing with 4 players! Looking forward to play it with six! This game is pure awesomeness! | https://boardgamegeek.com/image/1979022/imperial-2030 | https://cf.geekdo-images.com/beuPfjwdZpMyzFqzEQuDbA__large/img/B1B5XbYFOtR1jFdBCXKR8Gpvy0Y=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1979022.jpg |
| 60 | 1956917 | First Imperial 2030 session(3 players)! Awesome, Awesome game! I'm really glad I bought it. | https://boardgamegeek.com/image/1956917/imperial-2030 | https://cf.geekdo-images.com/kRGbElTK72rUPMU4RnEtLw__large/img/PFb6jzwRhHf1lFPmHyhi3NlKdhU=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1956917.jpg |
| 61 | 1685420 | Face of desperation. Greencop didn't see the sudden end of Russia. | https://boardgamegeek.com/image/1685420/imperial-2030 | https://cf.geekdo-images.com/9QeVD9y6TgZVwnh7t_-HRQ__large/img/bEelJoclH7NrQWraOkL_JNu2kUU=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1685420.jpg |
| 62 | 1685419 | End of the game. Russia finished with a quick move before the others take it! | https://boardgamegeek.com/image/1685419/imperial-2030 | https://cf.geekdo-images.com/fN0eI6fgXanzOkh_OgApNw__large/img/HSc_cNPdPqZpB0K-mlTiBvip0lE=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1685419.jpg |
| 63 | 1559125 | Playing @ LeiriaCon 2013 | https://boardgamegeek.com/image/1559125/imperial-2030 | https://cf.geekdo-images.com/BPFgVO2X64kaFyPYbH9O7Q__large/img/I1bkPvIMRO5pk_mT6Uzdv3qC5UA=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1559125.jpg |
| 64 | 1559124 | Playing @ LeiriaCon 2013 | https://boardgamegeek.com/image/1559124/imperial-2030 | https://cf.geekdo-images.com/SpK_tUw0XwWPEdmyk9jEkw__large/img/n8ot4g9qFUkNMQHO8yQ1PuN-IG4=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1559124.jpg |
| 65 | 1559120 | Playing @ LeiriaCon 2013 | https://boardgamegeek.com/image/1559120/imperial-2030 | https://cf.geekdo-images.com/-GOT5YoF_z5Qkbt0km3R7Q__large/img/hb_exZfexZw3NL5iOFkaSjU2kKU=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1559120.jpg |
| 66 | 1479127 | All the components that come with the game | https://boardgamegeek.com/image/1479127/imperial-2030 | https://cf.geekdo-images.com/EevBWEQGc0TNE8D0ByKu0g__large/img/g5ydInppuCeM2INK8-DYERQekt0=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1479127.jpg |
| 67 | 1451972 |  | https://boardgamegeek.com/image/1451972/imperial-2030 | https://cf.geekdo-images.com/OMPySlopb3iuSMZz0nmlbg__large/img/ON50cx5Vu9FRSGnrWgaNNYXqYMc=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1451972.jpg |
| 68 | 1374056 | Box of First Russian edition | https://boardgamegeek.com/image/1374056/imperial-2030 | https://cf.geekdo-images.com/rPBvpCGad0-_vOvj-enqOg__large/img/Ein18gznVwkMELYA2wTCfexjirk=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1374056.jpg |
| 69 | 1374054 | live long Switzerland | https://boardgamegeek.com/image/1374054/imperial-2030 | https://cf.geekdo-images.com/vg6zmD_unM56axYpTZEoNQ__large/img/fOYqqG9wyGFfYWCCDA_nT7p2bfU=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1374054.jpg |
| 70 | 1335885 | Early game in the East | https://boardgamegeek.com/image/1335885/imperial-2030 | https://cf.geekdo-images.com/lcQ_kh03Kh1oeCygK1gy7A__large/img/DbUtm7m5Gdu_DkvrmhMg9-GDi8E=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1335885.jpg |
| 71 | 1292734 | Russian version gameboard modules. | https://boardgamegeek.com/image/1292734/imperial-2030 | https://cf.geekdo-images.com/Oq-QyHKxm4vGWWwhyb30kg__large/img/kjOfVytyLz836ptnQuX0QY55Ink=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1292734.jpg |
| 72 | 1292733 | Russian version gameboard. | https://boardgamegeek.com/image/1292733/imperial-2030 | https://cf.geekdo-images.com/HALEsVRwdWFevLxoLn0G4g__large/img/eu2_xleE-9FhbvF2usOP4fMTnP4=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1292733.jpg |
| 73 | 1292731 | Russian version gameboard. | https://boardgamegeek.com/image/1292731/imperial-2030 | https://cf.geekdo-images.com/gmjJRIbDqTtRXeZnYE4eEQ__large/img/J06ypSqN79WbCuAHiOZgCP8SfW0=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1292731.jpg |
| 74 | 1267447 | Game of Imperial 2030 played at ConnCon 2012. I was leading Europe and had just crossed the pond to borrow Canada back from the Yanks. | https://boardgamegeek.com/image/1267447/imperial-2030 | https://cf.geekdo-images.com/FuykJOCxk47bCk9S0e2T9Q__large/img/Sk6b4SknbzpgW5dNjjmuYnJRpeM=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1267447.jpg |
| 75 | 1254016 | Imperial 2030 being played at the 2012-02-25 CABS meeting (www.buckeyeboardgamers.org) | https://boardgamegeek.com/image/1254016/imperial-2030 | https://cf.geekdo-images.com/Wccznho8cONbgE6UVLq9jQ__large/img/gXAPWVU7NpJq7YfMnd7WbkDAEbU=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1254016.jpg |
| 76 | 1185399 | Рондель на русском | https://boardgamegeek.com/image/1185399/imperial-2030 | https://cf.geekdo-images.com/84hz8_O_fWAd_b6KoN2QqQ__large/img/6os9eM_3LJXQ7WbKPx5sTrFmmlo=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1185399.jpg |
| 77 | 1162179 | Game Play @ Spel'11 in Broechem - Belgium | https://boardgamegeek.com/image/1162179/imperial-2030 | https://cf.geekdo-images.com/H4tzdCCZDAxyXp2UHnmffg__large/img/oV2Lw0BwgbQcBG2k5CjwvPcLSxQ=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1162179.jpg |
| 78 | 1129209 | Mid game. | https://boardgamegeek.com/image/1129209/imperial-2030 | https://cf.geekdo-images.com/ixVoDZOud-qEBLL_tBT6rw__large/img/FFfv0nD40hLqw7gG9xfyo2dIN4w=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1129209.jpg |
| 79 | 1073454 | End of round 3 in the first walk-through of Imperial-Orion variant. There has already been some conflict due to the close proximity of the regional powers. | https://boardgamegeek.com/image/1073454/imperial-2030 | https://cf.geekdo-images.com/g8Str0XPquvFAmzKv8YSzQ__large/img/R_COSYOVmARZiLaePtja0Ad51Bw=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1073454.jpg |
| 80 | 1073453 | Home made modular board for Imperial-Orion, a space opera variant. | https://boardgamegeek.com/image/1073453/imperial-2030 | https://cf.geekdo-images.com/0ifslV2no89uiUGCnxFWyw__large/img/RFIQ1G0cN--t_B4ZxO4MonYxyCg=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1073453.jpg |
| 81 | 1027168 | The Money of the World Economy | https://boardgamegeek.com/image/1027168/imperial-2030 | https://cf.geekdo-images.com/I0XESZhuC8Xeqma5r6temQ__large/img/aneVVLOzK3M5PO60p-YOWsTe0Gs=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1027168.jpg |
| 82 | 1027166 | A View from the Rondel | https://boardgamegeek.com/image/1027166/imperial-2030 | https://cf.geekdo-images.com/aE98EcyWHgGhsHRGeNnAbw__large/img/K21tDohNZi-jACf0TCzEBRGWY1w=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1027166.jpg |
| 83 | 1027162 | The Dutch Rule Book | https://boardgamegeek.com/image/1027162/imperial-2030 | https://cf.geekdo-images.com/rXNKw25xjFrbZ8N3Bv7q1w__large/img/w6MpnS2fB7VLP17HxniLFaX8AEc=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1027162.jpg |
| 84 | 1027161 | China Economy is Growing | https://boardgamegeek.com/image/1027161/imperial-2030 | https://cf.geekdo-images.com/ZWooyese89LOgnaJtGL2nw__large/img/2IH8Ymuwr9lCbSIn__L8HHjQPnQ=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1027161.jpg |
| 85 | 1027160 | Brazilian Economy | https://boardgamegeek.com/image/1027160/imperial-2030 | https://cf.geekdo-images.com/l1lawh7flzXclhrmEOj75A__large/img/4N6io7WXIFCb3H9w5NELKnXDDFA=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1027160.jpg |
| 86 | 1027154 | Overview | https://boardgamegeek.com/image/1027154/imperial-2030 | https://cf.geekdo-images.com/5ovZRM4ASIjK13Cyth6rSg__large/img/YX32UhdS7P59BP5996siR_LyKT4=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1027154.jpg |
| 87 | 1013013 | the tax chart | https://boardgamegeek.com/image/1013013/imperial-2030 | https://cf.geekdo-images.com/rvglgp2fHYqnU6NJNbb9OQ__large/img/IMRfJLavKIFQfZ6x3VhSI63Yq7A=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1013013.jpg |
| 88 | 1013008 | the Global map overall | https://boardgamegeek.com/image/1013008/imperial-2030 | https://cf.geekdo-images.com/xGpKJ7YNhSjTmSK51ptw3w__large/img/8ykZQ3tOU4f47a0VqWwYLXPL6Oo=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1013008.jpg |
| 89 | 1013004 | The east side with China Australia and Russia | https://boardgamegeek.com/image/1013004/imperial-2030 | https://cf.geekdo-images.com/0rAWa7uCHRSDIsX3A9bPIw__large/img/6mX_DrM8WSi0KZv0IXR9rVGfPhY=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1013004.jpg |
| 90 | 1013003 | the world map from the east side | https://boardgamegeek.com/image/1013003/imperial-2030 | https://cf.geekdo-images.com/v4GJbLUDaO3khuq_JFgHDA__large/img/jbv6OYg0NHh50uQcVyFMJkOto4I=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1013003.jpg |
| 91 | 1013002 | flags for tax chips | https://boardgamegeek.com/image/1013002/imperial-2030 | https://cf.geekdo-images.com/3AXN4-Osngp4KCBXl5m5pg__large/img/eWLRcrYt63Hi1aeSzNloXPxRoSg=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1013002.jpg |
| 92 | 1013001 | new tax chips with flags of each country | https://boardgamegeek.com/image/1013001/imperial-2030 | https://cf.geekdo-images.com/nNL7Dyw-2Y9xIrSf_HAY-w__large/img/rVdfI7rRybOj-4oxcoWVktq5gMs=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1013001.jpg |
| 93 | 1012999 | new components for the armies and fleets | https://boardgamegeek.com/image/1012999/imperial-2030 | https://cf.geekdo-images.com/s_OTTWLzlhMeVIauezFxVQ__large/img/X5-RY0FZuzQa6XpmbuXQno-YIrM=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1012999.jpg |
| 94 | 1012998 | my bonds during the game | https://boardgamegeek.com/image/1012998/imperial-2030 | https://cf.geekdo-images.com/oobDSpZxMCme20_OhkBmzw__large/img/runQWpV14xZmAnmniQ6pkd4zios=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1012998.jpg |
| 95 | 1012997 | Europe and Africa | https://boardgamegeek.com/image/1012997/imperial-2030 | https://cf.geekdo-images.com/SNRyKcd2jA9u4luKsZTUyg__large/img/H92s1gRC9b04EzlR4h3XKZssVoU=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1012997.jpg |
| 96 | 1012995 | Brazil and South America | https://boardgamegeek.com/image/1012995/imperial-2030 | https://cf.geekdo-images.com/yBTOFCOr_RqxgeT_VXwaCg__large/img/zcjs0jQvLcwcST9z5F-wPs9cZd8=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1012995.jpg |
| 97 | 1012988 | the swiss tiles indicating no country control | https://boardgamegeek.com/image/1012988/imperial-2030 | https://cf.geekdo-images.com/eypoFQfnP6fuPpHkRvWDAw__large/img/-4EFllAwJP04ctfHPA20zealGsA=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1012988.jpg |
| 98 | 1012985 | in the middle of the game | https://boardgamegeek.com/image/1012985/imperial-2030 | https://cf.geekdo-images.com/IFL1qsgfbngGEsbgD4-UbA__large/img/QhY4Ae9Eg64fP7K4ur-dfMZ7bYE=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1012985.jpg |
| 99 | 1012984 | a 3 player session. our first Imperial 2030 | https://boardgamegeek.com/image/1012984/imperial-2030 | https://cf.geekdo-images.com/ppYNVTK0BVCKiGMO-VawdA__large/img/emfJnf_EQ00mULe7K-aIUyG-USU=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1012984.jpg |
| 100 | 1012982 | new edition money. very much smaller | https://boardgamegeek.com/image/1012982/imperial-2030 | https://cf.geekdo-images.com/8aVEmbOFhoQ28gEWkrRjcA__large/img/zSDRq0o1Mi-vKoZIkNDPkTuvBKE=/fit-in/1024x1024/filters:no_upscale():strip_icc()/pic1012982.jpg |

## 4. Videos

Count: **35** video records. `config.numitems` = 35. `config.endpage` = 1. Page count: 1.

The BGG URL is `https://boardgamegeek.com` plus `href`. The external URL is built only from `videohost` and `extvideoid` (`youtube` → `https://www.youtube.com/watch?v=`, `vimeo` → `https://vimeo.com/`). `duration` is copied as returned, including empty and `N/A`.

| # | videoid | title | language | duration | BGG URL | external URL |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 505230 | IMPERIAL 2030 \| In My Box Insert Review | English | PT5M16S | https://boardgamegeek.com/video/505230/imperial-2030/imperial-2030-in-my-box-insert-review | https://www.youtube.com/watch?v=fmjNPRUPdV0 |
| 2 | 494641 | Imperial 2030 - Einfach Losspielen (Brettspiel Regeln) | German | PT19M33S | https://boardgamegeek.com/video/494641/imperial-2030/imperial-2030-einfach-losspielen-brettspiel-regeln | https://www.youtube.com/watch?v=cZs1BTJv82o |
| 3 | 417595 | Unboxing Imperial 2030 (No Talking) | English | PT2M33S | https://boardgamegeek.com/video/417595/imperial-2030/unboxing-imperial-2030-no-talking | https://www.youtube.com/watch?v=c_nykEInaaE |
| 4 | 390261 | Imperial 2030 - Review | Turkish | PT9M35S | https://boardgamegeek.com/video/390261/imperial-2030/imperial-2030-review | https://www.youtube.com/watch?v=wTgbgZPLhho |
| 5 | 388035 | Evolution of a Board Game: Imperial 2030 | English | PT1M48S | https://boardgamegeek.com/video/388035/imperial-2030/evolution-of-a-board-game-imperial-2030 | https://www.youtube.com/watch?v=7nqwtD5XM_A |
| 6 | 343704 | Peaky Boardgamer Episode #87 - Imperial 2030 - Full rules explanation (English) | English | PT20M49S | https://boardgamegeek.com/video/343704/imperial-2030/peaky-boardgamer-episode-87-imperial-2030-full-rul | https://www.youtube.com/watch?v=vEPzqVDfGvk |
| 7 | 316428 | Tutorial e Recensione Imperial\Imperial 2030 - Guerra & Soldi! | Italian | PT34M32S | https://boardgamegeek.com/video/316428/imperial-2030/tutorial-e-recensione-imperialimperial-2030-guerra | https://www.youtube.com/watch?v=GufhYIi_C2A |
| 8 | 303101 | The Purge: # 3027 Imperial vs Imperial 2030: We compare the versions and tell you which one you should get | English | PT5M23S | https://boardgamegeek.com/video/303101/imperial-2030/the-purge-3027-imperial-vs-imperial-2030-we-compar | https://www.youtube.com/watch?v=6FEFmKeIm5I |
| 9 | 290999 | Imperial 2030 Game Session Highlights | English | PT14M37S | https://boardgamegeek.com/video/290999/imperial-2030/imperial-2030-game-session-highlights | https://www.youtube.com/watch?v=6vKrH_PP4Zo |
| 10 | 280907 | Run-through: Imperial 2030 | English | PT32M34S | https://boardgamegeek.com/video/280907/imperial-2030/run-through-imperial-2030 | https://www.youtube.com/watch?v=MpGvIzTYLFQ |
| 11 | 280217 | Imperial 2030 First Game | English | PT13M29S | https://boardgamegeek.com/video/280217/imperial-2030/imperial-2030-first-game | https://www.youtube.com/watch?v=HUh9CPqIfZw |
| 12 | 279879 | Overview: Imperial 2030 | English | PT14M17S | https://boardgamegeek.com/video/279879/imperial-2030/overview-imperial-2030 | https://www.youtube.com/watch?v=CJiMbizHrNE |
| 13 | 272442 | RECENSIONE IMPERIAL 2030 ITA | Italian | PT6M16S | https://boardgamegeek.com/video/272442/imperial-2030/recensione-imperial-2030-ita | https://www.youtube.com/watch?v=JXeYd6HrV8A |
| 14 | 226767 | Imperial 2030 | Dutch | PT25M51S | https://boardgamegeek.com/video/226767/imperial-2030/imperial-2030 | https://www.youtube.com/watch?v=t4g-hw4dmVQ |
| 15 | 187283 | Comparativa Imperial 2030 con Imperial | Spanish | PT9M18S | https://boardgamegeek.com/video/187283/imperial-2030/comparativa-imperial-2030-con-imperial | https://www.youtube.com/watch?v=IaVFZqHv5l0 |
| 16 | 169882 | [TH] Imperial 2030 | Thai | PT2H4M25S | https://boardgamegeek.com/video/169882/imperial-2030/th-imperial-2030 | https://www.youtube.com/watch?v=TrSDkc4IH88 |
| 17 | 150382 | Boardgame Opinions: Imperial 2030 | English | PT7M32S | https://boardgamegeek.com/video/150382/imperial-2030/boardgame-opinions-imperial-2030 | https://www.youtube.com/watch?v=k_092UftXhY |
| 18 | 150237 | Imperial 2030 / Cómo se juega | Spanish | PT37M29S | https://boardgamegeek.com/video/150237/imperial-2030/imperial-2030-como-se-juega | https://www.youtube.com/watch?v=OSt3uFwNmZE |
| 19 | 138917 | Shut Up & Sit Down reviews: IMPERIAL 2030 | English | PT19M40S | https://boardgamegeek.com/video/138917/imperial-2030/shut-up-and-sit-down-reviews-imperial-2030 | https://www.youtube.com/watch?v=CElzUejyO_Y |
| 20 | 118581 | Imperial 2030 \| GTTV | Polish | PT14M | https://boardgamegeek.com/video/118581/imperial-2030/imperial-2030-gttv | https://www.youtube.com/watch?v=xlOkk1qyxUI |
| 21 | 104804 | Review feito pelo canal After Match. | Portuguese | PT7M6S | https://boardgamegeek.com/video/104804/imperial-2030/review-feito-pelo-canal-after-match | https://www.youtube.com/watch?v=p8bw54Qwgno |
| 22 | 51822 | Meu Turno - Imperial 2030 Review | Portuguese | PT55M13S | https://boardgamegeek.com/video/51822/imperial-2030/meu-turno-imperial-2030-review | https://www.youtube.com/watch?v=L5qm3XdpRCM |
| 23 | 18864 | Imperial 2030 - Review | Dutch | PT5M31S | https://boardgamegeek.com/video/18864/imperial-2030/imperial-2030-review | https://www.youtube.com/watch?v=eSWB2tbNXE8 |
| 24 | 18863 | Imperial 2030 - Speluitleg | Dutch | PT20M52S | https://boardgamegeek.com/video/18863/imperial-2030/imperial-2030-speluitleg | https://www.youtube.com/watch?v=lceRN1T8m3s |
| 25 | 16911 | [Vídeo-explicación] Imperial 2030 | Spanish | N/A | https://boardgamegeek.com/video/16911/imperial-2030/video-explicacion-imperial-2030 | https://www.youtube.com/watch?v=9JdC4w8wKGY |
| 26 | 12278 | SpieLama Review [german] | German | PT31M54S | https://boardgamegeek.com/video/12278/imperial-2030/spielama-review-german | https://www.youtube.com/watch?v=KZf7YYt1Zoo |
| 27 | 11678 | Uitleg & Review (NL) - Nox' Spellenzolder | Dutch | PT21M49S | https://boardgamegeek.com/video/11678/imperial-2030/uitleg-and-review-nl-nox-spellenzolder | https://www.youtube.com/watch?v=aF5y0S7dCdE |
| 28 | 8780 | TRPMGSMT Imperial 2030 - Void In Control | English | PT13M36S | https://boardgamegeek.com/video/8780/imperial-2030/trpmgsmt-imperial-2030-void-in-control | https://www.youtube.com/watch?v=4aLvu1rAdJk |
| 29 | 8749 | TRPMPSMT Imperial 2030 2- Big Men Don't Get Paid | English | PT14M34S | https://boardgamegeek.com/video/8749/imperial-2030/trpmpsmt-imperial-2030-2-big-men-dont-get-paid | https://www.youtube.com/watch?v=yDDQzNOsvVI |
| 30 | 8707 | TRPMPSMT Imperial 2030 1- Character Draw | English | PT15M | https://boardgamegeek.com/video/8707/imperial-2030/trpmpsmt-imperial-2030-1-character-draw | https://www.youtube.com/watch?v=fD7-eXpdkck |
| 31 | 8641 | Hello! A Review of Imperial 2030 | English | PT7M17S | https://boardgamegeek.com/video/8641/imperial-2030/hello-a-review-of-imperial-2030 | https://www.youtube.com/watch?v=jOIgFOLR8q4 |
| 32 | 3912 | Game Night Imperial, at The Joker, Utrecht, The Netherlands | Dutch | PT3M21S | https://boardgamegeek.com/video/3912/imperial-2030/game-night-imperial-at-the-joker-utrecht-the-nethe | https://www.youtube.com/watch?v=ohfYxIuFXok |
| 33 | 3876 | Brief description [English] | English | PT2M40S | https://boardgamegeek.com/video/3876/imperial-2030/brief-description-english | https://www.youtube.com/watch?v=Uq4YhNxZ66c |
| 34 | 3875 | Korte beschrijving Nederlands | Dutch | PT2M51S | https://boardgamegeek.com/video/3875/imperial-2030/korte-beschrijving-nederlands | https://www.youtube.com/watch?v=XGLfUG1_Rw0 |
| 35 | 117 | Imperial 2030 Demo - Spiel 2009 - Geekdo Booth | English | (empty string) | https://boardgamegeek.com/video/117/imperial-2030/imperial-2030-demo-spiel-2009-geekdo-booth | https://vimeo.com/7437268 |

## 5. Differences between Imperial and Imperial 2030

The HTML wiki URL returned HTTP 403, so this section quotes the `wiki` string on the geekitems item. The heading in that field is "Differences between Imperial and Imperial 2030". Text after the Swiss Bank paragraph (Online Play, Microbadges, Awards) is included because it was in the same field. No differences were added.

Differences between Imperial and Imperial 2030

Nations: The nations are now United States, Europe, Russia, China, India and Brazil.

Game Board: Nations have only 4 home provinces and a max of 4 factories. There are many more sea (11 vs. 9) and neutral (27 vs. 15) regions. The board wraps around: the sea regions on the western and eastern edges of the board are adjacent to each other.

Canals: Fleets can use the Panama and Suez canals and troops may be transported through them. If a nation controls Colombia, they may deny the use of the Panama Canal to other nations. If a nation controls North Africa, they may deny the use of the Suez Canal to other nations.

Rondel: When moving more than 3 spaces, the payment for additional spaces is $1M + ($1M x nation's Power Factor).

Bonds: Each nation now also has a $30M bond that pays $9M (30%) interest.

Taxation: Success Bonus for a player is a fixed amount based on the Tax Chart. Also, the bonus is taken out of the nation's treasury instead of the bank thus the player may not receive the full amount if the treasury is short of money.

Swiss Bank: Any player who does not control a government receives a Swiss Bank instead. If a nation tries to pass the Investor space on the Rondel, a Swiss Bank can force the nation to stop on the Investor space if there is enough money in the Treasury to pay out all interests.

Online Play

- BrettspielWelt (real-time) — anchor href `/wiki/page/BrettspielWelt#`
- playimperial.club (asynchronous & real time) — anchor href `https://www.playimperial.club`

The "Online Play" heading itself linked to `/wiki/page/Online_Play#`. The "Awards" heading linked to `/wiki/page/Awards#`. "Gouden Ludo" linked to `/wiki/page/Gouden_Ludo#`. The "Microbadges" heading linked to `/wiki/page/Microbadges#`.

Microbadges

The visible text of this part was only the heading. Two images were inside it. Their `alt` and `src` values, which tag-stripping had dropped, are:

- href `/microbadge/12122` — alt `Microbadge: Imperial 2030 fan` — src `https://cf.geekdo-static.com/mbs/mb_12122_0.gif`
- href `/microbadge/39003` — alt `Microbadge: Imperial 2030 fan` — src `https://cf.geekdo-static.com/mbs/mb_39003_0.png`

Awards

2011 Gouden Ludo Nominee (Flanders/Belgium)

The `description` field has a shorter, different "new features" list (wooden bits, Swiss Bank, 30 million bond, neutral territory, home provinces, canals, and the Essen map-and-bonds note). That text is quoted in section 1 and is not repeated here as if it were the wiki differences section.

## 6. Copyright and license notices

No `license`, `licence`, `copyright`, or Creative Commons field or string was found on the geekitems item, on any file object, or on the image objects that were retrieved.

One file description contains a permission sentence. File page 75691, title "Imperial 2030 Reglas, Ayuda y Rondel en Español", description:

> Rondel de Imperial 2030 en Español, de España, Versión 1.
> Subido con permiso de Mac Gerdts.

No other license notice was retrieved. Image records did not include a per-image license even though the images `config.licensefilters` list offered filter labels.

## 7. Classification of files

Classes use only the title and the description text. "unspecified" means those texts do not say rules document, player aid, or scoring sheet, and also do not clearly name a different kind of item. "other" means the title or description names something that is none of those three.

Counts:
- rules document: 9
- scoring sheet: 7
- player aid: 6
- unspecified: 3
- other: 2
- rules document and player aid: 1

| filepageid | title | classification |
| --- | --- | --- |
| 320460 | Règles du jeu Imperial 2030 (format A4, DocGuillaume) | rules document |
| 262361 | Imperial 2030 Scoring Sheet | scoring sheet |
| 244121 | Imperial 2030 | rules document |
| 236294 | Imperial 2030 riassunto regolamento | rules document |
| 220206 | Finnish player aid for Imperial 2030 | player aid |
| 201008 | Imperial 2030 | rules document |
| 197755 | Imperial 2030 - rules in brief | rules document |
| 134244 | Imperial 2030 GameAid (Thai) | player aid |
| 133712 | A quick guide to odd rules of Imperial 2030 | rules document |
| 133630 | Imperial 2030 Thai Rule | rules document |
| 97688 | Printer friendly automated score sheet | scoring sheet |
| 94859 | Империал 2030 (Игровед) | rules document |
| 94530 | Imperial 2030 player aid em português do Brasil | player aid |
| 92797 | Imperial 2030 - Aide de jeu | player aid |
| 87819 | Imperial2030_HojasPuntuación | scoring sheet |
| 87818 | Imperial2030_ScoreSheet | scoring sheet |
| 85285 | Scoreblad | scoring sheet |
| 82500 | Samenvattingskaart | unspecified |
| 81362 | Imperial 2030 Tuckboxes | other |
| 75691 | Imperial 2030 Reglas, Ayuda y Rondel en Español | rules document and player aid |
| 74107 | Карточка с описанием ронделя на русском | unspecified |
| 70828 | Imperial 2030 player aid in Italian | player aid |
| 58757 | Rróżnice w stosunku do Imperiala | other |
| 53936 | Imperial 2030 Setup and Turn Order Player Aid | player aid |
| 53841 | Imperial 2030 - Integrated Scoresheet | scoring sheet |
| 51497 | Imperial 2030 result sheet | scoring sheet |
| 47882 | Imperial 2030 English Rules.pdf | rules document |
| 47881 | Imperial 2030 Quick Intro.pdf | unspecified |

## Counts

- Files: 28 (1 page, `config.numitems` 28)
- Images: 217 total; 100 listed
- Videos: 35 (1 page, `config.numitems` 35)

