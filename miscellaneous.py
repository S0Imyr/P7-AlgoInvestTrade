import math
import cProfile

from finance import Portfolio
from operator import attrgetter
from utils import display_cell_length
from importdata import import_actions_data


def how_many_shares(action_price, money):
    return int(money / action_price)


class Choice:
    def __init__(self, name, price, profit, composition):
        self.name = name
        self.price = price
        self.profit = profit
        self.composition = composition

    def __repr__(self):
        return f'{self.name}: \n' \
               f'Price: {self.price} \n' \
               f'Profit: {self.profit} \n'


class Node:
    def __init__(self, height, width, choice, price, net_profit):
        self.height = height
        self.width = width
        self.choice = choice
        self.price = price
        self.net_profit = net_profit
        self.history = {}
        self.explored = False
        self.evaluated = False
        self.open = True

    def __repr__(self):
        display = f'Node ({self.height}, {self.width}) - '
        if self.evaluated:
            display += f'Price : {self.price}\n' \
                       f'Profit : {self.net_profit}\n'
        else:
            display += 'not yet priced\n'
        return display

    def evaluate(self):
        if not self.evaluated:
            if self.price == 0:
                self.price = self.choice.price
                self.net_profit = self.choice.profit * self.price
            else:
                self.net_profit += self.choice.price * self.choice.profit
                self.price += self.choice.price
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
        self.nodes = [[Node(0, 0, Choice(0, 0, 0, {}), 0, 0)]]
        self.branch = []

    def define_choices_optimised(self, action, cap):
        self.choices = []
        for i in range(how_many_shares(action.price, cap) + 1):
            self.choices.append(Choice(f"{i} action(s) {action.id}", i * action.price, action.profit, {action.id: i}))

    def define_choices_brute(self):
        self.choices = []
        for action in self.actions:
            self.choices.append(Choice(action.id, action.price, action.profit, {action.id: 1}))

    def define_choices_knapsack(self, step):
        self.choices = []
        action = self.actions[step]
        self.choices.append(Choice(f"0 {action.id}", 0, 0, {action.id: 0}))
        self.choices.append(Choice(f"1 {action.id}", action.price, action.profit, {action.id: 1}))

    def grow(self, cap):
        i = 0
        min_choice_price = math.inf
        next_nodes = []
        for choice in self.choices:
            min_choice_price = min(min_choice_price, choice.price)

        for node in self.nodes[-1]:
            for choice in self.choices:
                if node.price + choice.price <= cap:
                    new_node = Node(node.height + 1, i, choice, node.price, node.net_profit)
                    new_node.history.update(node.history)
                    new_node.history.update(choice.composition)
                    new_node.evaluate()
                    next_nodes.append(new_node)
                    i += 1
        self.nodes.append(next_nodes)

    def second_algo(self, cap):
        for num_action in range(len(self.actions)):
            self.define_choices_optimised(self.actions[num_action], cap)
            self.grow(cap)
        return self.nodes[-1]

    def knapsack(self, cap):
        step = 0
        for num_action in range(len(self.actions)):
            self.define_choices_knapsack(step)
            self.grow(cap)
            step += 1
        return self.nodes[-1]


def sort_results(results):
    sorted_results = sorted(results, key=attrgetter("price"))
    sorted_results = sorted(sorted_results, key=attrgetter("net_profit"), reverse=True)
    display = display_cell_length('Actions achetées', 50) + ' | '\
              + display_cell_length('Price', 12) + ' | '\
              + display_cell_length('Profit', 12) + '\n'
    for node in sorted_results[:100]:
        composition = ""
        for action, num in node.history.items():
            if num != 0:
                composition += f"{num} {action} - "
        display += display_cell_length(composition[:-2], 50) + ' | ' \
                   + display_cell_length(node.price, 12) + ' | ' \
                   + display_cell_length(node.net_profit, 12) + '\n'
    print(display)


def best_result(results):
    best_node = Node(0, 0, Choice(0, 0, 0, {}), math.inf, 0)
    best_nodes = [best_node]
    for node in results:
        if node.net_profit > best_node.net_profit:
            best_node = node
            best_nodes = [best_node]
        elif node.net_profit == best_node.net_profit:
            if node.price == node:
                best_nodes.append(node)
            elif node.price < best_node.price:
                best_node = node
                best_nodes = [best_node]
    if len(best_nodes) > 1:
        display = f"{len(best_nodes)} best results:\n"
        for node in best_nodes:
            composition = ""
            for action, num in node.history.items():
                if num != 0:
                    composition += f"{num} {action} - "
            display += composition[:-2] + '\n' \
                       + str(node.price) + '\n' \
                       + str(node.net_profit)
    else:
        display = ""
        composition = ""
        for action, num in best_node.history.items():
            if num != 0:
                composition += f"{num} {action} - "
        display += composition[:-2] + '\n' \
                   + str(best_node.price) + '\n' \
                   + str(best_node.net_profit)
    print(display)


if __name__ == '__main__':

    """ Tests data """
    """    #1
    names1 = [1, 2, 3]
    prices1 = [15, 30, 40]
    profits1 = [0.10, 0.17, 0.25]
    min_price1 = 10

    portfolio1 = Portfolio()
    portfolio1.initialize(names1, prices1, profits1)
    tree1 = Tree(portfolio1.actions)
    cap1 = 100

    #sort_results(tree1.knapsack(cap1))

    #2
    namestry = ['01', '02', '03', '04', '05', '06']
    pricestry = [10, 15, 25, 35, 30, 40]
    profitstry = [0.05, 0.1, 0.15, 0.2, 0.17, 0.25]
    captry = 100
    min_pricetry = min(pricestry)

    try_portfolio = Portfolio()
    try_portfolio.initialize(namestry, pricestry, profitstry)
    try_tree = Tree(try_portfolio.actions)
    #sort_results(try_tree.knapsack(captry))"""
    """ data """

    names, prices, profits = import_actions_data('dataForceBrute.csv')
    cap = 400
    market = Portfolio()
    market.initialize(names, prices, profits)
    next_nodes = []
    for action in market.actions:
        next_nodes.append(Portfolio([action]))
    tree = Tree(portfolio.actions)
    cProfile.run('best_result(tree.knapsack(cap))')
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