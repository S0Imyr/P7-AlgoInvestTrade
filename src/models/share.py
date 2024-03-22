

class Share:
    """Create an action object and calculate the net_profit"""
    def __init__(self, name, price, profit):
        self.name = name
        self.price = price
        self.profit = profit
        self.net_profit = self.price * self.profit / 100

    def __repr__(self):
        return f'Action {self.name}: \n' \
               f'Price: {self.price} \n' \
               f'Profit: {self.profit}%'
