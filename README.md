# Projet-7


### Principe et configuration nécessaire :
Il s'agit d'un programme qui à partir d'un ensemble d'actions va sélectionner un portefeuille d'actions qui aura pour un montant donné, le meilleur rendement.
Le programme permet de sélectionner les données, puis sélectionner la méthode.

On distingue trois grandes méthodes :
1. Force brute
2. Glouton
3. Programmation dynamique

La première méthode ne doit être appliquée que sur un nombre d'action restreint (inférieur à 25).

## Installation
### Fichiers du site
Sur le terminal se placer sur un dossier cible.

Puis suivre les étapes suivantes :
1. Cloner le dépôt ici présent en tapant: `$ git clone https://github.com/S0Imyr/Projet-7.git`
2. Accéder au dossier ainsi créé avec la commande : `$ cd Projet-7`
3. Créer un environnement virtuel pour le projet avec 
    - `$ python -m venv env` sous windows 
    - ou `$ python3 -m venv env` sous macos ou linux.
4. Activez l'environnement virtuel avec 
    - `$ source env/Scripts/activate` sous windows 
    - ou `$ source env/bin/activate` sous MacOS ou Linux.
5. Installez les dépendances du projet avec la commande `$ pip install -r requirements.txt`


### Lancement du programme

6. Pour lancer le programme tapper : `$ python main.py`

Vous pouvez ensuite naviguer entre les menus pour sélectionner des actions, puis la méthode.
