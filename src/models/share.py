
class Share:
    """Share model representing a stock or share."""
    def __init__(self, name: str, price: float, profit_percentage: float):
        """
        Initialize a Share instance.

        Args:
            name: The name or identifier of the share.
            price The price of the share.
            profit_percentage: The profit percentage of the share.

        Raises:
            ValueError: If price or profit_percentage is not positive.
        """
        if price <= 0 or profit_percentage <= 0:
            raise ValueError("Price and profit percentage must be positive.")
        self.name = name
        self.price = price
        self.profit_percentage = profit_percentage

    @property
    def profit_amount(self) -> float:
        """Calculate and return the amount of profit of the share."""
        return self.price * self.profit_percentage / 100

    def __repr__(self) -> str:
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

    # Tests avec des valeurs négatives
    try:
        share3 = Share("DEF", 20, -2)
    except ValueError as e:
        print(e)
    try:
        share4 = Share("GHI", -20, 2)
    except ValueError as e:
        print(e)
    # Tests avec des valeurs nulles
    try:
        share3 = Share("DEF", 20, 0)
    except ValueError as e:
        print(e)

    try:
        share4 = Share("GHI", 0, 2)
    except ValueError as e:
        print(e)
