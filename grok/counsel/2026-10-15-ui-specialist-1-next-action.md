# Next-action graphics

Date: 2026-10-15. Specialist review of turn guidance only. The screen is not built. This note does not change the plan file. It specifies the graphic a developer can build for "what the player does next."

The plan is right that one status line carries the decision, and that legal places are marked while unaffordable ones go dark. That line is not yet a component. There is no size, no contrast, no separation of player and nation, and no rule for prompts that must not cover the map. Build the system below. Do not add a second instruction somewhere else on the map.

## One banner

One element, `#next-action`, in normal flow at the top of the play area, directly under the framework action bar, `margin-top: 0`. It pushes the map down. It is not `position: fixed` over the map, and it has no scrim. The map stays at full brightness.

The framework title (`pagemaintitletext`, filled from the state description) and this banner show the same sentence string. They must not use different words. The chips, the step strip, and the buttons exist only in `#next-action`. Do not paint the sentence a third time on the map, the trays, or a floating chip.

Background `#1A1814`. Text `#F4F0E6`. That pair is 15.58:1. Padding `12px 16px`. Minimum width 540px. Type is the framework sans, not a display face. No emoji, no dingbats, no flag glyphs, no check or cross characters.

### Row 1, the four facts

One horizontal row, `min-height: 80px`, `align-items: center`, `column-gap: 8px`. Below 740px the chips wrap onto their own line and the sentence takes the full width under them. Type does not drop below 16px. The row grows with the sentence. It does not cover the map.

| Slot | Size | Paint |
| --- | --- | --- |
| Who | height 28px, max-width 180px, padding 0 10px, type 16px / 600 | Name in `#F4F0E6`. A 12×12px square of the player color, 1px solid `#F4F0E6`, sits 8px before the name. The name itself is never set in the player color. |
| Nation | height 28px, min-width 72px, padding 0 10px, type 14px / 600 | Word plus a 12×12px swatch. See the swatch table. |
| Phase | height 28px, min-width 88px, padding 0 10px, type 14px / 600 | `#F4F0E6` on `#3A3428` (10.84:1). |
| Sentence | flex 1, 16px / 400, line-height 22px, max 2 lines | `#F4F0E6` on `#1A1814` (15.58:1). This is the only instruction. |
| Buttons | height 44px, min-width 96px, type 14px / 600, gap 8px | Framework button colors only: primary, secondary, alert. Do not tint them to a nation. The alert button is last and has an extra 16px of space before it. |

Who and nation are always separate. The banner never says that China must act when a player must act. If the name is longer than the chip, truncate with an ellipsis and put the full name on the control's title. Focus ring for any control inside the banner: 2px solid `#E8A317`, offset 2px. `#E8A317` on `#1A1814` is 8.17:1.

Nation swatches. Text contrast is on the chip fill. Do not lighten these.

| Nation | Fill | Text | Contrast |
| --- | --- | --- | --- |
| Russia | `#6B4C9A` | `#F4F0E6` | 5.90:1 |
| China | `#F2C200` | `#1A1814` | 10.54:1 |
| India | `#1A1A1A` | `#F4F0E6` | 15.29:1, plus a 2px solid `#F4F0E6` border so the chip is visible on the banner |
| Brazil | `#1F7A3A` | `#F4F0E6` | 4.73:1 |
| United States | `#C0392B` | `#F4F0E6` | 4.78:1 |
| Europe | `#1E5AA8` | `#F4F0E6` | 5.99:1 |

Phase words, exact: `Setup`, `Rondel`, `Factory`, `Production`, `Maneuver`, `Investor`, `Import`, `Taxation`, `Game over`.

The sentence is an `aria-live="polite"` region. When buttons appear or the sentence becomes a prompt, switch that region to `assertive` for that update only.

### China example, verbatim

Actor is the government player (who chip). Nation chip: `China`. Phase chip: `Rondel`. Sentence, idle, before a space is selected, characters exact:

`On Investor, factor 2, choosing Taxation (4 spaces, cost 3) or Factory (5 spaces, cost 6).`

Do not add "million" inside that sentence. A separate 12px label, `#E6E0D4` on `#1A1814` (13.49:1), sits at the end of the chip row only while a rondel cost is on screen: `Unit: million`. Screen-reader names append the unit: `Taxation, 4 spaces, cost 3 million`.

