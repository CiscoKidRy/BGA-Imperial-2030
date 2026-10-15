# Counsel: investor panels and private cash

Date: 2026-10-15. Source: `grok/ui-design-2026-10-15.md`. This note does not edit that plan. Players are investors, 2 to 6. Nations are not panels. There is one panel per investor, never six empty seats padded in.

## Summary

1. Each investor panel is face up for bonds, nation flag cards, the Investor card, and a Swiss Bank, in that order, for every viewer including spectators.
2. Bonds are grouped by nation in tray order (Russia, China, India, Brazil, United States, Europe), skipping nations with none, and each bond shows price then interest, plus the nation price sum that decides government.
3. An opponent panel, and a spectator panel, always shows one cash chip reading Private, same size whether the stack is 0 or not, with no number, empty mark, tooltip, aria value, or cash field in the DOM.
4. The owner panel uses that same chip but prints the million total, and only that client receives the integer.
5. The owner alone gets one Add control per nation they govern; opponents never get the control, and it cannot pay another player, the bank, or a nation they do not govern.
6. The log records the payment amount, source, and destination, and it never prints remaining private cash or whether cash is zero.
7. Unaffordable bonds are dark only on the owner's prompt, so other clients cannot infer the cash ceiling from which choices are dim.
8. Seat numbers are fixed and clockwise; Swiss Bank asks are numbered from the Investor-card holder, and a battle ask names the nation on that government's panel.
9. The player whose decision it is is marked Deciding; later people in that same ask are marked Waiting with an index; panels are not grayed merely for waiting.
10. When a scoring marker reaches 25, every panel and one log entry reveal cash, because cash scores, and earlier replay states still omit it.
11. The desktop side column is 280 px outer and 248 px inner, with a fixed 96 by 28 px cash chip.
12. Mobile is one stacked column of full-width panels above the map, including below the 490 px breakpoint where two panel columns are dropped.
13. A 36 px sticky strip names the current decider so a six-player stack does not hide whose turn it is.
14. Nation marks are a color chip plus RU, CN, IN, BR, US, or EU, with explicit text colors so China yellow and India black survive dark mode.
15. Changing the Studio view from one test player to another clears the previous cash integer before drawing the next private view.

## Face-up block

The same block is drawn for the owner, opponents, and spectators. Absence of a card is public. Absence of cash is not, so these rules are not the same.

Top to bottom under the framework name row:

1. Seat line. Text: `Seat 2 of 6`. The number is clockwise seating from setup and does not move when the Investor card passes.
2. Decision line, only while this player is in the current ask. See below.
3. Bonds. A heading `Bonds` is always present so a player with no bonds still occupies the same kind of row (`No bonds`), which is public and is not a signal about cash. Each nation the player holds is a group. Header: color chip, two-letter code, name, and `prices 15` (sum of purchase prices in that nation). One line per bond: `price 12 · interest 5`. Price is first because the purchase-price sum, not interest, is government and the end-game tiebreak. Do not merge different bonds into one unlabeled total. Do not require hover. Tooltips are not available on touch.
4. Nation flag cards held, in the same nation order. These are government cards, not map flags. A 2-player panel must fit three; a 3-player panel must fit two; 4 to 6 usually show one, or none when the card is in the bank. No empty flag slot is drawn for a card the player does not hold.
5. Investor card, only if this player holds it. One labeled chip: `Investor`.
6. Swiss Bank, only if this player holds it. One labeled chip: `Swiss Bank`. A player with no nation has one. It is removed from the panel when they gain a nation. Do not keep a blank Swiss Bank slot.

Nation chips use the board colors (Russia purple, China yellow, India black, Brazil green, United States red, Europe blue) plus the letters RU, CN, IN, BR, US, EU. India has a light border and light lettering on the black chip. China uses black lettering on yellow. Do not use flag emoji or images copied from the publisher.

## Opponent panel and owner panel

Personal cash is the only hidden amount. Opponents must not learn the number and must not learn whether it is zero. Spectators use the opponent panel until the game-end reveal. Hiding with CSS is not enough: the public payload, the spectator gamedatas, and every replay step before the end omit both the integer and any empty-or-not flag. A notification that the client ignores is still a leak if the integer was in it.

Shared cash chip, both panels: 96 by 28 px, centered label, neutral fill `#d8d8d8`, text `#222222`, in light and dark mode. It does not change height, width, color, or animation when cash changes. There is no bill stack, no digit count, no class name such as `cash-empty` or `cash-positive`, and no sound that differs for zero.

Opponent and spectator chip text is always `Private`. The accessible name is `Personal cash, private` and carries no value. The row is present from setup through the last moment before scoring, including when the owner has 0. The Add control is not in this DOM.

Owner chip text is the total, such as `13 million` or `0 million`. The accessible name includes that total. Only the owning client receives it, on the private channel. The chip stays 96 by 28 px during play, which fits `37 million` (the largest setup figure). Growth is allowed only at the end reveal, and then for every panel at once.

The owner's panel may be taller by the Add row. That extra row is government, which is already public via the flag cards, and other clients do not render it. Panel sort order is seating order, never cash order.

Switching the active test player in Studio destroys the previous cash text node before the next private total is drawn.

## Add personal cash

On the owner panel only, under the cash chip: one button per nation that player currently governs, labeled `Add to China` (nation name). No button for a nation they do not govern. No button on a Swiss Bank holder's panel. No button that pays another investor, pulls money out of a treasury, or pays the bank. Rondel fees, bond purchases, and interest cover stay on their own prompts; they are not this control.

The amount is a positive integer in millions, at least 1, at most that player's current cash. The server rejects a non-integer, a zero, an over-spend, a nation the caller does not govern, and a confirm while another player's ask is unresolved. The client may cap the field from the owner's private total. That cap is not sent to anyone else.

