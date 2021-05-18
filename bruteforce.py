import math
import itertools
from os import popen

from finance import Portfolio
from importdata import import_actions_data


class Node:
    def __init__(self, height, width, price, net_profit, composition):
        self.height = height
        self.width = width
        self.price = price
        self.net_profit = net_profit
        self.composition = composition

    def __repr__(self):
        display = f'Node ({self.height}, {self.width}) - '
        display += f'Price : {self.price}\n' \
                   f'Profit : {self.net_profit}\n'
        return display


def list_branches(market, cap):
    step = 0
    nodes = [Node(step, 0, 0, 0, [])]
    for action in market.actions:
        next_nodes = []
        width = 0
        for node in nodes:
            node.width += 1
            width += 1
            next_nodes.append(node)
            new_price = node.price + action.price
            if new_price < cap:
                new_profit = node.net_profit + action.net_profit
                new_composition = []
                new_composition.extend(node.composition)
                new_composition.append(action.name)
                next_nodes.append(Node(step, width, new_price, new_profit, new_composition))
            width += 1
        step += 1
        nodes = next_nodes
    return nodes


def best_branch_portfolio(nodes):
    best_branch = Node(0, 0, math.inf, 0, [])
    best_branches = [best_branch]
    for node in nodes:
        if node.net_profit > best_branch.net_profit:
            best_branch= node
        elif node.net_profit == best_branch.net_profit:
            if node.price < best_branch.price:
                best_branch = node
            elif node.price == best_branch.price:
                best_branches.append(node)
    if len(best_branches) > 1:
        return best_branches
    else:
        return best_branch


def list_portfolios(market):
    portfolios = []
    for i in range(len(market)):
        portfolios.extend(itertools.combinations(market, i))
    return portfolios


def best_portfolios(portfolios, cap):
    best_portfolio = Portfolio()
    for portfolio in portfolios:
        portfolio_price = 0
        portfolio_profit = 0
        for action in portfolio:
            portfolio_price += action.price
            portfolio_profit += action.net_profit
        if portfolio_price <= cap and portfolio_profit > best_portfolio.profit:
            best_portfolio = Portfolio()
            best_portfolio.actions = portfolio
            best_portfolio.price = portfolio_price
            best_portfolio.profit = portfolio_profit
    return best_portfolio


def bruteforce(market, cap):
    all_possible_portfolio = list_portfolios(market.actions)
    best_portfolio = best_portfolios(all_possible_portfolio, cap)
    return best_portfolio


if __name__ == '__main__':
    import cProfile
    from views import display_best_branch
    "cProfile.run('results()')"
    data_file='data/dataForceBrute.csv'
    cap = 500
    names, prices, profits = import_actions_data(data_file)
    market = Portfolio()
    market.add_data_actions(names, prices, profits)
    branches = list_branches(market, cap)
    branch = best_branch_portfolio(branches)
    display_best_branch(branch)

