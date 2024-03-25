import math
from algorithms.bruteforce import list_branches, best_branch_portfolio
from models import Portfolio
from utils.data_import import import_shares_data


def how_many_shares(action_price, money):
    return int(money / action_price)


class ShareChoice:
    def __init__(self, name, price, profit, composition):
        self.name = name
        self.price = price
        self.profit = profit
        self.composition = composition

    def __repr__(self):
        return f'{self.name}: \n' \
               f'Price: {self.price} \n' \
               f'Profit: {self.profit} \n'


class TreeNode:
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
                self.net_profit = self.choice.profit_percentage * self.price
            else:
                self.net_profit += self.choice.price * self.choice.profit_percentage
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
        self.nodes = [[TreeNode(0, 0, ShareChoice(0, 0, 0, {}), 0, 0)]]
        self.branch = []

    def define_choices_optimised(self, action, cap):
        self.choices = []
        for i in range(how_many_shares(action.price, cap) + 1):
            self.choices.append(ShareChoice(f"{i} action(s) {action.id}", i * action.price, action.profit_percentage, {action.id: i}))

    def define_choices_brute(self):
        self.choices = []
        for action in self.actions:
            self.choices.append(ShareChoice(action.id, action.price, action.profit_percentage, {action.id: 1}))

    def define_choices_knapsack(self, step):
        self.choices = []
        action = self.actions[step]
        self.choices.append(ShareChoice(f"0 {action.id}", 0, 0, {action.id: 0}))
        self.choices.append(ShareChoice(f"1 {action.id}", action.price, action.profit_percentage, {action.id: 1}))

    def grow(self, cap):
        i = 0
        min_choice_price = math.inf
        next_nodes = []
        for choice in self.choices:
            min_choice_price = min(min_choice_price, choice.price)

        for node in self.nodes[-1]:
            for choice in self.choices:
                if node.price + choice.price <= cap:
                    new_node = TreeNode(node.height + 1, i, choice, node.price, node.net_profit)
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


def display_best_result(results):
    best_node = TreeNode(0, 0, ShareChoice(0, 0, 0, {}), math.inf, 0)
    best_nodes = [best_node]
    for node in results:
        if node.profit_amount > best_node.net_profit:
            best_node = node
            best_nodes = [best_node]
        elif node.profit_amount == best_node.net_profit:
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


def display_portfolio(portfolio: Portfolio):
    print(f"\nLe portefeuille : \n "
          f"\nComposition: \n \n{portfolio} \n"
          f"Pour un prix total de {portfolio.price:.2f} \n"
          f"Pour un pourcentage de profit de {portfolio.profit_percentage:.2f}%\n"
          f"Pour un montant de profit de {portfolio.profit_amount:.2f}"
          )


def display_best_branch(branch):
    composition = ""
    for action in branch.composition:
        composition += f"{action} \n"
    print(f"\nLe meilleur portefeuille trouvé : \n "
          f"\nComposition: \n \n{composition} "
          f"\nPour un prix total de {branch.price:.2f} "
          f"\nPour un profit total de {branch.profit_amount:.2f}")


if __name__ == '__main__':

    data_file = '../data/dataForceBrute.csv'
    cap = 500
    market = import_shares_data(data_file)
    branches = list_branches(market, cap)
    branch = best_branch_portfolio(branches)
    display_best_branch(branch)
