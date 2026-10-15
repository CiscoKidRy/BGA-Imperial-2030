# Bo, seat 1

Stopped after 20 of my actions. The phase was not "Game over". The last banner I saw was "Waiting for Ava: Move Europe fleets, or finish the fleet step. A fleet may stay." Actor was 0 and waiting was true, so I did not act. That seat was not moving, so I never reached 25 actions.

## Banner before each action

Each of these told me what to do.

1. Yes. "Bo, choose one Russia bond, or pass." buy:russia:4
2. Yes. "Bo, choose one China bond, or pass." buy:china:2
3. Yes. "Bo, choose one India bond, or pass. The booklet does not name who leads this nation. This test rotates the lead." buy:india:9
4. Yes. "Bo, choose one Brazil bond, or pass. The booklet does not name who leads this nation. This test rotates the lead." buy:brazil:4
5. Yes. "Bo, choose one United States bond, or pass. The booklet does not name who leads this nation. This test rotates the lead." pass
6. Yes. "Bo, choose one Europe bond, or pass. The booklet does not name who leads this nation. This test rotates the lead." pass
7. Yes. "First turn for India. The octagon is in the hub. Any of the eight spaces may be chosen. The move is not limited to six spaces, and it costs nothing." rondel:5
8. Yes. "Confirm Production, after Import. The first turn costs nothing." confirm
9. Yes. "Commit production: army in New Delhi, fleet in Mumbai." commit
10. Yes. "On Production, after Import, factor 0. Move clockwise 1 to 6 spaces. The first 3 cost 0." rondel:6
11. Yes. "Confirm Maneuver, before Taxation (1 spaces, cost 0)." confirm
12. Yes. "Move India fleets, or finish the fleet step. A fleet may stay." done
13. Yes. "Move India armies, or finish the army step. An army may stay." done
14. Yes. "Place a flag on a region this nation occupies alone, or finish." done
15. Yes. "On Maneuver, before Taxation, factor 0. Move clockwise 1 to 6 spaces. The first 3 cost 0." rondel:7
16. Yes. "Confirm Taxation (1 spaces, cost 0)." confirm
17. Yes. "Check the four taxation results, then commit. Revenue 4 uses header 0. Upkeep 2. Bonus 0. Power +0." commit
18. Yes. "On Taxation, factor 0. Move clockwise 1 to 6 spaces. The first 3 cost 0." rondel:0
19. Yes. "Confirm Factory (1 spaces, cost 0)." confirm
20. Yes. "Build one factory for India. The treasury pays 5 million." city:Kolkata

## Cash in my JSON

No other player's balance appeared. players[].cash for Ava, Cy, and Dee was null on every read, and scores was null. My cash was only on seat 1. A starting total did appear in the log text: "Experienced setup. Each player has 19 million." Later lines name payments, not balances: the China treasury pays 1 to Bo, 2 to Cy, and 3 to Dee; "Ava receives 4 million interest and forgoes 0"; "Ava receives 2 million from the bank for the Investor card."

## Rules

Rondel prices matched. At factor 0, 1 to 3 spaces cost 0 and 4, 5, and 6 spaces cost 1, 2, and 3. That is one million, plus the power factor, for each space past the third. Seven-space moves and staying put were not offered. I did not see a wrong cost. "1 spaces" is clumsy, but the cost shown was 0.

The tax line matched the written anchors. Two unoccupied factories and no flags make revenue 4. Two units make upkeep 2. A bonus of 1 starts at 6 million, and 2 at 10, so bonus 0 is right. Power +0 is the column below 6. The worked case of 11 million, bonus 2, and +4 did not occur. Factory pay of 5 from the treasury matches the Factory space. I did not see a wrong tax number.

The India, Brazil, United States, and Europe banners say the booklet does not name who leads. The experienced setup does name the method: the start player leads Russia, the player to the left of the start player leads China, and India, Brazil, the United States, and Europe are taken "in the same way." This test moved the lead one seat each nation. China matched (the seat left of the start player). India did not: the leader was two seats left of the start player, not the China leader again. Those banners still said to choose a bond or pass.

No Swiss Bank, canal, peace, or hostile/friendly prompt reached me. I sent no gift. Absent borders, Panama's west mouth, convoy, factory destruction, and a peace offer that does not ask every defender were not treated as bugs.
