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
            choice = input("\nChoissisez une option en inscrivant "
                           "le nombre associé \n")
            try:
                choice = int(choice)
            except ValueError:
                print("Entrée invalide, donnez l'un des indices de menu")

            if choice in range(len(self.menus)):
                return self.menus[choice]


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
        self.menu.add("Portefeuille réduit", MethodMenu(0))
        self.menu.add("Dataset1", MethodMenu(1))
        self.menu.add("Dataset2", MethodMenu(2))
        self.menu.add("Quitter", ExitMenu())
        self.menu.display_menu()
        user_choice = self.menu.get_user_choice()
        return user_choice()


class MethodMenu:
    def __init__(self, data):
        self.menu = Menu("Méthode")
        self.data = data

    def __call__(self):
        self.menu.add("Force brute", MethodMenu(0))
        self.menu.add("Glouton", MethodMenu(1))
        self.menu.add("Quitter", ExitMenu())
        self.menu.display_menu()
        user_choice = self.menu.get_user_choice()
        return user_choice()


class ExitMenu:
    """ Displays the exit screen """
    def __call__(self):
        print("Aurevoir")
        exit()