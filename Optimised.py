import cProfile
from typing import List
import numpy as np


from finance import Portfolio
from operator import attrgetter
from importdata import import_actions_data, clean_up
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


def dynamic_programming(price_cap, prices, profits, step=1):
    """ Resolution of Knapsack with dynamic programmation"""
    number_of_shares = len(prices)
    capacities = round(price_cap / step) + 1
    f = np.zeros(shape=(number_of_shares + 1, capacities))
    f_shares_composition = np.full(fill_value="", dtype='U100', shape=(number_of_shares + 1, capacities))


    for share in range(1, number_of_shares + 1):
        for cap in range(capacities):
            if prices[share - 1] <= cap:
                if f[share - 1, cap] > f[share - 1, cap - prices[share - 1]] + profits[share - 1]:
                    f[share, cap] = f[share - 1, cap]
                    f_shares_composition[share, cap] = f_shares_composition[share - 1, cap]
                else:
                    f[share, cap] = f[share - 1, cap - prices[share - 1]] + profits[share - 1]
                    f_shares_composition[share, cap] = f_shares_composition[share - 1, cap - prices[share - 1]] + f"Action {share} - "

            else:
                f[share, cap] = f[share - 1, cap]
                f_shares_composition[share, cap] = f_shares_composition[share - 1, cap]
    return f[-1, -1], f_shares_composition[-1, -1]


def bruteforce_with_n_best_actions(market, cap, n):
    market_selection = n_best_actions(market, n)
    portfolio = bruteforce(market_selection, cap)
    return portfolio
