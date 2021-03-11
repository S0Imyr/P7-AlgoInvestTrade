prices = [10, 15, 25, 35, 30, 40, 11, 13, 24, 17, 21, 55, 19, 7, 9, 4, 2, 5, 12, 57]
profits = [0.05, 0.10, 0.15, 0.20, 0.17, 0.25, 0.07, 0.11, 0.13, 0.27, 0.17, 0.09, 0.23, 0.01, 0.03, 0.08, 0.12, 0.14, 0.21, 0.18]

money = 100
pricestry = [10, 15, 25, 35, 30, 40]
profitstry = [0.05, 0.1, 0.15, 0.2, 0.17, 0.25]

min_price = min(pricestry)
possibilities = []
actual_share = 0

total_cost = 0


def serialize_shares(prices_list, profits_list):
    shares = {}
    for num_share in range(len(prices_list)):
        shares[num_share] = {}
        shares[num_share]['price'] = prices_list[num_share]
        shares[num_share]['profits'] = profits_list[num_share]
    return shares


def how_many_shares(cost, money):
    return money // cost


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
    how = []
    for share in pricestry:
        how.append(how_many_shares(share, money))
    print(how)
    print(serialize_shares(prices, profits))
"""    for num_share in range(len(how)):
        for j in range(how[num_share]):
            possibility = []"""