This sentence names the two paid spaces in the example. It does not mean the other legal spaces are hidden. Draw them with the outline rules below. From Investor, clockwise, at factor 2:

| Spaces | Space | Tag | Draw |
| --- | --- | --- | --- |
| 1 | Import | `1 space, cost 0` | legal |
| 2 | Production | `2 spaces, cost 0` | legal |
| 3 | Maneuver | `3 spaces, cost 0` | legal |
| 4 | Taxation | `4 spaces, cost 3` | legal |
| 5 | Factory | `5 spaces, cost 6` | legal |
| 6 | Production | `6 spaces, cost 9` | legal, or disabled if that player cannot pay |

Investor itself is not a destination. Plate `Already here`. No choice outline. Not dark.

The Swiss Bank stop does not appear in this example. The marker is already on Investor. A stop is only when the chosen move would pass Investor.

After the player selects a space, replace the sentence. Do not keep the idle sentence up.

- Taxation selected: `Confirm Taxation (4 spaces, cost 3).` Buttons: `Confirm move` (primary), `Cancel` (alert).
- Factory selected: `Confirm Factory (5 spaces, cost 6).` Same buttons.

Cancel restores the verbatim sentence and the 3px outline. Confirm is the commitment. There is no undo button on this banner.

Waiting clients use a different sentence, still one sentence, chips unchanged: `Waiting for {name}: China is on Investor, factor 2.` After a selection: `Waiting for {name}: China may move to Taxation (4 spaces, cost 3).` or the Factory twin. They do not get the buttons.

## Step strip

Second row inside `#next-action`, only while the action has steps. `margin-top: 8px`. `list-style: none`. Steps are not buttons and are not in tab order. A 12×2px bar, `#8A8478`, sits between steps. No chevron.

Each step is `height: 32px`, `min-width: 96px`, padding `0 10px`, type 14px / 600. If a translated label would wrap, replace the row with `2 of 3` plus the current word, and four-or-fewer 10×10px squares (gap 4px). Do not shrink the type.

| State | Paint | Extra word |
| --- | --- | --- |
| Done | text `#E6E0D4` (13.49:1), no fill | `Done` at 12px before the label |
| Current | text `#F4F0E6` on `#3A3428` (10.84:1), 4×32px left bar `#E8A317` | accessible name starts `Current step` |
| Upcoming | text `#8A8478` (4.77:1 on `#1A1814`) | none |
| Skipped | same `#8A8478`, plus a 1px strike in `#8A8478` | `Skipped` at 12px before the label |

`#5C574E` on `#1A1814` is 2.47:1. Do not use it. Do not go darker than `#8A8478` for text on this background. The strike is never the only signal.

Labels, in order:

- Maneuver: `1 Fleets`, `2 Armies`, `3 Flags`.
- Investor, when the marker lands: `1 Interest`, `2 Investor card`, `3 Swiss Bank`.
- Investor, when the marker passes that space: step 1 is `Skipped`. Steps 2 and 3 still show. Do not renumber them.
- If the landed action is the Taxation that reaches 25, Investor steps 2 and 3 are `Skipped`. Interest is not shown, because the marker did not land on Investor.
- Taxation: `1 Pay in`, `2 Upkeep`, `3 Bonus`, `4 Power`. All four are visible before commit. None of them is a click. Sentence: `Check the four taxation results, then commit.` Button: `Commit taxation` (primary). The tax chart column highlight stays on the board. The banner does not repeat the chart.

Canal, battle, and hostile-or-friendly keep the Maneuver strip on the current step. They do not add a phase called Battle.

## How choices are drawn

Three drawings. Color is never the only difference. Outline style, the plate text, and the hit target differ too.

Every legal outline is a double stroke: 3px solid `#F4F0E6`, then 1px solid `#1A1814` outside it, 2px outside the region. The light stroke alone fails on China yellow (`#F4F0E6` against `#F2C200`). The hairline `#1A1814` on `#F2C200` is 10.54:1, so the hairline is mandatory on every legal outline, including seas.

### Legal and payable

