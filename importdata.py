import csv
from finance import Portfolio


def clean_up(portfolio):
    """ With a portfolio of shares, select the shares where price and profit are both strictly positives"""
    available_actions = []
    total_price = 0
    for action in portfolio.actions:
        if action.price > 0 and action.profit > 0:
            available_actions.append(action)
            total_price += action.price
    portfolio.actions = available_actions


def import_actions_data(file):
    """Import shares data from a file and return three lists of names, prices, profits"""
    names, prices, profits = [], [], []
    with open(file, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            if row[0] != 'name':
                names.append(row[0])
            if row[1] != 'price':
                prices.append(float(row[1]))
            if row[2] != 'profit':
                profits.append(float(row[2]))
    market = Portfolio()
    market.add_data_actions(names, prices, profits)
    clean_up(market)
    return market
