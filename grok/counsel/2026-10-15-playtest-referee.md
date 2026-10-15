# Playtest referee, game 5

Watched `http://127.0.0.1:8765/api/game/5?seat=0` from 11:58:12 to 12:10:28. No action was posted. No seat was played.

The log was only the setup line until 12:07:00. That is past the eight-minute mark, so the watch continued. It stopped at the ten-minute cap. A last read at 12:10:28 was unchanged. There is no line with "lands on" (zero, not two).

## What the log did

Three lines, still in Russia setup, waiting on Cy to buy or pass:

- "Experienced setup. Each player has 19 million. Russia is chosen first."
- "Ava buys Russia 2 million, interest 1."
- "Bo buys Russia 4 million, interest 2."

Ava (seat 0) chose first, then Bo (seat 1). The prompt at the end was Cy, Russia, Setup: "Waiting for Cy: Choose one Russia bond, or pass." Dee had not acted. No nation had a government on the board. No rondel space, tax, investor payout, or maneuver was logged.

## Player notes

Absent, checked at the start and again at 12:10:

- `2026-10-15-playtest-ava.md`
- `2026-10-15-playtest-bo.md`
- `2026-10-15-playtest-cy.md`
- `2026-10-15-playtest-dee.md`

## Checks

| Check | Result |
| --- | --- |
| Rondel moves are clockwise | Not reached. No rondel move was logged, so this is not a failure. |
| A first turn has no cost | Not reached. No nation has taken a first rondel turn. Not a failure. |
| Tax matches 0–5 bonus 0 power 0; 6 bonus 1 power 1; 11 bonus 2 power 4 | Not reached. No tax line. Not a failure. |
| Government follows purchase price | Not reached. The log never names a government. Not a failure. |
| Log does not print remaining personal cash | Pass. |

The only cash sentence is the opening line that each player has 19 million. That is the published experienced-setup amount for four players, not a balance after a purchase. The two buy lines name the bond price and its interest, not what the buyer had left. No later line prints a personal remainder.

Not scored as failures, because this test states them as limits: missing map borders, no convoy, no factory destruction, and a peace offer that does not ask each defender. None of those came up in the log.

## After the referee stopped

The four players kept going. A later read of the same game, after Ava and Bo had written their notes, had 40 log lines. The checks that were not reached at 12:10 had been reached:

- "Russia lands on Production." "Russia produces an army in Moscow." "Russia produces a fleet in Vladivostok." The first turn did not log a rondel payment.
- "Russia taxes 4. Soldiers cost 2. Bonus 0. Power +0, now 0." India logged the same tax line. Revenue 4 is the column whose header is 0–5. Bonus 0 and power +0 match that column.
- "A Russia fleet moves from Vladivostok to Sea of Japan." That is one of the named harbor exits.
- "Ava governs Europe." That followed "Ava buys Europe 2 million, interest 1." Dee had bought the Russia 9, Cy the Brazil 6, Bo the India 9, and Ava the China 9. Those are the highest purchase prices in those nations.
- "China treasury pays 1 million interest to Bo." The same entry pays 2 to Cy and 3 to Dee. The lines name the payment, not a remaining personal balance.
- The United States had no government and was skipped.

Ava's note and Bo's note were on disk by then. Cy's note and Dee's note were not. Ava had stopped on Europe's fleet step, so the table was waiting on a seat that was no longer acting.