If the owner has 0 and still governs a nation, the buttons remain on the owner panel. Submit does nothing until the amount is at least 1. There is no helper text `you have no money`, because that sentence must never be copied into a public log. Opponents do not see the buttons appear or disappear with the balance.

The public result is notes of the stated amount moving to that nation treasury. It is not a shrinking pile on the player panel.

## Log

Every rule payment is logged. Remaining private cash is not. Forbidden in the log, the animated log, and replay before the end: a remainder, a new total, the word zero applied to private cash, and a phrase such as `cannot afford` or `cash empty`.

Acceptable shapes:

- `Alex pays 4 million to the China treasury.`
- `Alex pays 3 million to the bank (rondel).`
- `The bank pays Alex 2 million (Investor).`
- `China pays Alex 4 million interest.`
- `Alex forgoes 4 million China interest.`
- `Alex pays 5 million of Sam's China interest.`
- `China pays Alex 2 million (tax bonus).`

Interest paid to a player, the Investor's 2 million, and the tax bonus increase private cash. Log the amount received. Do not append `now has`. A voluntary add uses the first shape and names the treasury. Factory, import, and soldiers' pay are treasury and bank transactions; they do not mention private cash.

Public notification arguments carry amount, from, to, nation, and reason. They do not carry `cash_after`. A private notification to the owner may carry `cash_after` for that counter only.

Affordability: bonds the acting player cannot buy are dark on that player's prompt only. Other clients see the legal catalog without a broke mask. Choosing a cheaper bond is public after it happens; the dim state before the choice is not.

## Seating and several people waiting

Desktop panels stack top to bottom in seat order. Mobile uses the same order. The Investor card on its holder's panel is the start of clockwise Swiss Bank order. Seat 1 is not implied to be that holder.

When one player alone is deciding (their nation turn), that panel's decision line reads `Deciding` plus the nation. The status line remains the sentence the plan already calls for. This column repeats who, so the side stack agrees with it.

When several people are in one ask:

- Swiss Bank force, or Swiss Bank investment: order is clockwise from the Investor-card holder, skipping anyone who does not hold a Swiss Bank. Investment also skips the Investor-card holder, as the plan's investor section does. Each involved panel reads `Swiss Bank 1 of 3` and either `Deciding` or `Waiting`.
- Battle: the ask is by nation, then shown on that nation's government panel. Text: `Battle 2 of 4: India`. A player who governs two nations in the same sea can be in the queue twice. Those asks stay separate.
- Anyone not in the queue has no decision line. Do not gray their panel. Graying reads as out of the game and hides face-up bonds. Disable-panel gray is only for a player who has left the table.

A sticky strip, 36 px, sits at the top of the desktop column and at the top of the mobile stack: `Dana is deciding · Swiss Bank 2 of 3`. It names the player and the ask. It does not name cash. The full panels remain in seat order underneath; the strip does not reorder them.

The Add buttons do not confirm while this strip names someone else.

## Game end

When any nation marker reaches 25, cash stops being secret because it scores 1 point per million. One public notification reveals every investor's final cash. Every panel, including spectators, replaces `Private` with the million figure. The log entry is a single list, for example `Final cash: Alex 4, Dana 0, Sam 11 (million).` A zero in that entry is allowed. It is not allowed before this entry.

The score breakdown on the panel is interest times that nation's power factor, then cash points. The tiebreak stays the plan's purchase-price credit in the highest-power nation, then the next. The nation that reached 25 is named on the status line and is not labeled the winner merely for arriving.

Replay of earlier moves still has no cash integer. The end notification is the first public one that contains it. Panels update together, not one secret at a time ahead of the others.

## Widths

Desktop side column, `desktop_version`:

| Piece | Width or size |
| --- | --- |
| Column outer | 280 px |
| Inner content, after 16 px padding each side | 248 px |
| Minimum inner before type drops to 12 px | 220 px |
| Cash chip | 96 by 28 px |
| Bond line | 22 px high, 13 px type |
| Nation group header | 20 px high |
| Flag card | 40 by 26 px, gap 8 px, three across (136 px) inside 248 px |
| Investor and Swiss Bank chips | 96 by 28 px |
| Add button | 72 px min, wraps under the chip inside 248 px |
| Sticky decider strip | 36 px high, full column width |
| Custom block min-width | none that would force the page sideways |

The framework name row stays above this block. Six panels scroll inside the side column. Type does not shrink below 12 px to keep all six on screen. Bonds stay inline at six players; they are not moved to a hover-only layer.

Stacked mobile, `mobile_version`, one column above the map at every width, not two columns:

| Piece | Width or size |
| --- | --- |
| Breakpoint | under 490 px, BGA already leaves the two-column panel layout; this game stays one column above that too |
| Panel outer | 100 percent of the panel strip |
| Inner padding | 12 px each side |
| Target inner width | viewport minus 24 px |
| Minimum inner before framework scale | 300 px |
| Cap on very wide tablets | 420 px, centered, so a bond line does not stretch apart |
| Cash chip | same 96 by 28 px, one line, does not wrap |
| Bond line | may wrap interest under price below 360 px viewport; the cash row still does not |
| Sticky decider strip | 36 px, pinned over the stack |
| Flag row | same 40 by 26 px cards, wraps after three |

The cash row is the one row that is not allowed to change height between empty and full, owner and opponent, or 2 and 6 players. Bond groups may grow the panel. That growth is public information.

## Out of scope

This note does not change map, rondel, tax chart, nation trays, or setup deals. It does not add player-to-player payments. It does not put publisher art in the panel. The plan file is left as it is.
