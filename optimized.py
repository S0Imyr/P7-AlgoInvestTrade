import numpy as np
import math
from operator import attrgetter

from finance import Portfolio
from bruteforce import bruteforce


def greedy(market, cap):
    actions_sorted_by_profit = sorted(market.actions, key=attrgetter("profit"), reverse=True)
    portfolio = Portfolio()
    for action in actions_sorted_by_profit:
        if portfolio.price + action.price < cap:
            portfolio.add_actions([action])
    return portfolio


def n_best_actions(portfolio, num_select):
    portfolio_select = Portfolio()
    portfolio_select.actions = sorted(portfolio.actions, key=attrgetter("profit"), reverse=True)[:num_select]
    return portfolio_select


def dynamic_programming(price_cap, prices, profits):
    """ Resolution of Knapsack with dynamic programmation"""
    number_of_shares = len(prices)
    f = np.zeros(shape=(number_of_shares + 1, price_cap + 1))
    f_shares_composition = [[[] for x in range(price_cap + 1)] for y in range(number_of_shares + 1)]
    for share in range(1, number_of_shares + 1):
        for cap in range(price_cap + 1):
            if prices[share - 1] <= cap:
                if f[share - 1, cap] > f[share - 1, cap - prices[share - 1]] + profits[share - 1]:
                    f[share, cap] = f[share - 1, cap]
                    f_shares_composition[share][cap] = f_shares_composition[share - 1][cap]
                else:
                    f[share, cap] = f[share - 1, cap - prices[share - 1]] + profits[share - 1]
                    f_shares_composition[share][cap] = f_shares_composition[share - 1][cap - prices[share - 1]] + [share]
            else:
                f[share, cap] = f[share - 1, cap]
                f_shares_composition[share][cap] = f_shares_composition[share - 1][cap]
    return f_shares_composition[-1][-1]


def bruteforce_with_n_best_actions(market, cap, n):
    market_selection = n_best_actions(market, n)
    portfolio = bruteforce(market_selection, cap)
    return portfolio


def KS_dynamic(market, cap, ndigits=0):
    prices = []
    for action in market.actions:
        prices.append(math.ceil(action.price * (10 ** ndigits)))
    num_actions = dynamic_programming(price_cap=math.ceil(cap * (10 ** ndigits)), prices=prices, profits=market.net_profits())
    portfolio = Portfolio()
    actions = []
    for num_action in num_actions:
        actions.append(market.actions[num_action-1])
    portfolio.add_actions(actions)
    return portfolio

if __name__ == '__main__':
    pass
    # "data\dataForceBrute.csv"
    # "data\dataset1_Python+P7.csv"
    # "data\dataset2_Python+P7.csv"
    # market = import_actions_data(file=r"data\dataset1_Python+P7.csv")

    # KS_dynamic(market, 500, ndigits=2)

    # portfolio = Portfolio()
