import csv, math
from finance import Action, Portfolio


def import_actions_data():
    names = []
    prices = []
    profits = []
    with open('dataForceBrute.csv', newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=';')
        for row in data:
            if row[0] != 'name':
                names.append(row[0])
            if row[1] != 'price':
                prices.append(float(row[1]))
            if row[2] != 'profit':
                profits.append(float(row[2]))
    return names, prices, profits


def how_many_shares(action_price, money):
    return int(money / action_price)


class Choice:
    def __init__(self, name, price, profit):
        self.name = name
        self.price = price
        self.profit = profit

    def __repr__(self):
        return f'{self.name}: \n' \
               f'Price: {self.price} \n' \
               f'Profit: {self.profit} \n'


class Node:
    def __init__(self, height, width, choice, price, profit):
        self.height = height
        self.width = width
        self.choice = choice
        self.price = price
        self.profit = profit
        self.history = []
        self.explored = False
        self.evaluated = False
        self.open = True

    def __repr__(self):
        display = f'Node ({self.height}, {self.width}) - '
        if self.evaluated:
            display += f'Price : {self.price}\n' \
                       f'Profit : {self.profit}\n'
        else:
            display += 'not yet priced\n'
        return display

    def evaluate(self):
        if not self.evaluated:
            if self.price == 0:
                self.price = self.choice.price
                self.profit = self.choice.profit
            else:
                net_profit = self.profit * self.price + self.choice.price * self.choice.profit
                self.price += self.choice.price
                self.profit = net_profit / self.price
            self.evaluated = True


class Branch:
    def __init__(self, history, price, profit):
        self.history = history
        self.price = price
        self.profit = profit

    def __repr__(self):
        return f'{self.history} --- ' \
               f'Price : {self.price} --- ' \
               f'Profit : {self.profit}'


class Tree:
    def __init__(self, actions):
        self.actions = actions
        self.choices = []
        self.nodes = [[Node(0, 0, Choice(0, 0, 0), 0, 0)]]
        self.branch = []

    def define_choices_optimised(self, action, cap):
        self.choices = []
        for i in range(how_many_shares(action.price, cap) + 1):
            self.choices.append(Choice(f"{i} action(s) {action.id}", i * action.price, action.profit))

    def define_choices_brute(self):
        self.choices = []
        for action in self.actions:
            self.choices.append(Choice(action.id, action.price, action.profit))

    def grow(self):
        i = 0
        min_choice_price = math.inf
        next_nodes = []
        for choice in self.choices:
            min_choice_price = min(min_choice_price, choice.price)

        for node in self.nodes[-1]:
            for choice in self.choices:
                if node.price + choice.price <= cap:
                    new_node = Node(node.height + 1, i, choice, node.price, node.profit)
                    new_node.history.extend(node.history)
                    new_node.history.append(choice.name)
                    new_node.evaluate()
                    next_nodes.append(new_node)
                    i += 1
        self.nodes.append(next_nodes)


if __name__ == '__main__':
    names, prices, profits = import_actions_data()


    """ Tests data """
    #0
    names1 = [1, 2, 3]
    prices1 = [15, 30, 40]
    profits1 = [0.10, 0.17, 0.25]
    min_price = 10

    portfolio = Portfolio()
    portfolio.initialize(names1, prices1, profits1)

    cap = 100

    #1
    namestry = ['01', '02', '03', '04', '05', '06']
    pricestry = [10, 15, 25, 35, 30, 40]
    profitstry = [0.05, 0.1, 0.15, 0.2, 0.17, 0.25]
    try_cap = 100
    min_pricetry = min(pricestry)

    try_portfolio = Portfolio()
    try_portfolio.initialize(namestry, pricestry, profitstry)

    """ Tests data """


    portfolio.initialize(names, prices, profits)

    tree = Tree(portfolio.actions)

    for num_action in range(len(names1)):
        tree.define_choices_optimised(portfolio.actions[num_action], cap)
        tree.grow()
        print(tree.nodes[-1])


    """    tree = BigTree(try_portfolio.actions)
    tree.initialize()
    print('Step 1: ', len(tree.opened_nodes))
    tree.explore(try_cap)
    print('Step 2', len(tree.opened_nodes))
    tree.explore(try_cap)
    print('Step 3', len(tree.opened_nodes))
    tree.explore(try_cap)
    print('Step 4', len(tree.opened_nodes))
    tree.explore(try_cap)
    print('Step 5', len(tree.opened_nodes))
    tree.explore(try_cap)
    print('Step 6', len(tree.opened_nodes))
    tree.explore(try_cap)
    print('Step 7', len(tree.opened_nodes))
    tree.explore(try_cap)
    print('Step 8', len(tree.opened_nodes))
    tree.explore(try_cap)
    print('Step 9', len(tree.opened_nodes))
    tree.explore(try_cap)
    print('Step 10', len(tree.opened_nodes))
    tree.explore(try_cap)

    print(tree.branch[0])
    print(len(tree.branch))"""

