from finance import Action


class TestAction:
    action = Action("share1", 50, 5)

    def test_net_profit(self):
        assert self.action.net_profit == 50 * 5 / 100

    def test_action_repr(self):
        assert self.action.__repr__() == "Action share1: \nPrice: 50 \nProfit: 5%"
