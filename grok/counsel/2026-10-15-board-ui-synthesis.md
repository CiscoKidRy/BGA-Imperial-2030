# Board-like screen, 2026-10-15

This is the design for the local test screen. It follows the empty board photo `reference/bgg/images/574713.jpg` and the close-ups named in the four notes. The drawing is original. The publisher photo is not embedded and is not traced.

Sources for this page: `2026-10-15-board-ui-1-map.md`, `2026-10-15-board-ui-2-rondel.md`, `2026-10-15-board-ui-3-tracks.md`, `2026-10-15-board-ui-4-pieces.md`, and an enlargement of the top of 574713 read on 2026-10-15.

## What the screen becomes

One board, wider than it is tall, with a dark navy frame and a light-blue ocean. The scoring track crosses the top. The map fills the middle. One rondel sits in the South Pacific, west of South America. The tax chart sits on the ocean south of Africa. Six nation trays run along the bottom: Russia, China, India, Brazil, USA, Europe. The red land is on the left. The green land is left of center. The blue land is near the middle. The trays are not stacked under the matching lands.

The dark next-action banner stays above the board. Confirm stays in that banner. Private cash stays in the side list and stays hidden from other seats. The engine is not changed.

## Map

Use the percentage boxes in the map note as the placement. Draw flat original shapes. City names sit on pale labels.

Click targets are only the cities, seas, and neutrals already in the engine. Printed names that are not in the engine stay as labels: Alaska, Canada, Quebec, Peru, Argentina, Ukraine, Kazakhstan, Mongolia, Afghanistan, Iran, Near East, Guinea, Nigeria, East Africa, Congo, South Africa, Philippines, Australia, and New Zealand. The edge arrows, the PD emblem, and the unnamed island east of South Africa are not targets.

The white land at the upper left has no readable name. Do not label it Greenland. The tiny white patch with a red cross inside the blue land has no readable name. It is not a click target. Do not add a move border that the engine does not already have. Panama's west mouth stays undrawn.

A region with no piece still shows its name. Only a region that is a legal choice gets a light outline and a dark hairline.

## Rondel

One wheel, in the South Pacific. It is the position marker and the click control. There is no second wheel.

On close-up 576979, 12 o'clock is Taxation, golden yellow. Clockwise: Factory blue, Production gray, Maneuver yellow-green, Investor light blue, Import orange, Production gray, Maneuver yellow-green. From Factory, that is the engine order. Do not rotate Factory to the top.

A click selects a wedge. It does not commit the move. The two Production wedges are two targets. The two Maneuver wedges are two targets. The line under the wheel is "1 to 3 fields for free". A nation cylinder stands on that nation's current wedge.

## Track and tax chart

The tracks note shifts the factor groups so that x1 begins on cell 5. That reading is not used. An enlargement of the top of 574713 shows x0 over 1–5, x1 over 6–10, x2 over 11–15, x3 over 16–20, x4 over 21–24, and x5 on 25 only. Cell 0 has no factor label. Cells 5, 10, 15, and 20 are lighter. Cell 25 is gold. Those groups match the engine.

The tax chart on the photo matches the engine: headers 0-5, 6, 8, 10, 11, 12, 13, 14, 15, 16, 18+; bonus 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5; power 0 then +1 through +10. Draw that chart on the ocean. Highlight the active column only during Taxation.

## Trays and pieces

Each tray is the nation color, with the short name, a simple three-band mark plus the nation letter, and the public figures the test already shows: government, treasury, and the top bond as interest/price. Do not draw a copied flag, and do not paste the bond sheet onto the map. Do not print private cash on a tray.

Pieces, as original shapes: a brown square for an armament factory, a light-blue square for a shipyard, a small ship for a fleet, a nation-colored block for an army, and a pin with R, C, I, B, U, or E for a flag. Empty city sites are circles in the same brown or light-blue. A city that holds a factory shows the square.

## Play review

`2026-10-15-board-ui-review-play.md` rejects a board that drops behavior the page already has. The build keeps those behaviors.

`2026-10-15-board-ui-review-layout.md` reads the track rules as falling after 4, 9, 14, 19, and 24. An enlargement of the header, read after that note, shows x0 over 1–5, x1 over 6–10, x2 over 11–15, x3 over 16–20, x4 over 21–24, and x5 on 25. The lighter number cells are 5, 10, 15, and 20. Cell 25 is light, and its numeral is gold. The screen uses that enlargement. It does not fill cell 25 gold. The engine's factor groups are the same groups, and the engine file is not edited.

The dark banner still holds the sentence, the steps, the choice list, Confirm, and Cancel. A wedge click only selects. Confirm commits. Cancel clears the selection. Taxation stays at the top of the drawing. The engine indexes do not move. Each offered stop shows its steps or "any", its cost, and whether it is selected. "Cannot pay" is only on the acting seat's wedge. A nation still in the hub is shown in the hub.

View as still removes the cash nodes before the next seat is drawn. A missing cash number is the word Private. Private cash is not printed on the board.

A click on an engine city, sea, or neutral sends the action only when that region is exactly one enabled choice. Any other click on those regions sets "Not a legal choice." Names that are not in the engine are not clicks.

An army block still says hostile or friendly. A region shows every piece on it. The tax column is highlighted only during Taxation. The trays keep every public row the page shows now, and each nation marker stays on its power cell. The side list keeps bonds, nation cards, Investor, Swiss Bank, the add-to-treasury control, the log, the limit note, and the end score.

## Drawn screen

The page draws the wheel in open water, west of Brazil. Each action name is drawn inside its wedge. Taxation is at the top. The coasts are original polygons. `2026-10-15-board-ui-review-visual.md` and `2026-10-15-board-ui-review-after-draw.md` both end in Accept.

## Left out of this pass

Studio `Game.js` is not edited. The publisher images stay out of git. Convoy, factory destruction, the 15-flag choice, both variants, and the basic setup stay absent.
