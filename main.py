prices = [10, 15, 25, 35, 30, 40, 11, 13, 24, 17, 21, 55, 19, 7, 9, 4, 2, 5, 12, 57]
profits = [0.05, 0.10, 0.15, 0.20, 0.17, 0.25, 0.07, 0.11, 0.13, 0.27, 0.17, 0.09, 0.23, 0.01, 0.03, 0.08, 0.12, 0.14, 0.21, 0.18]

money = 100
pricestry = [10, 15, 25, 35, 30, 40]
profitstry = [0.05, 0.1, 0.15, 0.2, 0.17, 0.25]

min_price = min(pricestry)
possibilities = []
actual_share = 0

total_cost = 0


class Branch:
    def __init__(self):
        self.shares = []


class Share:
    def __init__(self, id, price, profit):
        self.id = id
        self.price = price
        self.profit = profit

    def __repr__(self):
        return f'Share {self.id}: \n' \
               f'Price: {self.price} \n' \
               f'Profit: {self.profit}'

    def evaluate_profit(self):
        return self.price * self.profit / 100


def display_cell_length(message, length):
    if len(str(message)) > length:
        return str(message)[:length]
    else:
        return str(message) + " " * (length - len(str(message)))

class Portfolio:
    def __init__(self):
        self.shares = []

    def initialize(self, prices, profits):
        if len(prices) != len(profits):
            print("The prices data and the profits data must coincide. The number of element don't match")
        else:
            for num_share in range(len(prices)):
                self.shares.append(Share(num_share, prices[num_share], profits[num_share]))

    def __repr__(self):
        display = display_cell_length('Share', 12) + ' | ' + display_cell_length('Price', 12) + ' | ' + display_cell_length('Profit', 12) + '\n'
        for share in self.shares:
            display += display_cell_length(share.id, 12) + ' | ' + display_cell_length(share.price, 12) + ' | ' + display_cell_length(share.profit, 12) + '\n'
        return display


def available_shares(list_shares, money):
    pass

def how_many_shares(share_price, money):
    return money // share_price


def can_i_add_share(cost, money):
    pass


def add_share(share_id):
    pass


possibility = []
possibility_cost = 0
possibility_profit = 0

"""while possibility_cost + min_price < money:
    

    if total_cost + pricestry[actual_share]:
        total_cost += pricestry[actual_share]
        total_profit += pricestry[actual_share] * profitstry[actual_share]
    else:
        actual_share += 1"""

if __name__ == "__main__":

    try_portfolio = Portfolio()
    try_portfolio.initialize(pricestry, profitstry)
    share_option = []
    for share in try_portfolio.shares:
        for i in range(how_many_shares(share.price, money)):
            share_option.append(share)

    print(share_option)
    print(try_portfolio)

"""    for num_share in range(len(how)):
        for j in range(how[num_share]):
            possibility = []"""



