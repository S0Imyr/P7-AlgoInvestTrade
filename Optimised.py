from finance import Portfolio
from operator import attrgetter
from importdata import import_actions_data
from bruteforce import best_portfolio, knapsack


def clean_up(portfolio):
    available_actions = []
    total_price = 0
    for action in portfolio.actions:
        if action.price > 0 and action.profit > 0:
            available_actions.append(action)
            total_price += action.price
    portfolio.actions = available_actions


def select(portfolio, num_select):
    sorted_action_by_profit = sorted(portfolio.actions, key=attrgetter("profit"), reverse=True)
    return Portfolio(sorted_action_by_profit[:num_select])


if __name__ == '__main__':
    cap0 = 500

    names, prices, profits = import_actions_data('dataset1_Python+P7.csv')
    market1 = Portfolio([])
    market1.convert_to_action(names, prices, profits)
    clean_up(market1)
    select_market1 = select(market1, 20)

    result = best_portfolio(knapsack(select_market1, cap0))
    print(result.composition)
    print(result.price)
    print(result.net_profit)

    names, prices, profits = import_actions_data('dataset2_Python+P7.csv')
    market2 = Portfolio([])
    market2.convert_to_action(names, prices, profits)
    clean_up(market2)
    select_market2 = select(market2, 20)

    result = best_portfolio(knapsack(select_market2, cap0))
    print(result.composition)
    print(result.price)
    print(result.net_profit)
