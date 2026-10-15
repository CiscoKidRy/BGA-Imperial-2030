# Counsel: treasury tables, 2026-10-15

Specialist note on the six nation trays, the bond dialog, the tax chart, and the scoring track. Source: `grok/ui-design-2026-10-15.md` and the unpunched sheet `reference/bgg/images/602507.jpg`. This note does not change the plan. No game fact below is added beyond those two sources. The sheet photo shows the United States, Russia, and India blocks; each block is the same nine faces. The plan uses that ladder for every nation.

## Fifteen-line summary

Six trays sit in one row under the map, left to right: Russia, China, India, Brazil, United States, Europe.
That is turn order, not the sheet order. Image 602507 shows United States, then Russia, then India.
Each tray is one ledger: labels left, integers right, tabular figures, and the same rows on every tray.
The rows are government, credit, interest, treasury, power and factor, the top bond, then factories, armies, fleets, and flags.
Government is the player name, or the words "no government" when that nation has issued no bond.
Credit is the sum of purchase prices. It is the only figure that decides government, and it is the strong row on every tray.
Interest is a smaller row, labeled as not used for government, and the turn highlight never lands on it.
Treasury cash is public, as a plain integer of millions. An empty treasury is 0. No credit is an em dash, not 0.
The pile shows the lowest remaining price on top, with that card's interest and price, and a count that includes the top card.
Piece rows use two right-aligned subcolumns, on the board and left in supply. Factories are brown and light blue, not a fraction of 12.
The active tray takes the turn pawn and a color outline. That nation's scoring-track cell is marked for the whole turn.
The tax chart is eleven equal centered columns. The bonus row ends 5, 5. One column is highlighted only while that nation taxes.
A revenue of 7, 9, or 17 uses the rightmost header at or below it, and a caption under the chart names that header.
Cell 0 of the scoring track has no printed factor. x0 sits over points 1–5 only. At power 0 the tray factor is blank.
The bond dialog always lists nine bonds, interest 1 through 9. Price stays printed. An upgrade shows only the price difference. A bond the player cannot buy stays visible, dark, and not clickable, with a reason that does not reveal private cash to anyone else.

## Tray order and chrome

The six trays are equal width and one row, under the map. Left to right: Russia (purple), China (yellow), India (black), Brazil (green), United States (red), Europe (blue). Do not sort them by cash, power, or the sheet. On a narrow screen they wrap or scroll; Russia stays first.

The printed bond says "USA". The tray title says "United States", which is the name in the plan.

Every tray uses a light ledger ground and dark numerals, so the columns match. Nation color is a stripe at the top, not a fill behind the numbers. Yellow and black are stripes only; they must not become the text color.

The wooden turn pawn sits on the active tray, with an outline in that nation's color. The other five trays stay fully readable. Treasury cash is public, so an inactive tray is not dimmed.

## Ledger alignment

One shared row grid. A label in one tray lines up with the same label in the other five, so credit can be read across as a single line. Same for interest, treasury, and power.

Inside a tray the labels are left-aligned and the integers are right-aligned. Use tabular lining figures. No leading zeros, no decimals, no thousands separator. The unit is a million. Put "million" in the label, not after every number.

There is no minus. A treasury does not show a negative balance. The plan stops soldiers' pay when the treasury is empty.

| Row | Label, left | Value, right | Format |
| --- | --- | --- | --- |
| 1 | Government | player name, or no government | text, not a number |
| 2 | Credit | sum of purchase prices held | integer; em dash if no bond has been issued |
| 3 | Interest | sum of interest on those bonds | integer; em dash if no bond has been issued; smaller type |
| 4 | Treasury | public cash | integer; 0 when empty |
| 5 | Power | scoring-track position, 0 through 25 | integer |
| 5b | Factor | printed factor for that position | x0 through x5, or blank when power is 0 |
| 6 | Top bond | lowest remaining certificate | interest, then price, then how many are left |
| 7 | Factories | on the board | brown count, then light-blue count |
| 8 | Armies | on the board, and still in supply | two integers |
| 9 | Fleets | on the board, and still in supply | two integers |
| 10 | Flags | on the board, and still in supply | two integers |

Credit is the strong row on every tray, all the time, not only on the active nation. Under the credit value, the words "decides government". Under the interest value, the words "not used for government". The two numbers are never adjacent without those labels, and they never share one unlabeled column.

A tie does not rewrite the government name. The plan keeps the current government when the high credit is only tied, and it uses seating from the Investor card when several players tie for a new high. The tray shows the name that rule produced. It does not break a tie by interest.

When no bond has been issued, the government line is exactly "no government". Credit and interest are em dashes. A zero there would look like a player on zero credit. Treasury may still show 0.

## What credit includes

Credit is the sum of the printed purchase prices of the bonds that player currently holds in that nation. It is not the interest sum. It is not the cash the player has paid over the game. An upgrade returns the lower bond to the pile, so that old price leaves the sum and the new printed price enters it. The difference just paid is not a second credit line on top of the old price.

The same credit figure is the one the plan uses for the end-game tiebreak. The tray does not keep a second "tiebreak" number.

## Bond pile

The tray shows a pile, not all nine faces. The lowest remaining price is on top. On this ladder the lowest price is also the lowest interest: 2, 4, 6, 9, 12, 16, 20, 25, 30, with interest 1 through 9.

The top line reads interest, then price, in that order, which is the order printed on the card (interest at the upper left, price at the upper right). A count beside it includes the top card, from 1 to 9. An empty pile says "none", not 0, so it is not read as a bond priced at 0.

Do not add the remaining prices into a sum next to the treasury. That sum is not cash.

The pile order is stock display only. The buyer may choose any bond still in the pile, not only the top card. The dialog, not the pile, is the choice.

