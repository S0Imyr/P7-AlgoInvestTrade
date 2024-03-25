# Optimized Investment Algorithms

## 1. Summary :
This is a program that, given a set of stocks, will select a portfolio of stocks that will yield the best return for a given amount. The program allows you to select the data and then choose the method.

There are three main methods:
1. Brute Force
2. Greedy
3. Dynamic Programming

The first method should only be applied to a limited number of stocks (less than 25).

## 2. Installation
### Repository Files
1. Clone the repository: `git clone https://github.com/rlossec/Optimized-Investment-Algorithm.git`
2. Navigate to the project folder: `cd Optimized-Investment-Algorithm`
3. Create a virtual environment:
    - Windows: `python -m venv env`
    - macOS/Linux: `python3 -m venv env`
4. Activate the virtual environment:
    - Windows: `./env/Scripts/activate`
    - macOS/Linux: `source env/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`

## 3. Running the Program

To run the program, type in `src` directory: `python main.py`  
You can then navigate between the menus to select stocks and choose the method.

## 4. Tests
### Running Tests
To run tests, execute: `python -m unittest` in the project root directory.

### Writing Tests
Tests are located in the `tests` directory. You can add new test files or expand existing ones to cover more scenarios and edge cases.

## 5. License
This project is licensed under the MIT License. See the `LICENSE` file for more details.


# Algorithmes d'optimisation d'investissement

## 1. Principe :
Il s'agit d'un programme qui à partir d'un ensemble d'actions va sélectionner un portefeuille d'actions qui aura pour un montant donné, le meilleur rendement.
Le programme permet de sélectionner les données, puis sélectionner la méthode.

On distingue trois grandes méthodes :
1. Force brute
2. Glouton
3. Programmation dynamique

La première méthode ne doit être appliquée que sur un nombre d'action restreint (inférieur à 25).

## 2. Installation
### Fichiers du site
Sur le terminal se placer sur un dossier cible.

Puis suivre les étapes suivantes :
1. Cloner le dépôt ici présent en tapant: `git clone https://github.com/rlossec/Optimized-Investment-Algorithm.git`
2. Accéder au dossier ainsi créé avec la commande : `cd Optimized-Investment-Algorithm`
3. Créer un environnement virtuel pour le projet avec 
    - `python -m venv env` sous windows 
    - ou `python3 -m venv env` sous macos ou linux.
4. Activez l'environnement virtuel avec 
    - `source env/Scripts/activate` sous windows 
    - ou `source env/bin/activate` sous MacOS ou Linux.
5. Installez les dépendances du projet avec la commande `pip install -r requirements.txt`

## 3. Lancement du programme

Pour lancer le programme tapper : `python main.py`

Vous pouvez ensuite naviguer entre les menus pour sélectionner des actions, puis la méthode.

## 4. Tests
### Exécution des tests
Pour exécuter les tests, lancez la commande suivante : `python -m unittest` dans le répertoire principal du projet.

### Écriture des tests
Les tests se trouvent dans le répertoire `tests`. Vous pouvez ajouter de nouveaux fichiers de test ou étendre les existants pour couvrir davantage de scénarios et de cas limites.

## 5. Licence
Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus de détails.
