import unittest
from models import Share, Portfolio


class TestShare(unittest.TestCase):
    def test_create_share(self):
        share = Share("Company A", 100, 5)
        self.assertEqual(share.name, "Company A")
        self.assertEqual(share.price, 100)
        self.assertEqual(share.profit, 5)
        self.assertEqual(share.net_profit, 5)

    def test_calculate_net_profit(self):
        # Test with positive price and profit
        share1 = Share("ABC", 10, 5)
        self.assertEqual(share1.net_profit, 0.5)

        # Test with zero price and profit
        share2 = Share("XYZ", 0, 0)
        self.assertEqual(share2.net_profit, 0)

        # Test with negative profit
        share3 = Share("DEF", 20, -2)
        self.assertEqual(share3.net_profit, -0.4)


class TestPortfolio(unittest.TestCase):

    def setUp(self):
        self.portfolio = Portfolio()

    def test_create_portfolio(self):
        portfolio = Portfolio()
        self.assertEqual(portfolio.shares, [])
        self.assertEqual(portfolio.price, 0)
        self.assertEqual(portfolio.profit, 0)

    def test_add_shares(self):
        shares = [Share("Share D", 120, 4), Share("Share E", 180, 7)]
        portfolio = Portfolio()
        portfolio.add_shares(shares)
        self.assertEqual(len(portfolio.shares), 2)
        self.assertEqual(portfolio.shares, shares)
        self.assertEqual(portfolio.price, 300)  # 120 + 180
        self.assertEqual(portfolio.profit, 17.4)  # 120 * 4 / 100 + 180 * 7 / 100

    def test_add_data_shares(self):
        names = ["Share A", "Share C"]
        prices = [10, 20]
        profits = [5, 10]
        self.portfolio.add_data_shares(names, prices, profits)
        self.assertEqual(len(self.portfolio.shares), 2)
        self.assertEqual(self.portfolio.price, 30)
        self.assertEqual(self.portfolio.profit, 250)


if __name__ == "__main__":
    unittest.main()
