import cProfile

from finance import Portfolio
from operator import attrgetter
from importdata import import_actions_data, clean_up
from bruteforce import best_portfolio, bruteforce, knapsack


def greedy(market, cap):
    actions_sorted_by_profit = sorted(market.actions, key=attrgetter("profit"), reverse=True)
    portfolio = Portfolio()
    for action in actions_sorted_by_profit:
        if portfolio.price < cap:
            portfolio.add_actions([action])
    return portfolio


def n_best_actions(portfolio, num_select):
    sorted_action_by_profit = sorted(portfolio.actions, key=attrgetter("profit"), reverse=True)
    return Portfolio(sorted_action_by_profit[:num_select])


def knapSack_DP(price_cap, prices, profits, number_of_shares):
    """ Resolution of Knapsack with dynamic programmation"""
    f = [[0 for x in range(price_cap + 1)] for x in range(number_of_shares + 1)]
 
    for share in range(number_of_shares + 1):
        for cap in range(price_cap + 1):
            if share == 0 or cap == 0:
                f[share][cap] = 0
            elif prices[share-1] <= cap:
                f[share][cap] = max(profits[share-1]
                          + f[share-1][cap-prices[share-1]], 
                              f[share-1][cap])
            else:
                f[share][cap] = f[share-1][cap]
 
    return f[number_of_shares][price_cap]
 

def knapsack_Memoization(prices, val, price_cap, n):
    """ Resolution of Knapsack with  memoization technique (an extension of recursive approach)"""
    t = [[-1 for i in range(price_cap + 1)] for j in range(n + 1)]

    if n == 0 or price_cap == 0:
        return 0
    if t[n][price_cap] != -1:
        return t[n][price_cap]
    if prices[n-1] <= price_cap:
        t[n][price_cap] = max(
            val[n-1] + knapsack_Memoization(
                prices, val, price_cap-prices[n-1], n-1),
            knapsack_Memoization(prices, val, price_cap, n-1))
        return t[n][price_cap]
    elif prices[n-1] > price_cap:
        t[n][price_cap] = knapsack_Memoization(prices, val, price_cap, n-1)
        return t[n][price_cap]


def bruteforce_with_n_best_actions(market, cap, n):
    market_selection = n_best_actions(market, n)
    portfolio = bruteforce(market_selection, cap)
    return portfolio


def resultsdata2():
    cap0 = 500
    names, prices, profits = import_actions_data('dataset2_Python+P7.csv')
    market2 = Portfolio([])
    market2.convert_to_action(names, prices, profits)
    clean_up(market2)
    select_market2 = n_best_actions(market2, 23)
    result = best_portfolio(knapsack(select_market2, cap0))
    print(result.composition)
    print(result.price)
    print(result.net_profit)


if __name__ == '__main__':
    cProfile.run('resultsdata1()')
    cProfile.run('resultsdata2()')
