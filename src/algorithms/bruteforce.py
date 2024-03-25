import math
import itertools
from typing import List, Tuple

from models import Portfolio
from utils.importdata import import_shares_data


class Node:
    def __init__(self, height: int, width: int, price: float, net_profit: float, composition):
        self.height = height
        self.width = width
        self.price = price
        self.net_profit = net_profit
        self.composition = composition

    def __repr__(self) -> str:
        return (f'Node ({self.height}, {self.width}) - '
                f'Price: {self.price}\n'
                f'Profit: {self.net_profit}\n')


def list_branches(market: Portfolio, cap: float) -> List[Node]:
    step = 0
    nodes = [Node(step, 0, 0, 0, [])]
    for share in market.shares:
        next_nodes = []
        width = 0
        for node in nodes:
            node.width += 1
            width += 1
            next_nodes.append(node)
            new_price = node.price + share.price
            if new_price < cap:
                new_profit = node.net_profit + share.profit_amount
                new_composition = []
                new_composition.extend(node.composition)
                new_composition.append(share.name)
                next_nodes.append(Node(step, width, new_price, new_profit, new_composition))
            width += 1
        step += 1
        nodes = next_nodes
    return nodes


def best_branch_portfolio(nodes):
    best_branch = Node(0, 0, math.inf, 0, [])
    best_branches = [best_branch]
    for node in nodes:
        if node.profit_amount > best_branch.net_profit:
            best_branch= node
        elif node.profit_amount == best_branch.net_profit:
            if node.price < best_branch.price:
                best_branch = node
            elif node.price == best_branch.price:
                best_branches.append(node)
    if len(best_branches) > 1:
        return best_branches
    else:
        return best_branch


def list_portfolios(market: Portfolio) -> List[List[Tuple[str, float, float]]]:
    """List all possible portfolios."""
    return [list(portfolio) for i in range(len(market)) for portfolio in itertools.combinations(market.shares, i)]


def best_portfolios(portfolios, cap):
    best_portfolio = Portfolio()
    for portfolio in portfolios:
        portfolio_price = 0
        portfolio_profit = 0
        for share in portfolio:
            portfolio_price += share.price
            portfolio_profit += share.profit_amount
        if portfolio_price <= cap and portfolio_profit > best_portfolio.profit_amount:
            best_portfolio = Portfolio()
            best_portfolio.shares = portfolio
            best_portfolio.price = portfolio_price
            best_portfolio.profit_amount = portfolio_profit
    return best_portfolio


def bruteforce(market, cap):
    all_possible_portfolio = list_portfolios(market)
    best_portfolio = best_portfolios(all_possible_portfolio, cap)
    return best_portfolio


if __name__ == '__main__':

    data_file = '../data/dataForceBrute.csv'
    cap = 500
    market = import_shares_data(data_file)
    branches = list_branches(market, cap)
    print(type(list_portfolios(market)[2]))
    branch = best_branch_portfolio(branches)