- Double stroke as above. Pointer cursor. `min-width` and `min-height` 44px. If the printed region is smaller, the hit target is still 44×44px.
- Cost tag always visible, not hover-only: height 20px, padding `0 6px`, type 12px / 600, `#1A1814` on `#F4F0E6` (15.58:1), 4px above the outline. Wording matches the banner parenthesis, for example `4 spaces, cost 3`.
- Hover and keyboard focus use the same paint: stroke becomes 4px. No hover-only fact.
- First tab stop is the first legal space clockwise, then `Confirm move`, then `Cancel`.
- Selecting a space thickens the stroke to 4px solid `#E8A317` with the same 1px `#1A1814` hairline, and adds a plate `Selected`. The accessible name gains `selected`.

Factory cities that can be built: same outline, tag `cost 5`. Import destinations: same outline, and the sentence carries the running total: `Import: choose a province and a unit. Cost so far: {n}.` Button `Done importing` (primary) when the player stops before three. Production is not a destination click. Open factories get the legal stroke and a plate `Builds 1`. The commit button is `Commit production`.

### Disabled: exists now, cannot be taken

Use this for a space, bond, city, or unit the action could use, when the cost cannot be paid or the supply is empty. This is the plan's dark choice. It is not illegal.

- Veil `rgba(26,24,20,0.72)` over that target only.
- 3px dashed `#F4F0E6`, plus the 1px `#1A1814` hairline.
- `pointer-events: none` on the click action. `aria-disabled="true"`. It stays in tab order so the reason is read. It does not activate.
- Reason plate always visible, including on touch: height up to 32px, max-width 160px, type 12px / 600, `#F4F0E6` on `#1A1814` (15.58:1). Two lines maximum.

Plate words:

- Rondel fee the acting player cannot pay: `Costs 9 million. You cannot pay it.` Spectators see `Costs 9 million.` and the dashed stroke. No plate and no sentence may show a personal-cash total, or say that the stack is empty.
- Treasury cannot pay a factory or an import: `Costs 5 million. Treasury is short.` Treasury cash is public, so the shortfall may name the treasury. It still must not name personal cash.
- Bond the acting player cannot pay: `You cannot pay it.` Spectators see the bond dark and the price, with no personal total.
- Empty supply: `No armies left.` or `No fleets left.` or `No flags left.` or `No factories left.`

During Maneuver, an empty supply does not replace the step sentence. Movement is not a purchase. The empty-supply sentence is for Factory, Production, Import, and flags.

### Illegal: not a choice this step

No stroke, no veil, no plate, no hit target, not in the accessibility tree as a control. Leave the region at its normal map color. Do not draw an X. Do not turn it red. Red is reserved for the alert button.

Counterclockwise rondel spaces, the space just left, a city of the wrong color, and a province with a standing hostile army are illegal, not dark.

A click that hits the map and misses every target does not open a dialog. For 2 seconds the sentence becomes `Not a legal choice.` and then the previous sentence returns. The clicked region, if it has a node, shifts 4px horizontally for 150ms and returns. `prefers-reduced-motion`: no shift, sentence only.

## Prompts that must not hide the map

These four replace the sentence and add buttons in the same banner. No modal, no dimmed page, no card in the center, no second dock on the sea. The map can still pan. The step strip stays. Outlines mark the places that matter. Everything else stays unmarked, not darkened.

Button labels are the framework buttons. Primary moves forward. Alert refuses or cancels. Secondary is the other legal answer when neither answer is a cancel.

### Swiss Bank stop

Asked only when the move would pass Investor, and only of Swiss Bank holders, one at a time, clockwise from the Investor card. Not this China example.

- Who chip: that holder. Nation chip: the nation that is moving. Phase: `Rondel`.
- Chip at 12px on `#3A3428`: `Swiss Bank 1 of 2`, using the real counts.
- Sentence: `{name}, stop {nation} on Investor?`
- Buttons: `Stop on Investor` (primary), `Let it pass` (secondary).
- Investor has the legal outline. The selected destination keeps `Selected` and is not committed. Later holders are not named in the banner.

### Canal yes / no

- Phase stays `Maneuver`. The current step stays current.
- Sentence: `{name}, allow {nation} to cross Suez?` or `Panama` in the same sentence.
- Buttons: `Yes, allow` (primary), `No, refuse` (alert).
- The two seas and the moving piece get the legal outline. The canal is not covered by a panel.

