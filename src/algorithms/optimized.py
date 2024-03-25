import numpy as np
import math
from operator import attrgetter

from models import Portfolio
from algorithms.bruteforce import bruteforce


def greedy(market, cap):
    shares_sorted_by_profit = sorted(market.shares, key=attrgetter("profit_percentage"), reverse=True)
    portfolio = Portfolio()
    for share in shares_sorted_by_profit:
        if portfolio.price + share.price < cap:
            portfolio.add_share(share)
    return portfolio


def n_best_shares(portfolio, num_select):
    portfolio_select = Portfolio()
    portfolio_select.shares = sorted(portfolio.shares, key=attrgetter("profit_percentage"), reverse=True)[:num_select]
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


def bruteforce_with_n_best_shares(market, cap, n):
    market_selection = n_best_shares(market, n)
    portfolio = bruteforce(market_selection, cap)
    return portfolio


def KS_dynamic(market, cap, ndigits=0):
    prices = []
    for share in market.shares:
        prices.append(math.ceil(share.price * (10 ** ndigits)))
    num_shares = dynamic_programming(price_cap=math.ceil(cap * (10 ** ndigits)), prices=prices, profits=market.list_profit_amounts())
    portfolio = Portfolio()
    shares = []
    for num_share in num_shares:
        shares.append(market.shares[num_share - 1])
    portfolio.add_shares(shares)
    return portfolio


if __name__ == '__main__':
    pass
    # "data\dataForceBrute.csv"
    # "data\dataset1_Python+P7.csv"
    # "data\dataset2_Python+P7.csv"
    # market = import_shares_data(file=r"data\dataset1_Python+P7.csv")

    # KS_dynamic(market, 500, ndigits=2)

    # portfolio = Portfolio()
