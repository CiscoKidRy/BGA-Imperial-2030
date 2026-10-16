# Review of the board design against the play page

Date: 2026-10-15. Peer review only. I read `2026-10-15-board-ui-synthesis.md`, `2026-10-15-board-ui-3-tracks.md`, `2026-10-15-board-ui-4-pieces.md`, and `playtest/index.html`, including `renderBanner`, `renderMap`, `renderRondel`, and `renderPanels`. I compared those with the tax chart, the trays, and the scoring track on that page. I did not edit the game, and I did not change `playtest/engine.py` or Studio `Game.js`.

The synthesis can replace the box grid only if a builder can follow it and still keep every behavior the page already has. It cannot. Four of the six checks hold. The other two, and several behaviors outside that list, are not in the design.

## Checks

1. Banner and rondel. Holds. The synthesis keeps the dark next-action banner above the board, keeps Confirm in that banner, and says a wedge click selects and does not commit. That is what the page does. The click sends the existing rondel choice. Confirm, or Place here on a first turn, is the button that commits.

2. View as and private cash. Does not hold. The synthesis says private cash stays in the side list and stays hidden from other seats. It does not say that View as clears the cash nodes before the next seat is drawn, and it does not say the hidden value is the word Private.

3. Illegal region click. Does not hold. The synthesis says which names are targets, and that only a legal region gets an outline. It never says what the click does. The page still has a sentence for a click that is not exactly one legal choice.

4. Pieces. Holds. The synthesis matches the piece note: a brown square, a light-blue square, a ship in the nation color, a nation-colored army block, and a pin lettered R, C, I, B, U, or E. It says not to draw a copied flag. The tracks note still describes waving national flags. The synthesis already sets those aside. The light-blue square is the harbor factory the page already shows. It is not a new piece type.

5. Tax highlight. Holds. The synthesis says to highlight the active column only during Taxation. The page highlights a column only when the phase is Taxation, and only the column the engine marks on that legal action.

6. Engine file. Holds. The synthesis says the engine is not changed, and that Studio `Game.js` is not edited. Nothing in the design requires a change to `playtest/engine.py` either. The factor groups in the synthesis are the engine's groups: no label on cell 0, x0 over 1–5, x1 over 6–10, x2 over 11–15, x3 over 16–20, x4 over 21–24, and x5 on 25 only. The tracks note, which starts x1 on cell 5, is the reading the synthesis refuses. Building that reading would show a different factor than the engine while leaving the engine alone.

## Behavior the design does not keep

View as is a button on the current page. Its click removes every cash node, including the add-million field, then changes seat, then draws the next view. The previous number is gone before that draw. A late response for the seat just left does not paint that seat's cash. When the engine omits a number, the side list says Private. When the engine sends a number, the page shows it, including every seat at the end of the game. "Hidden" is not the word on the page. A board that waits for the next response before clearing the old number, or that substitutes another word, drops this.

A city, sea, or neutral with exactly one enabled choice is sent. Any other click on those regions sets the banner sentence to "Not a legal choice." and then lets the real sentence come back. That includes a region with no legal choice and a region with two, such as a harbor that can take both an army and a fleet. The page does not guess. The choice list in the banner is how those two are picked. Printed names that are not engine regions are not clicks today. The design's extra labels must stay that way. Making only the outlined regions clickable would drop the sentence.

The piece recipe has no hostile or friendly mark. The page prints one of those words on every army, and that is the only place it does so. The recipe also does not say that a region keeps every army, fleet, flag, and factory when they share a region. A single token would drop the rest. A region with no piece still shows its name in both the page and the design. That part can stay.

