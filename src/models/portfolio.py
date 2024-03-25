import itertools
from typing import List, Tuple

from models import Share
from utils.utils import display_cell_length


class Portfolio:
    """Portfolio model"""
    def __init__(self):
        self.shares: List[Share] = []
        self.price: float = 0
        self.profit: float = 0

    def __repr__(self):
        display = display_cell_length('Action', 12) + ' | ' \
                  + display_cell_length('Price', 12) + ' | ' \
                  + display_cell_length('Profit', 12) + '\n'
        for share in self.shares:
            display += display_cell_length(share.name, 12) + ' | ' \
                       + display_cell_length(share.price, 12) + ' | ' \
                       + display_cell_length(str(share.profit) + '%', 12) + '\n'
        return display

    def __len__(self):
        return len(self.shares)

    def add_data_shares(self, names, prices, profits):
        """Check if the data can be converted into shares and then add them to the portfolio"""
        if len(names) != len(prices) or len(names) != len(profits) or len(prices) != len(profits):
            raise ValueError("The prices data and the profits data must coincide. The number of element don't match")
        else:
            for share in range(len(names)):
                self.shares.append(Share(names[share], prices[share], profits[share]))
                self.price += prices[share]
                self.profit += prices[share] * profits[share]

    def add_shares(self, shares):
        self.shares.extend(shares)
        for share in shares:
            self.price += share.price
            self.profit += share.net_profit

    def prices(self):
        prices_list = []
        for share in self.shares:
            prices_list.append(share.price)
        return prices_list

    def net_profits(self):
        profits_list = []
        for share in self.shares:
            profits_list.append(share.profit * share.price / 100)
        return profits_list

    def remove_ineffective_shares(self) -> None:
        """Select shares with positive prices and profits from the portfolio."""
        positive_shares: List[Share] = [share for share in self.shares if
                                         share.price > 0 and share.profit > 0]
        self.shares = positive_shares
