from finance import Action


class TestAction:
    action = Action("share1", 50, 5)

    def test_net_profit(self):
        assert self.action.net_profit == 50 * 5 / 100
