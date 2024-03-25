
from operator import attrgetter


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
    display = (display_cell_length('Actions achetées', 50) + ' | '
               + display_cell_length('Price', 12) + ' | '
               + display_cell_length('Profit', 12) + '\n')
    for node in sorted_results[:100]:
        composition = ""
        for share, num in node.history.items():
            if num != 0:
                composition += f"{num} {share} - "
        display += (display_cell_length(composition[:-2], 50) + ' | '
                    + display_cell_length(node.price, 12) + ' | '
                    + display_cell_length(node.profit_amount, 12) + '\n')
    print(display)


if __name__ == '__main__':
    pass
