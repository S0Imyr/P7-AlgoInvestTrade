import itertools
from typing import List, Tuple

from models import Share
from utils.utils import display_cell_length


class Portfolio:
    """Portfolio model"""
    def __init__(self):
        self.shares: List[Share] = []
        self.price: float = 0
        self.profit_amount: float = 0

    def __repr__(self):
        display = display_cell_length('Action', 12) + ' | ' \
                  + display_cell_length('Price', 12) + ' | ' \
                  + display_cell_length('Profit', 12) + '\n'
        for share in self.shares:
            display += display_cell_length(share.name, 12) + ' | ' \
                       + display_cell_length(share.price, 12) + ' | ' \
                       + display_cell_length(str(share.profit_percentage) + '%', 12) + '\n'
        return display

    def __len__(self):
        return len(self.shares)

    @property
    def profit_percentage(self):
        """Calculate and return the net profit."""
        return self.profit_amount / self.price * 100

    def add_share(self, share: Share) -> None:
        """Add a share to the portfolio and update price and profit."""
        self.shares.append(share)
        self.price += share.price
        self.profit_amount += share.profit_amount

    def add_shares(self, shares: List[Share]):
        for share in shares:
            self.add_share(share)

    def prices(self) -> List[float]:
        """Return a list of prices for all shares in the portfolio."""
        return [share.price for share in self.shares]

    def net_profits(self) -> List[float]:
        """Return a list of net profits for all shares in the portfolio."""
        return [share.profit_amount for share in self.shares]

    # def add_shares_from_data(self, names, prices, profits):
    #     """Check if the data can be converted into shares and then add them to the portfolio"""
    #     if len(names) != len(prices) or len(names) != len(profits) or len(prices) != len(profits):
    #         raise ValueError("The prices data and the profits data must coincide. The number of element don't match")
    #     else:
    #         for share_index in range(len(names)):
    #             self.shares.append(Share(names[share_index], prices[share_index], profits[share_index]))
    #             self.price += prices[share_index]
    #             self.profit_amount += prices[share_index] * profits[share_index] / 100

    def add_shares_from_data(self, names, prices, profits):
        """Check if the data can be converted into shares and then add them to the portfolio"""
        if len(names) != len(prices) or len(names) != len(profits) or len(prices) != len(profits):
            raise ValueError("The prices data and the profits data must coincide. The number of elements don't match")
        else:
            num_shares = len(names)

        ignored_data = []
        for share_index in range(num_shares):
            try:
                new_share = Share(names[share_index], prices[share_index], profits[share_index])
                self.add_share(new_share)
            except ValueError:
                ignored_data.append((names[share_index], prices[share_index], profits[share_index]))

        if ignored_data:
            print("Les données suivantes ont été ignorées car elles contiennent des valeurs négatives :")
            for data in ignored_data:
                print(f"Name: {data[0]}, Price: {data[1]}, Profit: {data[2]}")

    def update_portfolio_stats(self) -> None:
        """Update price and profit for the entire portfolio."""
        self.price = sum(share.price for share in self.shares)
        self.profit_amount = sum(share.profit_amount for share in self.shares)

    def remove_ineffective_shares(self) -> None:
        """Select shares with positive prices and profits from the portfolio."""
        positive_shares: List[Share] = [share for share in self.shares if
                                        share.price > 0 and share.profit_percentage > 0]
        self.shares = positive_shares


if __name__ == '__main__':

    # test_create_portfolio
    print("---- Test 1 ----")
    portfolio = Portfolio()
    print('Liste des actions', portfolio.shares, [])
    print('Prix', portfolio.price, 0)
    print('Profit', portfolio.profit_amount, 0)

    # test_add_shares
    print("---- Test 2 ----")
    shares = [Share("Share D", 120, 4), Share("Share E", 180, 7)]
    portfolio = Portfolio()
    portfolio.add_shares(shares)
    print("Nombre d'actions", len(portfolio.shares), 2)
    print('Liste des actions', portfolio.shares, shares)
    print('Prix', portfolio.price, 300)  # 120 + 180
    print('Profit €', portfolio.profit_amount, 120 * 4 / 100 + 180 * 7 / 100)     # 17.4
    print('Profit %', portfolio.profit_percentage, 17.4 / 300 * 100)              # 5.8

    # test_add_data_shares
    print("---- Test 3 ----")
    portfolio = Portfolio()
    names = ["Share A", "Share C"]
    prices = [10, 20]
    profits = [5, 10]
    portfolio.add_shares_from_data(names, prices, profits)
    print("Nombre d'actions", len(portfolio.shares), 2)
    print('Prix', portfolio.price, 30)
    print('Profit €', portfolio.profit_amount, 10 * 5 / 100 + 20 * 10 / 100)    # 2.5
    print('Profit %', portfolio.profit_percentage, 2.5 / 30 * 100)             # 8.3333
