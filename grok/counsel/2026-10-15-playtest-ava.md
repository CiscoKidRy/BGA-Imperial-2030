# Ava playtest, 15 Oct 2026

Seat 0. Stopped after 25 of my actions. Phase was still Maneuver, not game over. I did not act on the next banner: "Move Europe fleets, or finish the fleet step. A fleet may stay."

Every banner below told me what to do.

1. "Ava, choose one Russia bond, or pass." Yes. Bought price 2.
2. "Ava, choose one China bond, or pass." Yes. Bought price 9.
3. "Ava, choose one India bond, or pass. The booklet does not name who leads this nation. This test rotates the lead." Yes. Bought price 6.
4. "Ava, choose one Brazil bond, or pass. The booklet does not name who leads this nation. This test rotates the lead." Yes. Bought price 2.
5. "Ava, choose one United States bond, or pass. The booklet does not name who leads this nation. This test rotates the lead." Yes. Passed. Cash was 0, so nothing at 9 or under was enabled.
6. "Ava, choose one Europe bond, or pass. The booklet does not name who leads this nation. This test rotates the lead." Yes. Passed. Cash was still 0.
7. "First turn for China. The octagon is in the hub. Any of the eight spaces may be chosen. The move is not limited to six spaces, and it costs nothing." Yes. Chose rondel:1.
8. "Confirm Production, after Factory. The first turn costs nothing." Yes. Confirmed.
9. "Commit production: army in Beijing, fleet in Shanghai." Yes. Committed.
10. "On Production, after Factory, factor 0. Move clockwise 1 to 6 spaces. The first 3 cost 0." Yes. Chose the 1-space move.
11. "Confirm Maneuver, before Investor (1 spaces, cost 0)." Yes. Confirmed.
12. "Move China fleets, or finish the fleet step. A fleet may stay." Yes. Finished.
13. "Move China armies, or finish the army step. An army may stay." Yes. Finished.
14. "Place a flag on a region this nation occupies alone, or finish." Yes. Finished.
15. "On Maneuver, before Investor, factor 0. Move clockwise 1 to 6 spaces. The first 3 cost 0." Yes. Chose 1 space, onto Investor.
16. "Confirm Investor (1 spaces, cost 0)." Yes. Confirmed.
17. "Ava, buy one new bond in any nation, upgrade one bond of the same nation, or pass." Yes. Bought a new Europe bond at 2. I had no Europe bond yet.
18. "First turn for Europe. The octagon is in the hub. Any of the eight spaces may be chosen. The move is not limited to six spaces, and it costs nothing." Yes. Chose rondel:1.
19. "Confirm Production, after Factory. The first turn costs nothing." Yes. Confirmed.
20. "Commit production: fleet in London, army in Paris." Yes. Committed.
21. "On Investor, factor 0. Move clockwise 1 to 6 spaces. The first 3 cost 0." Yes. Chose 1 space, onto Import.
22. "Confirm Import (1 spaces, cost 0)." Yes. Confirmed.
23. "Buy up to 3 units for China. Each costs 1 million from the treasury." Yes. Finished without buying.
24. "On Production, after Factory, factor 0. Move clockwise 1 to 6 spaces. The first 3 cost 0." Yes. Chose the 1-space move.
25. "Confirm Maneuver, before Investor (1 spaces, cost 0)." Yes. Confirmed.

## Other players' cash

No hidden cash total appeared. Bo, Cy, and Dee had `cash: null` on every read, including the last one. `scores` was null because the game was not over. The setup log did say "Experienced setup. Each player has 19 million." That is the shared opening stake, the same number for all four seats, not a later balance. Interest lines named payments only: Bo 1, Cy 2, Dee 3. They did not state what those players had left.

## What I could check

Rondel prices at factor 0 matched the booklet. The first three spaces cost 0. Four, five, and six spaces cost 1, 2, and 3. First turns offered all eight spaces at cost 0. Later turns offered only 1 to 6 and did not offer the space already occupied. From Investor, Taxation was 4 spaces for 1, and Factory was 5 spaces for 2. That is the same schedule as the booklet's factor-2 example (3 and 6), with 0 in place of 2.

`nation.factor` is null while power is 0, but those banners say "factor 0", and the costs used 0. I am not calling that a wrong rondel cost. "1 spaces" is clumsy. The number was still 0.

Moves that pass Investor are labeled "Interest is not paid." That matches interest being paid only when the marker lands on Investor. I never chose a pass, so I did not see whether the investor card still acted.

China landed on Investor with 21 in the treasury. It paid 10 of interest and had 11 left, which is still the treasury. My own 4 was paid in full. I then got 2 for the Investor card, and the card passed to Bo. That order matches the booklet.

Brazil, India, and Russia each taxed 4 from two factories and no flags. Bonus was 0, which is required below 6. India and Russia paid 2 upkeep for 2 units. Power stayed 0. I never saw revenue 11, so the booklet's +4 example did not come up.

Russia opened with me, and China with the seat on my left. The India, Brazil, United States, and Europe banners say the booklet does not name that lead and that this test rotates it. I am not treating that rotation as a bug.

No Swiss Bank, canal, peace, or hostile/friendly prompt reached me.

I cannot support a rules contradiction from these 25 actions. No wrong tax number, wrong rondel cost, leaked private cash total, or banner that failed to say what to do.
