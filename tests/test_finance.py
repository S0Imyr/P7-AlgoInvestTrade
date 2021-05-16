from finance import Action, Portfolio
import pytest

class TestAction:
    def setup_method(self):
        self.action = Action("share1", 50, 5)

    def test_net_profit(self):
        assert self.action.net_profit == 50 * 5 / 100

    def test_action_repr(self):
        assert self.action.__repr__() == "Action share1: \nPrice: 50 \nProfit: 5%"


class TestPortfolio:
    def setup_method(self):
        self.portfolio = Portfolio()
    
    def test_add_valid_actions_portfolio(self):
        n0 = len(self.portfolio.actions)
        names = ['share1', 'share2', 'share3']
        prices = [15, 20, 50]
        profits = [5, 15, 2]
        self.portfolio.add_actions(names, prices, profits)
        assert len(self.portfolio.actions) - n0 == len(['share1', 'share2', 'share3'])

    def test_add_invalid_actions_portfolio(self):
        names = ['share1', 'share3']
        prices = [15, 20, 50]
        profits = [5, 15]
        with pytest.raises(ValueError):
            self.portfolio.add_actions(names, prices, profits)
