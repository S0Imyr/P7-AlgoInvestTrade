import math
import cProfile

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


def knapsack_node(market, cap):
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


def best_portfolio(nodes):
    best_node = Node(0, 0, math.inf, 0, [])
    best_nodes = [best_node]
    for node in nodes:
        if node.net_profit > best_node.net_profit:
            best_node = node
        elif node.net_profit == best_node.net_profit:
            if node.price < best_node.price:
                best_node = node
            elif node.price == best_node.price:
                best_nodes.append(node)
    if len(best_nodes) > 1:
        return best_nodes
    else:
        return best_node


def results():
    cap0 = 500
    names, prices, profits = import_actions_data('dataForceBrute.csv')
    market1 = Portfolio([])
    market1.convert_to_action(names, prices, profits)
    result = best_portfolio(knapsack_node(market1, cap0))
    print(result.composition)
    print(result.price)
    print(result.net_profit)


if __name__ == '__main__':
    cProfile.run('results()')
