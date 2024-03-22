import unittest
from models import Share, Portfolio


class TestShare(unittest.TestCase):
    def test_create_share(self):
        share = Share("Company A", 100, 5)
        self.assertEqual(share.name, "Company A")
        self.assertEqual(share.price, 100)
        self.assertEqual(share.profit, 5)
        self.assertEqual(share.net_profit, 5)


class TestPortfolio(unittest.TestCase):
    def test_create_portfolio(self):
        portfolio = Portfolio()
        self.assertEqual(portfolio.actions, [])
        self.assertEqual(portfolio.price, 0)
        self.assertEqual(portfolio.profit, 0)

    def test_add_actions(self):
        shares = [Share("Company D", 120, 4), Share("Company E", 180, 7)]
        portfolio = Portfolio()
        portfolio.add_actions(shares)
        self.assertEqual(len(portfolio.actions), 2)
        self.assertEqual(portfolio.actions, shares)
        self.assertEqual(portfolio.price, 300)  # 120 + 180
        self.assertEqual(portfolio.profit, 17.4)  # 120 * 4 / 100 + 180 * 7 / 100


if __name__ == "__main__":
    unittest.main()
