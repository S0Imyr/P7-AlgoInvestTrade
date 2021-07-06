import time

from importdata import import_actions_data
from bruteforce import bruteforce
from optimised import KS_dynamic, greedy, bruteforce_with_n_best_actions
from views import display_best_portfolio


def input_cap():
    cap = 0
    while cap <= 0:
        cap = input("Quel est le montant maximal pour le portefeuille ? \n")
        try:
            cap = float(cap)
            if cap <= 0:
                print("Le montant doit être positif.")
        except ValueError:
            print("Veuillez donner un nombre décimal.")
    return cap


def input_number_of_actions():
    number_best_actions = 0
    while number_best_actions <= 0:
        number_best_actions = input("Sur quel nombre d'actions voulez vous travailler ? \n")
        try:
            number_best_actions = int(number_best_actions)
            if number_best_actions <= 0:
                print("Le montant doit être positif.")
        except ValueError:
            print("Veuillez donner un nombre entier.")
    return number_best_actions


def input_number_of_decimals():
    try:
        number_of_decimals = int(input("Pour la précision sur les prix, combien de décimales ? \n"))
        if number_of_decimals <= 0:
            print("Le montant doit être positif.")
    except ValueError:
        print("Veuillez donner un nombre entier.")
    return number_of_decimals

class Menu:
    def __init__(self, name):
        self.name = name
        self.options = []
        self.menus = []

    def add(self, option, menu):
        """ Allows to add entries and their handler to the menu"""
        self.options.append(option)
        self.menus.append(menu)

    def display_menu(self):
        display = f"\n{self.name} : \n \n"
        for key, option in enumerate(self.options):
            display += f"{key}. {option}\n"
        print(display)

    def get_user_choice(self):
        """ Asks to input the key corresponding to the desired option. """
        while True:
            self.display_menu()
            choice = input("Choissisez une option en inscrivant "
                           "le nombre associé \n")
            try:
                self.choice = int(choice)
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
        self.menu.add("Portefeuille réduit", MethodMenu(data_file="data\dataForceBrute.csv"))
        self.menu.add("Dataset1", MethodMenu(data_file="data\dataset1_Python+P7.csv"))
        self.menu.add("Dataset2", MethodMenu(data_file="data\dataset2_Python+P7.csv"))
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
        cap = input_cap()
        start_time = time.time()
        if self.menu.choice == 0:
            portfolio = bruteforce(market, cap=cap)
        elif self.menu.choice == 1:
            portfolio = greedy(market=market, cap=cap)
        elif self.menu.choice == 2:
            number_best_actions = input_number_of_actions()
            portfolio = bruteforce_with_n_best_actions(market=market, cap=cap, n=number_best_actions)
        elif self.menu.choice == 3:
            number_of_decimals = input_number_of_decimals()
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
