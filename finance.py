from utils import display_cell_length


class Action:
    """Create an action object and calculate the net_profit"""
    def __init__(self, name, price, profit):
        self.name = name
        self.price = price
        self.profit = profit
        self.net_profit = self.price * self.profit / 100

    def __repr__(self):
        return f'Action {self.name}: \n' \
               f'Price: {self.price} \n' \
               f'Profit: {self.profit}%'


class Portfolio:
    """Create a protfolio object with multiple actions"""
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
                self.actions.append(Action(names[action], prices[action], profits[action]))
                self.price += prices[action]
                self.profit += prices[action] * profits[action]

    def add_actions(self, actions):
        self.actions.extend(actions)
        for action in actions:
            self.price += action.price
            self.profit += action.net_profit

