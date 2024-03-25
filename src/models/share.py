
class Share:
    """Share model"""
    def __init__(self, name, price, profit_percentage):
        if price < 0 or profit_percentage < 0:
            raise ValueError("Price and profit percentage must be non-negative.")
        self.name = name
        self.price = price
        self.profit_percentage = profit_percentage

    @property
    def profit_amount(self):
        """Calculate and return the net profit."""
        return self.price * self.profit_percentage / 100

    def __repr__(self):
        return f'Action {self.name}: \n' \
               f'Price: {self.price} \n' \
               f'Profit: {self.profit_percentage}%'



if __name__ == '__main__':
    # Création
    share = Share("Company A", 100, 5)
    print("Nom", share.name,  "Company A")
    print("Prix", share.price, 100)
    print("Profit en %", share.profit_percentage, 5)
    print("Montant", share.profit_amount, 5)

    # Montant
    share1 = Share("ABC", 10, 5)
    print("Montant", share1.profit_amount, 0.5)

        # Test with zero price and profit
    share2 = Share("XYZ", 0, 0)
    print("Montant", share2.profit_amount, 0)

    # Test with negative profit
    # share3 = Share("DEF", 20, -2)
    # Test with negative price
    # share3 = Share("DEF", -20, 2)