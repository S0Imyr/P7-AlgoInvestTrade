import csv


def import_shares_data():
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


def how_many_shares(share_price, money):
    return money // share_price


class BigTree:
    def __init__(self, shares):
        self.choices = []
        for share in shares:
            self.choices.append(Choice(share.id, share.price, share.profit))
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
    def __init__(self, shares_ids, price, profit):
        self.shares_ids = shares_ids
        self.price = price
        self.profit = profit

    def __repr__(self):
        return f'Shares : {self.shares_ids} --- ' \
               f'Price : {self.price} --- ' \
               f'Profit : {self.profit}'


class Share:
    def __init__(self, id, price, profit):
        self.id = id
        self.price = price
        self.profit = profit

    def __repr__(self):
        return f'Share {self.id}: \n' \
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
        self.shares = []

    def initialize(self, prices, profits):
        if len(prices) != len(profits):
            print("The prices data and the profits data must coincide. The number of element don't match")
        else:
            for num_share in range(len(prices)):
                self.shares.append(Share(num_share, prices[num_share], profits[num_share]))

    def __repr__(self):
        display = display_cell_length('Share', 12) + ' | ' + display_cell_length('Price', 12) + ' | ' + display_cell_length('Profit', 12) + '\n'
        for share in self.shares:
            display += display_cell_length(share.id, 12) + ' | ' + display_cell_length(share.price, 12) + ' | ' + display_cell_length(share.profit, 12) + '\n'
        return display


if __name__ == '__main__':
    names, prices, profits = import_shares_data()


    """ Tests data """
    pricestry = [10, 15, 25, 35, 30, 40]
    profitstry = [0.05, 0.1, 0.15, 0.2, 0.17, 0.25]
    try_cap = 100
    min_price = min(pricestry)
    try_portfolio = Portfolio()
    try_portfolio.initialize(pricestry, profitstry)
    """ Tests data """
    try_tree_height = 0
    for share in try_portfolio.shares:
        try_tree_height = max(try_tree_height, how_many_shares(share.price, try_cap))


    portfolio = Portfolio()
    portfolio.initialize(prices, profits)
    cap = 500

    tree_height = 0
    for share in portfolio.shares:
        tree_height = max(tree_height, how_many_shares(share.price, cap))
    print(tree_height)

    tree = BigTree(try_portfolio.shares)
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
    print(len(tree.branch))
