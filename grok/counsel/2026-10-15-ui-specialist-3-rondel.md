# Action rondel, 2026-10-15

Specialist note for the choice wheel. This file does not change `grok/ui-design-2026-10-15.md`. It does not add rules to `Game.js`, and it does not copy image 576979 into the repo.

## What was opened

The interface plan, rondel section, and image 576979. The photograph is eight wedges around a hub. The type on those wedges follows the curve. The line under the wheel reads "1 to 3 fields for free". Production is printed twice. Maneuver is printed twice. Factory, Investor, Import, and Taxation are printed once. A curved reading of that photograph is easy to scramble, so this note does not re-sort the wedges. The clockwise order used here is the order already fixed: from Factory, Production, Maneuver, Investor, Import, Production, Maneuver, Taxation, then Factory again. The two Production spaces are different stops. The two Maneuver spaces are different stops. The Production immediately after Factory is the first of those two.

## Two wheels

The wheel printed in the South Pacific is a position marker only. It keeps every nation's octagon. It is not a click target at any screen width, including a wide screen. Map zoom must not change the size of the choice control.

The choice is a second rondel, the action rondel, outside the map viewport. It shows the active nation's octagon only. Factory is fixed at 12 o'clock on this control even if the printed wheel sits at another rotation. A horizontal caption under the circle says: "Factory is at the top here. The map wheel may be turned differently. The clockwise order is the same." Under that, upright, not on a curve: "1 to 3 fields for free." In the choice list the same stops are called spaces. Fields on the printed line and spaces in the list are the same eight stops.

## When the choice is offered

The action rondel is on screen only when the active nation has a government and must take a rondel turn. A nation with no bonds is skipped in the base game, and this control stays closed. The no-Investor-card variant does not by itself open a rondel choice for a nation that still has no bonds.

The current space is never a row. The space seven steps clockwise is never a row. That seventh space is the neighbor just behind the octagon. The nation cannot stay, and it cannot move backward.

## First turn

Each nation starts with its octagon in the hub, not on a space. The first time that nation moves, the panel replaces the six-row list with eight rows and prints this sentence above them:

"First turn for {nation}. The octagon is in the hub. Any of the eight spaces may be chosen. The move is not limited to six spaces, and it costs nothing."

Every first-turn row costs 0 million, including Investor. None of them is disabled for money. The step column says "any", not a number from 1 to 6. The commit button reads "Place here". There is no pass-over state on this turn, because the octagon is not yet on a space. The Swiss Bank block stays closed.

## The six destinations

After the octagon is on a space, the list is the six clockwise spaces, in order, steps 1 through 6. Each row shows four facts: the space name, the step count, the cost in millions, and, for the acting player only, a disabled state when that player cannot pay.

Names that occur twice are not separated by color. The second line of the name is the neighbor phrase:

| Stop | Name on the row |
| --- | --- |
| Production immediately after Factory | Production, after Factory |
| Maneuver between that Production and Investor | Maneuver, before Investor |
| Investor | Investor |
| Import | Import |
| Production immediately after Import | Production, after Import |
| Maneuver between that Production and Taxation | Maneuver, before Taxation |
| Taxation | Taxation |
| Factory | Factory |

The two Production rows and the two Maneuver rows are separate controls. They do not share a button id. Suggested ids: `prod-after-factory`, `man-before-investor`, `investor`, `import`, `prod-after-import`, `man-before-taxation`, `taxation`, `factory`.

## Cost

