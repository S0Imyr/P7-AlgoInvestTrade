prices = [10, 15, 25, 35, 30, 40, 11, 13, 24, 17, 21, 55, 19, 7, 9, 4, 2, 5, 12, 57]
profits = [0.05, 0.10, 0.15, 0.20, 0.17, 0.25, 0.07, 0.11, 0.13, 0.27, 0.17, 0.09, 0.23, 0.01, 0.03, 0.08, 0.12, 0.14, 0.21, 0.18]

target = 100
pricestry = [10, 15, 25, 35, 30, 40]
profitstry = [0.05, 0.1, 0.15, 0.2, 0.17, 0.25]

min_price = min(pricestry)
possibilities = []
actual_share = 0

total_cost = 0


class Tree:
    def __init__(self, shares):
        self.shares = shares
        self.nodes = []
        self.opened_nodes = []
        self.branch = []

    def initialize(self):
        for share in self.shares:
            new_node = Node(1, share, share.price)
            new_node.history = [share.id]
            self.opened_nodes.append(new_node)
        self.nodes = [self.opened_nodes]

    def explore(self):
        next_nodes = []
        for node in self.opened_nodes:
            history = node.history
            for share in self.shares:
                if node.price + min_price <= target:
                    if node.price + share.price <= target:
                        child = Node(node.height + 1, share, node.price + share.price)
                        child.history.extend(history)
                        child.history.append(share.id)
                        next_nodes.append(child)
                else:
                    self.branch.append(Possibility(node.history))
        self.opened_nodes = next_nodes
        self.nodes.append(next_nodes)

    def cut_branch(self):
        self.opened_nodes = []
        for node in self.nodes:
            node.price += node.share.price
            if node.price < target:
                self.opened_nodes.append(node)

    def grow(self):
        pass


class Node:
    def __init__(self, height, share, price):
        self.height = height
        self.share = share
        self.price = price
        self.history = []
        self.explored = False

    def __repr__(self):
        return f'Node ({self.height}, {self.share.id}) --- ' \
               f'price = {self.price}'


class Possibility:
    def __init__(self, shares_ids):
        self.shares_ids = shares_ids
        self.profit = 0
        self.price = 0

    def evaluate_price(self):
        for share_id in self.shares_ids:
            self.price += tree.shares[share_id].price

    def evaluate_profit(self):
        for share_id in self.shares_ids:
            self.profit += tree.shares[share_id].evaluate_profit()

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

    def evaluate_profit(self):
        return self.price * self.profit / 100


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


def available_shares(list_shares, money):
    pass

def how_many_shares(share_price, money):
    return money // share_price


def can_i_add_share(cost, money):
    pass


def add_share(share_id):
    pass


if __name__ == "__main__":

    try_portfolio = Portfolio()
    try_portfolio.initialize(pricestry, profitstry)
    share_option = []
    for share in try_portfolio.shares:
        for i in range(how_many_shares(share.price, target)):
            share_option.append(share)

    print(share_option)
    print(try_portfolio)

    tree = Tree(try_portfolio.shares)
    tree.initialize()
    print(tree.nodes)
    tree.explore()
    print(tree.opened_nodes)
    tree.explore()
    print(tree.opened_nodes)
    print(tree.opened_nodes[1].history)
    tree.explore()
    print(tree.opened_nodes)
    tree.explore()
    print(tree.opened_nodes)
    tree.explore()
    print(tree.opened_nodes)
    tree.explore()
    print(tree.opened_nodes)
    tree.explore()
    print(tree.opened_nodes)
    tree.explore()
    print(tree.opened_nodes)
    tree.explore()
    print(tree.opened_nodes)
    print(tree.branch[0])
    tree.branch[0].evaluate_profit()
    tree.branch[0].evaluate_price()
    print(tree.branch[0])
"""    while len(tree.open_nodes) == 0:
        tree.explore()
        tree.cut_branch()"""


"""    for num_share in range(len(how)):
        for j in range(how[num_share]):
            possibility = []"""



