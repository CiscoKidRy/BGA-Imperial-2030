# Review of the board after the draw

Date: 2026-10-15. Peer review only. I read `playtest/index.html` and `2026-10-15-board-ui-review-play.md`, including `renderBanner`, `renderMap`, `bindRegions`, `pieces`, `renderRondel`, `renderTax`, `renderTrack`, and `renderPanels`. I did not edit the page, and I did not change `playtest/engine.py`.

The page does not import or name the engine file. A search of `playtest/index.html` finds no `engine.py`. Git shows `playtest/index.html` modified and `playtest/engine.py` with no diff. This draw did not need an engine change. Studio `Game.js` is not in the file. There is no publisher JPEG, no image address, and no embedded image. The land is inline SVG.

The Chrome check from 2026-10-15 is the browser evidence, and I am not substituting another result. It reported no page errors, the word Greenland absent, the eight wedge names present, the banner sentence "Ava, choose one Russia bond, or pass.", a Chicago click showing "Not a legal choice.", and View as Bo cash reading Private, 19 million, Private, Private. At 390px the page scroll width equaled the client width. The source matches that report. Greenland is not in the city, sea, neutral, or label lists.

## Checks

1. Banner and wedge. Holds. The dark banner is still `#next-action`. It still draws the sentence, the steps, the choice list, and every enabled primary, alert, and secondary action. Confirm and Cancel are those buttons, from their labels, and their clicks send their own actions. A wedge click sends only `rondel:` plus that stop's engine index, and only when that stop is enabled. That is the selection. It does not send Confirm. A stop that is not enabled does not send.

2. View as and private cash. Holds. The View as click removes every cash node, including the add-million field, and only then changes seat and draws the next view. A late response for the seat just left does not draw. When the cash number is missing, the side list says Private. When a number is present, the page shows that number. The reported Bo reading is that rule.

3. Region click. Holds. A city, sea, or neutral sends only when that name is exactly one enabled choice. Any other click on those regions sets the banner sentence to "Not a legal choice." and then lets the real sentence return. That covers a region with no choice and a region with two. The Chicago result matches. Alaska, Canada, and the other printed names that are not engine regions are labels with no click. The cross is not a click.

4. Pieces. Holds. Each army is drawn with the word hostile or the word friendly, not only in a tooltip. A region appends its factory, every army, every fleet, and its flag.

5. Tax highlight. Holds. A column is marked only when the phase is Taxation, and only the column the engine marks. The headers are 0-5, 6, 8, 10, 11, 12, 13, 14, 15, 16, 18+. The note about 7, 9, and 17 is still there.

6. Factors. Holds. The track is 0 through 25. The labels span x0 over 1–5, x1 over 6–10, x2 over 11–15, x3 over 16–20, x4 over 21–24, and x5 on 25 only. Cell 0 has no factor label.

7. Rondel targets. Holds. The two Production stops are `rondel:1` and `rondel:5`. The two Maneuver stops are `rondel:2` and `rondel:6`. Taxation is index 7 and is drawn at the top. The indexes are not renumbered. Factory stays index 0. Neighbor phrases are in the accessible name. The visible text is the action name, and, when a stop is offered, the steps or the word any, the cost, the word selected when it is selected, and the words cannot pay only when `privateBlock` is set.

8. Before a game. Holds. The setup form is still in the banner, with the player count and the experienced-setup button. Map clicks are not bound until a game exists, and the buttons do not send.

9. Left out of this file. Holds. Studio `Game.js` is not part of this file. The publisher JPEG is not embedded in the HTML.

The trays, the power markers, the hub label for a nation that has not left the hub, and the side list are still on the page. They were not part of this pass's reject list, and the draw did not remove them.

Accept