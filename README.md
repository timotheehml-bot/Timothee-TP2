# 🚀 Système de Gestion de Flotte Stellaire (Starfleet Management System)

Ce projet est une application en ligne de commande (CLI) écrite en Python pour simuler la gestion des vaisseaux et des équipages d'une flotte spatiale.

Le projet utilise les principes de la Programmation Orientée Objet (POO) pour structurer les entités clés (Flotte, Vaisseau, Membres) et la sérialisation JSON pour la persistance des données.

## 📁 Structure du Projet

Le projet est organisé en 8 fichiers Python, garantissant une bonne séparation des responsabilités (Single Responsibility Principle).

| Fichier | Rôle Principal | Responsabilité |
| :--- | :--- | :--- |
| **`main.py`** | Exécution & Menu | Point d'entrée principal, gère la boucle du menu et les interactions utilisateur. |
| **`Fleet.py`** | Classe `Fleet` | Contient une liste de `Spaceship` et calcule les statistiques globales. |
| **`Spaceship.py`** | Classe `Spaceship` | Contient une liste de `Member` (`Crew`) et gère la préparation au lancement. |
| **`Member.py`** | Classe `Member` | Classe de base pour tous les membres d'équipage. |
| **`Operator.py`** | Classe `Operator` | Hérite de `Member`, ajoute les attributs `role` et `experience`. |
| **`Mentalist.py`** | Classe `Mentalist` | Hérite de `Member`, ajoute l'attribut `mana`. |
| **`data.py`** | Constantes & Utils | Centralise toutes les couleurs ANSI, les listes de validation et la fonction `safe_input`. |
| **`save_and_load_data.py`** | Persistance | Contient les fonctions `save_data` et `load_data` pour la sérialisation/désérialisation JSON. |

## 🛠️ Configuration et Lancement

### Prérequis

* Python 3.x installé.

### Installation

1.  Assurez-vous que tous les 8 fichiers se trouvent dans le même répertoire.

### Exécution

Pour démarrer l'application, ouvrez votre terminal dans le répertoire du projet et exécutez :

```bash
python main.py