### Battle demand

Mover first. If the mover does not demand, each other nation in that region is asked in turn. Do not ask the mover twice.

- Sentence: `{nation} can fight in {region}. Demand a fight?`
- Buttons: `Demand a fight` (primary), `Do not fight` (secondary).
- The region has the legal outline.
- If they demand and more than one opposing unit is there, clear the buttons and set the sentence to `Choose one opposing unit to remove.` Only those opposing units get the legal outline. Confirm is the click on one unit, then buttons `Remove this unit` (primary) and `Cancel` (alert).

### Hostile or friendly

- Sentence: `Set this army in {province} to hostile or friendly.`
- Buttons: `Hostile` (secondary), `Friendly` (secondary). Neither is primary. Neither is alert.
- The army and the province get the legal outline.
- After the click, a 20px plate on the army reads `Hostile` or `Friendly` in 11px `#1A1814` on `#F4F0E6`. The figure may stand or lie down as well. The plate is required, because posture at 32px is not enough.
- Last open factory, that province only: do not show the buttons. Sentence: `This army stays friendly because that factory is the last open one.` Plate `Friendly`. The turn does not wait for a click. With motion allowed, show that sentence for 400ms, then continue. With reduced motion, keep it until the next banner update. The log keeps the line.

Flag placement uses this same banner, not a dialog. When a new exclusive occupation cannot take a flag because all 15 are out: `That flag is removed and not replaced.` No buttons. When one of those flags is free again: `Place this flag in {region}?` with `Place flag` (primary) and `Decline` (secondary).

## Empty, waiting, game over

The banner does not unmount. The layout must not jump because the band disappeared.

### Empty, before the first turn

Who: `No one`. Nation: `None`. Phase: `Setup`. Sentence: `Choose the player count and the deal, then place both markers.` No step strip. No outlines. No buttons until those choices exist. A nation with no government during play is not an empty screen. In the base deal the pawn moves on, and the banner never asks anyone to act for that nation. Who on that tray may read `No government`. The banner does not stop there.

### Waiting

Same banner. Add a chip, height 28px, padding `0 10px`, type 12px / 600, text `#E6E0D4`, 2px solid `#E6E0D4`, transparent fill. The word is `Waiting`. A 8×8px square of `#E6E0D4` sits 8px before the word. It may pulse opacity from 1 to 0.45 over 1.2s. Reduced motion: static square. No spinner glyph.

The actor does not see the Waiting chip or the waiting sentence. Everyone else does. Outlines, tags, and disabled plates stay visible to everyone. Only the actor gets buttons, pointer events, and tab stops. Do not write a personal-cash total into a waiting sentence.

Automatic stretches use who `No one` and no Waiting chip. Government check sentence: `Checking who governs {nation}.` Taxation while it is resolving with no commit left: `Taxation is resolving.` The four steps move from current to Done as each result is shown. Do not animate them one payment at a time beyond those four labels.

### Game over

Who: `No one`. Nation: the nation that reached 25, in that nation's chip. Phase chip swaps to fill `#F4F0E6`, text `#1A1814`, word `Game over`. Sentence, one sentence: `Game over: {nation} reached 25.` Example: `Game over: China reached 25.`

Remove every outline, veil, and plate in the same update. No buttons. No step strip. The scoring breakdown stays in the log. The banner does not list it, and it does not say that the nation which reached 25 is the winner.

## Build checks

- Idle China screen shows the verbatim sentence, who and China and Rondel as three chips, and six clockwise tags, with Investor marked `Already here`.
- A dark sixth Production has no click, a dashed stroke, and no personal-cash number.
- An illegal region has no stroke. Clicking empty map sets `Not a legal choice.` for 2 seconds.
- Suez, a battle demand, a hostile-or-friendly choice, and a Swiss Bank stop each change the sentence and add two 44px buttons without dimming the map.
- The last-open-factory province has no Hostile button.
- Taxation shows four steps and one `Commit taxation` button before anything is committed.
- Setup, waiting, and game over use the sentences in this note.
- Contrast pairs above stay at or above 4.5:1 for text and 3:1 for strokes. Brazil and the United States chips are already close. Do not lighten them.
- No emoji, no unicode icon, no modal, no second instruction string.