Steps 1, 2, and 3 cost 0 million. Each space past the third adds (1 + that nation's power factor) million, and the row shows the sum, not the addend alone.

| Steps | Extra spaces past 3 | Total paid to the bank |
| --- | --- | --- |
| 1 | 0 | 0 million |
| 2 | 0 | 0 million |
| 3 | 0 | 0 million |
| 4 | 1 | 1 times (1 + power factor) million |
| 5 | 2 | 2 times (1 + power factor) million |
| 6 | 3 | 3 times (1 + power factor) million |

The government player pays that total from personal cash to the bank. The nation's treasury is not the source. The panel prints the factor in the heading, for example "Power factor 2." When the total is above 0, the cost cell also shows the product, for example "2 extra x (1 + 2) = 6 million".

Check against the booklet's China example, octagon on Investor, power factor 2. Clockwise from Investor the six rows are:

| Steps | Space | Cost |
| --- | --- | --- |
| 1 | Import | 0 million |
| 2 | Production, after Import | 0 million |
| 3 | Maneuver, before Taxation | 0 million |
| 4 | Taxation | 3 million |
| 5 | Factory | 6 million |
| 6 | Production, after Factory | 9 million |

Taxation at four spaces is 3 million, and Factory at five spaces is 6 million. That matches the example. Leaving Investor is not a pass over Investor. None of these six rows draws the pass treatment.

A second check, octagon on Factory, power factor 0, is the pass example:

| Steps | Space | Cost | Investor |
| --- | --- | --- | --- |
| 1 | Production, after Factory | 0 million | not crossed |
| 2 | Maneuver, before Investor | 0 million | not crossed |
| 3 | Investor | 0 million | land |
| 4 | Import | 1 million | pass |
| 5 | Production, after Import | 2 million | pass |
| 6 | Maneuver, before Taxation | 3 million | pass |

Taxation is seven steps from Factory and is not a row. Factory itself is not a row.

## Disabled when the player cannot pay

A row is disabled only when its cost is greater than the acting player's personal cash. A cost of 0 is never disabled. Poverty cannot remove the three free spaces, so a poor government can always move.

The disabled row stays visible. Its cost remains readable. The state cell says "cannot pay". It does not print the cash balance. The row is not a button, and it is not in the tab order as an actionable control. The same words appear in the wedge's accessible name. A gray fill is extra, not the only signal. Text contrast stays at least 4.5 to 1.

That disabled flag is private to the acting player. Other players and spectators see all six rows as payable choices, with the public costs, and without the words "cannot pay". Showing a dark space to the table would reveal a bound on secret cash. The log, after a legal choice, records the space, the step count, and the millions paid to the bank. It does not record the remaining personal cash.

## Pass over Investor, distinct from landing

A row lands on Investor only when that row's space is Investor. A row passes Investor when the clockwise arc from the current space to the destination crosses Investor and the destination is a later space. Those two states do not share a border style.

Landing preview, on hover, focus, or selection: the destination wedge has a 3px solid outline in the nation color. If that destination is Investor, one horizontal sentence sits under the list: "Land on Investor. Interest is paid." The Swiss Bank force block stays closed. Forcing a stop is not offered, because the nation is already choosing that space.

Pass preview: the destination wedge has the same 3px solid outline, and the Investor wedge has a 3px dashed outline. A 4px arc is drawn clockwise outside the circle from the current wedge to the destination, with a gap across the Investor wedge so the dashed wedge reads as crossed. The sentence under the list is: "Pass over Investor. This is not a landing. Interest is not paid." After the landed action, Investor steps 2 and 3 still run, then the government check, the Swiss Bank grant or return, and the Investor-card pass. If the chosen space is Taxation and that tax reaches 25, the sentence adds: "Steps 2 and 3 are skipped because Taxation reaches 25."

In the no-Investor-card variant the pass sentence does not mention the 2 million payment or an investment from the pass. The variant section removes those. It does not remove the force-stop, so the force block below still follows the treasury test.

## Swiss Bank force-stop

The force block sits under the choice list. It is a text control, with no icon.

It opens only after the acting player has selected a row whose arc passes Investor, and only when that nation's treasury can pay every bond's interest. The treasury test is public. It uses treasury cash and the face interest of bonds in that nation. It must not be wired to personal cash. The rondel-fee test must not be wired to the treasury. The two tests are different.

If the selected move does not pass Investor, the block says: "This move does not pass Investor." No buttons.

If the move passes Investor and the treasury cannot pay every interest, the block says: "Swiss Bank cannot force a stop. The treasury cannot pay every bond's interest." No buttons. The original destination remains legal.

If the treasury can pay, holders are asked one at a time, in player seating order, clockwise, starting at the player who holds the Investor card. A holder who also holds that card is still asked. Holding the card does not cancel the force. This question is not the later Swiss Bank investment.

The status line names the holder being asked. That holder sees two buttons. Everyone else sees the same question with both buttons disabled and the sentence "Waiting for {name}."

Button labels, exact: "Force stop on Investor" and "Do not force". The first "Force stop on Investor" replaces the selected move. Later holders are not asked. If every holder declines, or no Swiss Bank is held, the selected destination stands. If none is held, the block says: "No Swiss Bank is held. The move is not forced."

A forced stop is a landing on Investor, not a pass. The dashed treatment is removed and the land sentence is shown. The step count becomes the clockwise distance from the current space to Investor, which is 1, 2, or 3 when a farther row was a pass, so the recomputed fee is 0 million. The original row's fee is not charged. The plan prices a move by the space where the octagon stops. It does not add a second fee for the abandoned destination. From the Factory example, a selected Import at 4 steps and 1 million, if forced, becomes Investor at 3 steps and 0 million, and interest is paid because the marker lands there.

The acting player commits with a separate button, "Move here", enabled only when a payable row is selected. Selecting a row does not start the Swiss Bank poll. The poll starts after "Move here". On a first turn the button is "Place here", and there is no poll.

## Layout

Pixels below are CSS pixels at 1x.

The action panel is `#action-rondel`. It is 384px wide, including 16px padding, so the content column is 352px. It sits beside the map on a viewport at least 960px wide, and it stacks under the map below that. It does not cover the map, and it does not scale with map zoom. On a narrow viewport the panel becomes the width of the play column, the circle stays centered, and the rows stretch. The circle does not shrink below 240px. Row height does not shrink.

Circle: 288px outer diameter, 8px outer stroke, hub 64px diameter. Eight wedges, 45 degrees each, Factory centered on 12 o'clock, then clockwise in the fixed order. Clicks inside the hub do nothing. The wedge hit area is the ring from the hub edge to the outer stroke. At the outer radius the arc of one wedge is about 113px, and the ring is about 112px deep, so the target is larger than 44px by 44px. The wedge and the matching row select the same choice.

List, under the circle: a radiogroup. One row per offered space. Row height 48px, gap 4px. Six rows are 312px. Eight first-turn rows are 416px. The panel grows. If the side column is short, the list scrolls and the circle stays pinned. Columns inside each row, left to right: a 36px step cell, an 8px gap, the name (flexible, two lines), an 8px gap, an 88px cost cell, an 8px gap, and a 96px state cell. The state cell is empty when the row is payable. It says "cannot pay" when disabled for the actor, or "selected" when that row is the pending choice.

Buttons in the Swiss Bank block: each at least 168px wide and 44px tall, 8px apart, side by side. "Move here" is a single button under the list, 352px by 44px, and it sits above the Swiss Bank block.

Type: names 14px on 18px, neighbor phrase 12px on 16px, headings 16px, the first-turn sentence 14px. Tabular figures for steps and costs. Focus is a 2px outline, not a color change by itself.

The printed map wheel is not given a hit target. Its accessible name is "Rondel position only. Choose on the action rondel."

## Label placement

No label is rotated. Not on the radius, and not on the tangent. The photograph does that. This control does not.

The space name exists only in the horizontal row, in screen axes. Inside a wedge, the only type is an upright step numeral, "1" through "6", 14px, baseline horizontal, centered in the wedge. The current wedge, when the octagon is already on the wheel, shows the upright word "now" and no numeral. The unreachable seventh wedge shows neither. On the first turn every wedge shows an upright short name of one word, still horizontal, and the full neighbor phrase stays in the row. "Production" and "Maneuver" inside those wedges are not enough to tell the twins apart, so the row is the place the neighbor phrase is required, and the wedge's accessible name repeats the full row text.

Color may distinguish neighboring wedges, including the two that share a name, but a color is not the name. Do not rely on it for Import versus Taxation, or for the two Production spaces, or for the two Maneuver spaces. Do not trace the photograph.

## Worked actor view

Factory, power factor 0, personal cash 1 million, actor's own screen. Public opponents do not see the last column's refusal.

1. Production, after Factory. 0 million. Payable. Does not cross Investor.
2. Maneuver, before Investor. 0 million. Payable. Does not cross Investor.
3. Investor. 0 million. Payable. Land.
4. Import. 1 million. Payable. Pass.
5. Production, after Import. 2 million. Cannot pay. Pass.
6. Maneuver, before Taxation. 3 million. Cannot pay. Pass.

If this actor selects Import and commits, a Swiss Bank holder may force the stop. The stop lands on Investor, costs 0 million, and pays interest. If no holder forces, the nation goes to Import, the government pays 1 million to the bank, and the pass runs Investor steps 2 and 3 after Import, unless a variant or a 25-point Taxation rule says otherwise. Import is not Taxation, so the 25-point skip does not apply to this row.

## Not decided here

This note does not lay out Factory, Production, Import, Maneuver, Investor, or Taxation after the octagon has stopped. Those remain the plan's later prompts. It does not change who may add cash to a treasury, and it does not show private cash on a shared control.
