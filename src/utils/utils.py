

def display_cell_length(message: str, length: int):
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
