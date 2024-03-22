from models import Share
from utils.utils import display_cell_length


class Portfolio:
    """Portfolio model"""
    def __init__(self):
        self.actions = []
        self.price = 0
        self.profit = 0

    def __repr__(self):
        display = display_cell_length('Action', 12) + ' | ' \
                  + display_cell_length('Price', 12) + ' | ' \
                  + display_cell_length('Profit', 12) + '\n'
        for action in self.actions:
            display += display_cell_length(action.name, 12) + ' | ' \
                       + display_cell_length(action.price, 12) + ' | ' \
                       + display_cell_length(str(action.profit) + '%', 12) + '\n'
        return display

    def add_data_actions(self, names, prices, profits):
        """Check if the data can be converted into actions and then add them to the portfolio"""
        if len(names) != len(prices) or len(names) != len(profits) or len(prices) != len(profits):
            raise ValueError("The prices data and the profits data must coincide. The number of element don't match")
        else:
            for action in range(len(names)):
                self.actions.append(Share(names[action], prices[action], profits[action]))
                self.price += prices[action]
                self.profit += prices[action] * profits[action]

    def add_actions(self, actions):
        self.actions.extend(actions)
        for action in actions:
            self.price += action.price
            self.profit += action.net_profit

    def prices(self):
        prices_list = []
        for action in self.actions:
            prices_list.append(action.price)
        return prices_list

    def net_profits(self):
        profits_list = []
        for action in self.actions:
            profits_list.append(action.profit * action.price / 100)
        return profits_list
