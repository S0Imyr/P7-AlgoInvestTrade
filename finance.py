from utils import display_cell_length


class Action:
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
    def __init__(self, actions):
        self.actions = actions

    def __repr__(self):
        display = display_cell_length('Action', 12) + ' | ' \
                  + display_cell_length('Price', 12) + ' | ' \
                  + display_cell_length('Profit', 12) + '\n'
        for action in self.actions:
            display += display_cell_length(action.id, 12) + ' | ' \
                       + display_cell_length(action.price, 12) + ' | ' \
                       + display_cell_length(action.profit, 12) + '\n'
        return display

    def convert_to_action(self, names, prices, profits):
        if len(names) != len(prices) or len(names) != len(profits) or len(prices) != len(profits):
            print("The prices data and the profits data must coincide. The number of element don't match")
        else:
            for action in range(len(names)):
                self.actions.append(Action(names[action], prices[action], profits[action]))


if __name__ == '__main__':
    pass
