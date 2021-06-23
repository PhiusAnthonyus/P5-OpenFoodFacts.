# P5-OpenFoodFacts

## Présentation
Il s'agit d'un programme permettant à un utilisateur de parcourir les aliments et de fournir un aliment de substitution plus sain que celui sélectionné.
Pour cela, le programme s'appuie sur les données de la base OpenFoodFacts.

## Description du parcours utilisateur
L'utilisateur est sur le terminal. L'utilisation du programme se résume à des interactions entre le programme et l'utilisateur.

### L'utilisateur arrive d'abord sur le menu principal :
* 1 -> Mettre à jour la base de données.
* 2 -> Faire une recherche.
* 3 -> Afficher les favoris.

### Dans la fonction recherche :
* Sélectionnez la catégorie. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entrée]
* Sélectionnez l'aliment. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant à l'aliment choisi et appuie sur entrée]
* Le programme affiche sa description, un magasin ou l'acheter (le cas échéant) et un lien vers la page d'Open Food Facts concernant cet aliment.
* L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base de données, ainsi que de trouver un substitut (le cas échéant).

## Fonctionnalités
* Recherche d'aliments dans la base OpenFoodFacts.
* L'utilisateur interagit avec le programme dans le terminal.
* Si l'utilisateur entre un caractère qui n'est pas un chiffre, le programme doit lui répéter la question.
* La recherche doit s'effectuer sur une base MySql.

## Pré-requis
* Il est nécessaire dans un premier temps de créer une base de donnée et d'avoir son mot de passe afin que le programme puisse accéder à la base de données locale.
* Les modules nécessaires au bon fonctionnement du programme sont : Cryptography, PyMysql, et Requests.

## Installation
Afin de créer les tables et de charger les données, le premier lancerment se fera avec create_database.py. Ensuite, utilisez le programme principal main.py pour mettre à jour la base de données.
