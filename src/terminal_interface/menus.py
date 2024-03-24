import time

from algorithms.tree import display_best_portfolio
from utils.importdata import import_actions_data

from algorithms.bruteforce import bruteforce
from algorithms.optimized import KS_dynamic, greedy, bruteforce_with_n_best_actions
from utils.utils import input_positive_integer

DATA_PATH = 'data/'

REDUCE_PORTFOLIO_PATH = "dataForceBrute.csv"
PORTFOLIO_1_PATH = "dataset1_Python+P7.csv"
PORTFOLIO_2_PATH = "dataset2_Python+P7.csv"


class Menu:
    def __init__(self, name: str):
        self.name = name
        self.options = []
        self.menus = []

    def add(self, option: str, menu):
        """ Allows to add entries and their handler to the menu"""
        self.options.append(option)
        self.menus.append(menu)

    def display(self) -> None:
        print(f"\n{self.name} : \n")
        for idx, option in enumerate(self.options):
            print(f"{idx}. {option}")

    def get_user_choice(self):
        """ Asks to input the key corresponding to the desired option. """
        while True:
            self.display()
            try:
                self.choice = int(input("Choissisez une option en inscrivant "
                               "le nombre associé \n"))
            except ValueError:
                print("Entrée invalide, donnez l'un des indices de menu")
            if self.choice in range(len(self.menus)):
                return self.menus[self.choice]


class BrowseMenus:
    """ Handles the navigation between menus. """
    def __init__(self):
        """ The attribute stores the next menu."""
        self.next_menu = None

    def start(self):
        """
        Launches the home menu.
        A loop while to browse between the menus.
        :return: None
        """
        self.next_menu = HomeMenu()
        while self.next_menu:
            self.next_menu()


class HomeMenu:
    def __init__(self):
        self.menu = Menu("Accueil")

    def __call__(self):
        self.menu.add("Choisir les données", DataMenu())
        self.menu.add("Quitter", ExitMenu())
        user_choice = self.menu.get_user_choice()
        return user_choice()


class DataMenu:
    def __init__(self):
        self.menu = Menu("Données")

    def __call__(self):
        self.menu.add("Portefeuille réduit", MethodMenu(data_file=DATA_PATH + REDUCE_PORTFOLIO_PATH))
        self.menu.add("Dataset1", MethodMenu(data_file=DATA_PATH + PORTFOLIO_1_PATH))
        self.menu.add("Dataset2", MethodMenu(data_file=DATA_PATH + PORTFOLIO_2_PATH))
        self.menu.add("Quitter", ExitMenu())
        user_choice = self.menu.get_user_choice()
        return user_choice()


class MethodMenu:
    def __init__(self, data_file):
        self.menu = Menu("Méthode")
        self.data_file = data_file

    def __call__(self):
        self.menu.add("Force brute", MethodMenu(data_file=self.data_file))
        self.menu.add("Glouton", MethodMenu(data_file=self.data_file))
        self.menu.add("Force brute sur les meilleurs profits (%)", MethodMenu(data_file=self.data_file))
        self.menu.add("Programmation dynamique", MethodMenu(data_file=self.data_file))
        self.menu.add("Retour au menu principal", HomeMenu())
        self.menu.add("Quitter", ExitMenu())
        user_choice = self.menu.get_user_choice()
        market = import_actions_data(file=self.data_file)
        if isinstance(user_choice, ExitMenu) or isinstance(user_choice, HomeMenu):
            return user_choice()
        cap = input_positive_integer("Quel est le montant maximal pour le portefeuille ? \n")
        start_time = time.time()
        if self.menu.choice == 0:
            portfolio = bruteforce(market, cap=cap)
        elif self.menu.choice == 1:
            portfolio = greedy(market=market, cap=cap)
        elif self.menu.choice == 2:
            number_best_actions = input_positive_integer("Sur quel nombre d'actions voulez vous travailler ? \n")
            portfolio = bruteforce_with_n_best_actions(market=market, cap=cap, n=number_best_actions)
        elif self.menu.choice == 3:
            number_of_decimals = input_positive_integer("Pour la précision sur les prix, combien de décimales ? \n")
            portfolio = KS_dynamic(market=market, cap=cap, ndigits=number_of_decimals)
        end_time = time.time()
        display_best_portfolio(portfolio)
        print(f"Temps d'exécution : {int((end_time - start_time)//60)} min {int(round((end_time - start_time)%60, ndigits=0))} s.")
        return user_choice()


class ExitMenu:
    """ Displays the exit screen """
    def __call__(self):
        print("Aurevoir")
        exit()


if __name__ == "__main__":
    browse_menus = BrowseMenus()
    browse_menus.start()
