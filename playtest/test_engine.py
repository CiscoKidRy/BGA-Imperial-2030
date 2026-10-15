"""Checks for the local Imperial 2030 test engine.

The numbers are the booklet cases: China on Investor at factor 2, the tax
chart, experienced cash, and a nation reaching 25.
"""

import unittest

import engine
from engine import Game, TAX_BONUS, TAX_POWER, factor, tax_index


def one_bond_each(game: Game) -> None:
    for _nation in range(6):
        for turn in range(game.n):
            seat = game._draft_seat()
            if turn == 0:
                nation = engine.NATIONS[game.draft_nation]
                game.act(seat, f"buy:{nation}:4")
            else:
                game.act(seat, "pass")


class Rules(unittest.TestCase):
    def test_factor_and_tax_chart(self):
        self.assertEqual(factor(0), 0)
        self.assertEqual(factor(5), 0)
        self.assertEqual(factor(6), 1)
        self.assertEqual(factor(11), 2)
        self.assertEqual(factor(17), 3)
        self.assertEqual(factor(25), 5)
        self.assertEqual(tax_index(5), 0)
        self.assertEqual(tax_index(6), 1)
        self.assertEqual((TAX_BONUS[1], TAX_POWER[1]), (1, 1))
        self.assertEqual(tax_index(7), 1)
        self.assertEqual(tax_index(11), 4)
        self.assertEqual((TAX_BONUS[4], TAX_POWER[4]), (2, 4))
        self.assertEqual(tax_index(17), 9)
        self.assertEqual((TAX_BONUS[9], TAX_POWER[9]), (5, 9))

    def test_experienced_cash_and_decline(self):
        game = Game(["Ava", "Bo", "Cy", "Dee"])
        self.assertEqual(game.cash, [19, 19, 19, 19])
        game.act(0, "pass")
        self.assertEqual(game.cash[0], 19)
        self.assertEqual(game.bonds[0], [])
        self.assertEqual(game.draft_nation, 0)
        self.assertEqual(game._draft_seat(), 1)

    def test_opening_leaves_two_million_false_for_experienced(self):
        game = Game(["Ava", "Bo", "Cy", "Dee"])
        one_bond_each(game)
        self.assertEqual(game.phase, "rondel")
        self.assertEqual(game.controller["russia"], 0)
        self.assertEqual(game.controller["china"], 1)
        self.assertEqual(game.investor, 1)
        self.assertEqual(game.cash[0], 11)
        self.assertIsNone(game.view(1)["players"][0]["cash"])
        self.assertEqual(game.view(0)["you"]["cash"], 11)
        self.assertNotIn("11", " ".join(game.log))

    def test_china_rondel_sentence_cost_and_hidden_cash(self):
        game = Game(["Ava", "Bo", "Cy", "Dee"])
        game.phase = "rondel"
        game.turn = 1
        game.controller["china"] = 0
        game.marker["china"] = 3
        game.power["china"] = 11
        game.cash[0] = 5
        actor = game.view(0)
        self.assertEqual(
            actor["banner"]["sentence"],
            "On Investor, factor 2, choosing Taxation (4 spaces, cost 3) or Factory (5 spaces, cost 6).",
        )
        rows = {item["id"]: item for item in actor["legal"]}
        self.assertEqual(rows["rondel:4"]["cost"], 0)
        self.assertEqual(rows["rondel:7"]["cost"], 3)
        self.assertTrue(rows["rondel:7"]["enabled"])
        self.assertEqual(rows["rondel:0"]["cost"], 6)
        self.assertFalse(rows["rondel:0"]["enabled"])
        self.assertNotIn("5", rows["rondel:0"]["detail"])
        other = game.view(1)
        factory = next(item for item in other["legal"] if item["id"] == "rondel:0")
        self.assertTrue(factory["enabled"])
        self.assertNotIn("cannot pay", factory["detail"].lower())
        self.assertIsNone(other["players"][0]["cash"])
        self.assertNotIn("confirm", {item["id"] for item in other["legal"]})
        self.assertTrue(other["banner"]["waiting"])

    def test_swiss_force_reprices_the_shorter_move(self):
        game = Game(["Ava", "Bo"])
        game.phase = "rondel"
        game.turn = 0
        game.controller["russia"] = 0
        game.marker["russia"] = 0
        game.power["russia"] = 0
        game.cash[0] = 10
        game.treasury["russia"] = 5
        game.bonds[1].append(("russia", 1, 2))
        game.pile["russia"] = [pair for pair in game.pile["russia"] if pair != (1, 2)]
        game.investor = 1
        game.swiss[1] = True
        game.act(0, "rondel:4")
        game.act(0, "confirm")
        self.assertEqual(game.phase, "swiss-veto")
        game.act(1, "force")
        self.assertEqual(game.marker["russia"], 3)
        self.assertEqual(game.cash[0], 10)
        self.assertEqual(game.phase, "investor-buy")
        self.assertIn("forces", " ".join(game.log))

    def test_upgrade_pays_the_difference_only(self):
        game = Game(["Ava", "Bo"])
        game.bonds[0].append(("china", 1, 2))
        game.pile["china"] = [pair for pair in game.pile["china"] if pair != (1, 2)]
        game.cash[0] = 3
        game.treasury["china"] = 0
        game.investor = 0
        game.phase = "investor-buy"
        game.pending = {"nation": "china", "queue": [0], "buyer": 0, "passed": False}
        game.act(0, "up:china:2:4")
        self.assertEqual(game.cash[0], 1)
        self.assertEqual(game.treasury["china"], 2)
        self.assertEqual(game.bonds[0], [("china", 2, 4)])
        self.assertIn((1, 2), game.pile["china"])

    def test_interest_shortfall_does_not_print_remaining_cash(self):
        game = Game(["Ava", "Bo"])
        game.controller["russia"] = 0
        game.cash[0] = 1
        game.cash[1] = 0
        game.treasury["russia"] = 0
        game.bonds[1].append(("russia", 5, 12))
        game._pay_interest("russia")
        self.assertEqual(game.cash[0], 0)
        self.assertEqual(game.cash[1], 1)
        text = " ".join(game.log)
        self.assertIn("pays 1 million", text)
        self.assertIn("unpaid in this test", text)
        self.assertNotIn("cannot cover", text)
        self.assertNotIn("empty", text.lower())

    def test_taxation_to_25_skips_investor_steps(self):
        game = Game(["Ava", "Bo"])
        game.controller["russia"] = 0
        game.power["russia"] = 24
        game.flags["Mexico"] = "russia"
        game.flags["Turkey"] = "russia"
        game.pending = {"nation": "russia", "passed": True, "space": "Taxation"}
        game._do_tax("russia")
        self.assertEqual(game.phase, "tax-confirm")
        preview = game.pending["tax"]
        self.assertEqual(preview["revenue"], 6)
        self.assertEqual(preview["gain"], 1)
        self.assertEqual(preview["bonus"], 1)
        game.act(0, "commit")
        self.assertTrue(game.over)
        self.assertEqual(game.power["russia"], 25)
        self.assertNotEqual(game.phase, "investor-buy")
        self.assertEqual(game.view(1)["banner"]["sentence"], "Game over: Russia reached 25.")
        self.assertEqual(game.view(1)["players"][0]["cash"], game.cash[0])

    def test_opening_rondel_can_tax(self):
        game = Game(["Ava", "Bo", "Cy", "Dee"])
        one_bond_each(game)
        game.act(0, "rondel:7")
        game.act(0, "confirm")
        self.assertEqual(game.phase, "tax-confirm")
        self.assertEqual(game.view(0)["banner"]["phase"], "Taxation")
        self.assertTrue(any(item["id"] == "commit" for item in game.view(0)["legal"]))
        game.act(0, "commit")
        self.assertEqual(game.turn, 1)
        self.assertEqual(game.phase, "rondel")
        self.assertEqual(game._actor_seat(), 1)

    def test_named_border_and_blocked_invented_border(self):
        game = Game(["Ava", "Bo"])
        game.controller["usa"] = 0
        game.armies.append(("usa", "New Orleans", False))
        game.phase = "maneuver"
        game.pending = {"nation": "usa", "sub": "army", "moved": [], "passed": False}
        game.act(0, "army:0:Mexico")
        self.assertEqual(game.armies[0][1], "Mexico")
        game.pending["moved"] = []
        with self.assertRaises(ValueError):
            game.act(0, "army:0:Canada")


if __name__ == "__main__":
    unittest.main()