Supply ceilings from the plan, so the "left" column has a fixed meaning: armies 10 China, 6 United States, 8 each other nation; fleets 6 China, 10 United States, 8 each other nation; flags 15 per nation. Factories are not painted in the nation color. The bank holds 12 brown and 12 light blue. The tray counts how many of each that nation has built. It does not show a fraction of 12.

When armies, fleets, or flags left are 0, print 0. That zero is a real empty supply. Do not replace it with a blank.

## Active turn

On the active nation's turn, mark only these:

- The turn pawn and the outline on that tray.
- That nation's marker cell on the scoring track, for the whole turn.
- One tax-chart column, and only while that nation is taxing.

Do not bold the active interest row. Do not change any numeral's weight because the turn changed. Credit stays the strong row on the inactive trays as well, so a player can read who governs another nation during the turn.

## Tax chart

Compact table, row labels outside the grid, eleven equal columns, values centered. Headers and cells, from the plan:

| Tax | 0–5 | 6 | 8 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 18+ |
| Bonus | 0 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 5 |
| Power | 0 | +1 | +2 | +3 | +4 | +5 | +6 | +7 | +8 | +9 | +10 |

The bonus row ends 5, 5. Do not print 10, and do not add those two cells.

There is no column for 7, 9, or 17. Highlight the rightmost header that is less than or equal to the revenue. Tax 7 highlights 6. Tax 9 highlights 8. Tax 17 highlights 16. Tax 0 through 5 highlights 0–5. Tax 18 or more highlights 18+.

The highlight is one full-height stripe across Tax, Bonus, and Power. A caption under the table states the revenue and the header used, so a skipped number is explained: "9 uses 8".

Bonus is an integer of millions, with the unit in the row label. Power uses a leading plus except for the 0 in column 0–5, so those cells are not read as cash. The plus amounts are added to the scoring track. They are not the tray's factor.

In the tax-increase variant the printed bonus row does not change. The third octagon sits on the bonus row of the recorded column. The variant payment is a separate line, 1 million for each column moved right, and nothing if the marker moves left. That line is not written into the 5, 5 cells.

## Scoring track

One compact row of cells 0 through 25. Factor labels are a header over bands, not text inside the point cells.

| Points | 0 | 1–5 | 6–10 | 11–15 | 16–20 | 21–24 | 25 |
| Printed factor | (none) | x0 | x1 | x2 | x3 | x4 | x5 |

Cell 0 has the numeral 0 and no factor. x0 is centered over 1–5 only. Do not stretch x0 back onto 0.

The active column on this track is the single cell that holds the active nation's marker. Do not light the whole factor band. Nations that share a cell keep their own markers; the ring is on the active nation's marker.

In the tray, factor is blank when power is 0, because nothing is printed on that cell. When power is 1 through 5, the tray shows x0, because that label is printed over those boxes. The booklet's "factor is zero at the start" is not painted onto cell 0. End-game scoring may still multiply by zero without putting x0 in that cell.

## Bond dialog

One nation per dialog. The title is the nation name and either "Buy" or "Upgrade". Always nine rows, including bonds that cannot be chosen. Sort by interest ascending, 1 through 9. Do not copy the sheet's 3 by 3, which groups 7-8-9, then 4-5-6, then 1-2-3.

Faces, checked on 602507 for the United States, Russia, and India, and listed for every nation in the plan:

| Interest | Price (million) | Printed rate on the card |
| --- | --- | --- |
| 1 | 2 | 50% |
| 2 | 4 | 50% |
| 3 | 6 | 50% |
| 4 | 9 | 44% |
| 5 | 12 | 42% |
| 6 | 16 | 38% |
| 7 | 20 | 35% |
| 8 | 25 | 32% |
| 9 | 30 | 30% |

The action table has four columns. Interest and Price are right-aligned. "You pay" is right-aligned. Reason is left-aligned and takes the remaining width.

| Column | Alignment | What it shows |
| --- | --- | --- |
| Interest | right | 1 through 9 |
| Price | right | the printed price, always, even on an upgrade |
| You pay | right | the full price, or the price difference, or an em dash |
| Reason | left | blank when the row can be chosen; otherwise why not |

The printed rate stays on a card facsimile if one is shown. It is not a column in this table. The amount due is never price times rate, and never an interest minus another interest.

A new bond: "You pay" equals Price. The column does not say "difference".

An upgrade: the dialog names the bond being returned, by interest and price. "You pay" is the new price minus that price, and the cell says "difference". Price in its own column stays the printed price. Example from the ladder: return the price 9 bond (interest 4) for the price 16 bond (interest 6). You pay 7. The interest gap is 2 and is not the payment. A negative "You pay" is not shown. A row that is not a higher bond does not display a difference.

The confirm line repeats the "You pay" figure and the nation treasury: pay that many million into the treasury. On an upgrade it also says the lower bond returns to the pile. It does not repeat interest as the amount.

Rows that cannot be chosen stay in the list, dark but still legible, and they are not clickable. "You pay" is an em dash. The reason is specific:

- Held by another player: "held by" and that player's name. This is public.
- The certificate being returned: "your bond".
- Not a higher price while upgrading: "not an upgrade".
- The actor's cash does not cover the price or the difference: the actor sees "short" and the integer of millions. No one else sees that integer.

Personal cash is secret, including whether the stack is empty. The shortfall is drawn only on the acting player's dialog. Observers do not see which rows are unaffordable. The log records the purchase that was made. It does not list the rejected rows and it does not print the private balance.

The first bond of a nation that had none is a new-bond dialog: all nine are in the pile, "You pay" is the full price, and the government line can change from "no government" after the purchase. The dialog does not take the government by comparing interest.
