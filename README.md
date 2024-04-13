# Automate Fini Déterministe

Ce projet implémente une classe `Automate` permettant de manipuler des automates finis déterministes (AFD). La classe `Automate` fournit des méthodes pour ajouter des états, des transitions, des symboles à l'alphabet, ainsi que pour sauvegarder et charger un automate à partir d'un fichier.

## Fonctionnalités

- Création et manipulation d'automates finis déterministes
- Ajout d'états, de transitions et de symboles à l'alphabet
- Sauvegarde et chargement d'un automate à partir d'un fichier texte
- Affichage graphique de l'automate à l'aide de la bibliothèque GraphViz

## Utilisation

Le code principal se trouve dans le fichier `main.py` dans le répertoire `src`. Pour lancer le programme, exécutez le fichier `main.py` depuis le répertoire `src`.

Les fonctions suivantes sont disponibles dans `partie_2.py` et peuvent être appellées dans le `main.py` :

- `union_automates(automate_1, automate_2)` : Retourne l'union de deux automates.
- `concat_automates(automate_1, automate_2)` : Retourne la concaténation de deux automates.
- `repet_automate(automate)` : Retourne la répétition d'un automate.

## Prérequis

- Python 3.x
- Bibliothèque GraphViz installée et accessible dans le PATH

## Installation

1. Installez les dépendances :
```
pip install graphviz
```
> Si vous rencontrez des difficultés avec le `/bin` de graphviz, téléchargez le .zip [sur le site officiel](https://graphviz.org/download/) et décompressez le /bin dans le /bin du projet

2. Placez-vous dans le répertoire `src` et exécutez le fichier `main.py` :
```
cd projet/src
python main.py
```

## Contribution

Travail réalisé par Charles Iacopino et Steven Guillemet pour le cours de Théorie des langages à l'Université Catholique de Lille.