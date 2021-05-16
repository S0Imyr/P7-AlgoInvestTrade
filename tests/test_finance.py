from finance import Action


class TestAction:
    action = Action("share1", 50, 0.05)
    def test_name(self):
        assert self.action.name == "share1"

    def test_price(self):
        assert self.action.price == 50

    def test_profit(self):
        assert self.action.profit == 0.05