The one wheel is the right replacement for the second wheel. These facts live only on the current wheel and are not in the design: the step count or the word "any", the cost, which stop is selected, and the words "cannot pay". "Cannot pay" is shown only to the acting seat. Other seats see the public cost and do not see a blocked unpaid wedge. A dark wedge for the whole table would show a bound on secret cash. A stop that is not a legal choice does not select. Taxation is drawn at 12 o'clock, and that stop is still the engine's Taxation index. Factory remains the engine's first stop. The drawing turns. The targets do not. A nation that has not left the hub is labeled in the hub on the page. The design only stands a cylinder on a current wedge, so an unplaced marker would disappear.

The synthesis says the trays show the public figures the test already shows, then names government, treasury, and the top bond. The page also shows credit, with the note that it decides government, interest, with the note that it does not, power, factor, how many of the top bond are left, factories, and armies, fleets, and flags on the board and still in supply. It also marks the active nation. Those figures are not on the map. Cutting the tray to three lines drops them. The tracks note's nine-pair bond stack is not on the page. The synthesis already says not to paste that sheet onto the map.

The page puts each nation's marker on its power cell, with that nation's color, pattern, and name. The design draws the track and never places the markers. If the tray also loses the power row, the power position is gone from the screen.

The side list's other lines are not named: bonds, nation cards, Investor, Swiss Bank, adding cash to a nation the viewed seat governs, the log, the limit note, and the end score. The banner is the same kind of gap. Confirm stays. The page also puts Cancel there, and Cancel clears the selected wedge without moving. The other action buttons, the choice list, and the steps are in that banner too.

## Not a loss

The four scroll buttons and the sentence "No army enters" belong to the box grid. The red cross is not an engine region, and the design already leaves it unnamed and unclickable. Those can go. Panama's west mouth stays undrawn, which the design already says, and the limit note already says it. The caption that Factory is at the top of a second wheel would be false on this board. Do not keep it. Do not draw the tracks note's flags, and do not build its factor groups.

## Reject

Changes required before building:

1. Keep the dark banner as the page draws it. The sentence stays there. Confirm stays there. Cancel stays there and still clears the selected wedge without moving. The other action buttons, the choice list, and the steps stay in that banner.

2. A rondel click still only selects. It uses the existing choice and does not commit. Confirm commits. Draw Taxation at the top without renumbering the stops. The two Production stops stay two targets, and the two Maneuver stops stay two targets. Each offered stop still shows its steps or "any", its cost, and whether it is selected. "Cannot pay" is shown only to the acting seat. Other seats do not see a blocked unpaid wedge. A stop that is not legal does not select. A nation still in the hub is still shown in the hub.

3. View as stays. That click removes the cash nodes, including the add-million field, before the next seat is drawn. A late response for the previous seat must not draw that seat's cash. When the engine omits the number, the side list says Private. When the engine sends a number, show that number, including at the end of the game. Do not print private cash on the board or on a tray.

4. A click on an engine city, sea, or neutral that is exactly one enabled choice still sends that choice. Any other click on those regions still sets the banner sentence to "Not a legal choice." and then lets the real sentence return. Do not pick one of two choices on the same region. Names that are not in the engine are not clicks.

5. Keep the piece-note shapes, and do not draw a copied flag. The light-blue square is the harbor factory. An army block still says hostile or friendly. A region still shows every army, fleet, flag, and factory on it, and still shows its name when it has none.

6. Highlight the tax column only while the phase is Taxation, using the column the engine already marks. Keep the page's note that a revenue of 7, 9, or 17 uses the rightmost header at or below it.

7. Keep every public tray row the page shows now: government, credit, interest, treasury, power, factor, the top bond with how many are left, and the factory, army, fleet, and flag counts. Still mark the active nation. Do not draw the bond sheet on the map.

8. Keep each nation's marker on its power cell, with the color, pattern, and name the page already uses. Use the synthesis factor groups. Do not use the tracks note's groups.

9. Keep the side list's bonds, nation cards, Investor, Swiss Bank, add-to-treasury control, log, limit note, and end score. Do not edit `playtest/engine.py` or Studio `Game.js` for this design.
