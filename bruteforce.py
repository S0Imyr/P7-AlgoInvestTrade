import csv


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


class BigTree:
    def __init__(self, actions):
        self.choices = []
        for action in actions:
            self.choices.append(Choice(action.id, action.price, action.profit))
        self.nodes = []
        self.opened_nodes = []
        self.branch = []

    def initialize(self):
        for choice in self.choices:
            new_node = Node(1, choice, 0, 0)
            new_node.history = [choice.name]
            new_node.evaluate()
            self.opened_nodes.append(new_node)
        self.nodes = [self.opened_nodes]

    def explore(self, cap):
        next_nodes = []
        for node in self.opened_nodes:
            history = node.history
            for choice in self.choices:
                if node.price + min_price <= cap:
                    if node.price + choice.price <= cap:
                        child = Node(node.height + 1, choice, node.price, node.profit)
                        child.evaluate()
                        child.history.extend(history)
                        child.history.append(choice.name)
                        next_nodes.append(child)
                else:
                    self.branch.append(Branch(node.history, node.price, node.profit))
        self.opened_nodes = next_nodes
        self.nodes.append(next_nodes)


class Choice:
    def __init__(self, name, price, profit):
        self.name = name
        self.price = price
        self.profit = profit


class Tree:
    def __init__(self, actions):
        self.possibilities = []
        self.actions = actions
        self.nodes = []
        self.opened_nodes = []
        self.branch = []

    def initialize(self, target):
        action = self.actions[0]
        firsts_nodes = []
        max_shares = how_many_shares(action.price, target) + 1
        for i in range(max_shares):
            choice = Choice(f'{i} action {action.id}', action.price * i, action.profit)
            first_node = Node(1, choice, 0, 0)
            first_node.evaluate()
            firsts_nodes.append(first_node)
        self.opened_nodes = firsts_nodes
        self.nodes.extend(firsts_nodes)

    def explore(self, target):
        for action in self.actions[1:]:
            for i in range(how_many_shares(action.price, target)):
                pass


class Node:
    def __init__(self, height, choice, price, profit):
        self.height = height
        self.choice = choice
        self.price = price
        self.profit = profit
        self.history = []
        self.explored = False
        self.evaluated = False

    def __repr__(self):
        display = f'Node ({self.height}, {self.choice.name}) \n'
        if self.evaluated:
            display += f'Price : {self.price}'
        else:
            display += 'not yet priced'
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
    def __init__(self, actions_ids, price, profit):
        self.actions_ids = actions_ids
        self.price = price
        self.profit = profit

    def __repr__(self):
        return f'Action : {self.actions_ids} --- ' \
               f'Price : {self.price} --- ' \
               f'Profit : {self.profit}'


class Action:
    def __init__(self, id, price, profit):
        self.id = id
        self.price = price
        self.profit = profit

    def __repr__(self):
        return f'Action {self.id}: \n' \
               f'Price: {self.price} \n' \
               f'Profit: {self.profit}'

    def net_profit(self):
        return self.price * self.profit


def display_cell_length(message, length):
    if len(str(message)) > length:
        return str(message)[:length]
    else:
        return str(message) + " " * (length - len(str(message)))


class Portfolio:
    def __init__(self):
        self.actions = []

    def initialize(self, prices, profits):
        if len(prices) != len(profits):
            print("The prices data and the profits data must coincide. The number of element don't match")
        else:
            for num_action in range(len(prices)):
                self.actions.append(Action(num_action, prices[num_action], profits[num_action]))

    def __repr__(self):
        display = display_cell_length('Action', 12) + ' | ' + display_cell_length('Price', 12) + ' | ' + display_cell_length('Profit', 12) + '\n'
        for action in self.actions:
            display += display_cell_length(action.id, 12) + ' | ' + display_cell_length(action.price, 12) + ' | ' + display_cell_length(action.profit, 12) + '\n'
        return display


if __name__ == '__main__':
    names, prices, profits = import_actions_data()


    """ Tests data """
    pricestry = [10, 15, 25, 35, 30, 40]
    profitstry = [0.05, 0.1, 0.15, 0.2, 0.17, 0.25]
    try_cap = 100
    min_price = min(pricestry)
    try_portfolio = Portfolio()
    try_portfolio.initialize(pricestry, profitstry)
    """ Tests data """
    try_tree_height = 0
    for action in try_portfolio.actions:
        try_tree_height = max(try_tree_height, how_many_shares(action.price, try_cap))


    portfolio = Portfolio()
    portfolio.initialize(prices, profits)
    cap = 500

    tree_height = 0
    for action in portfolio.actions:
        tree_height = max(tree_height, how_many_shares(action.price, cap))
    print(tree_height)

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

    secondtree = Tree(portfolio.actions)

    secondtree.initialize(500)
    print(secondtree.opened_nodes)