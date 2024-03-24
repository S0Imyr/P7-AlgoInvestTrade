import math
from operator import attrgetter

from utils.tree import TreeNode, ShareChoice


def display_cell_length(message, length):
    if len(str(message)) > length:
        return str(message)[:length]
    else:
        return str(message) + " " * (length - len(str(message)))


def input_positive_integer(message: str) -> int:
    while True:
        try:
            number = int(input(message))
            if number <= 0:
                print("Le nombre doit être positif.")
            else:
                return number
        except ValueError:
            print("Veuillez entrer un nombre entier.")


def display_sorted_results(results):
    sorted_results = sorted(results, key=attrgetter("price", "net_profit"), reverse=True)
    display = display_cell_length('Actions achetées', 50) + ' | '\
              + display_cell_length('Price', 12) + ' | '\
              + display_cell_length('Profit', 12) + '\n'
    for node in sorted_results[:100]:
        composition = ""
        for action, num in node.history.items():
            if num != 0:
                composition += f"{num} {action} - "
        display += display_cell_length(composition[:-2], 50) + ' | ' \
                   + display_cell_length(node.price, 12) + ' | ' \
                   + display_cell_length(node.net_profit, 12) + '\n'
    print(display)


def display_best_result(results):
    best_node = TreeNode(0, 0, ShareChoice(0, 0, 0, {}), math.inf, 0)
    best_nodes = [best_node]
    for node in results:
        if node.net_profit > best_node.net_profit:
            best_node = node
            best_nodes = [best_node]
        elif node.net_profit == best_node.net_profit:
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


if __name__ == '__main__':
    pass
