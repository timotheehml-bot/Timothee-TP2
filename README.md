# Gestion de Flotte Spatiale — Projet Python

Ce projet est une application en ligne de commande (CLI) structurée autour des principes de la Programmation Orientée Objet (POO). Il permet la gestion complète d'une flotte de vaisseaux spatiaux avec persistance des données via JSON.

## 📌 Structure du Dépôt

Le projet est organisé en huit modules Python pour garantir la séparation des responsabilités et l'intégrité du modèle.

| Fichier | Rôle Principal | Description Technique |
| :--- | :--- | :--- |
| `main.py` | Orchestrateur | Point d'entrée de l'application. Gère la boucle de menu et la logique d'interaction. |
| `data.py` | Configuration | Définit les constantes (validation des types, couleurs) et la fonction utilitaire `safe_input`. |
| `save_and_load_data.py` | Persistance | Fonctions `save_data` et `load_data` utilisant la sérialisation `__dict__` pour la gestion des attributs privés. |
| `Fleet.py` | Classe `Fleet` | Conteneur pour les vaisseaux. Implémente la logique de capacité maximale et le calcul des statistiques agrégées. |
| `Spaceship.py` | Classe `Spaceship` | Conteneur pour l'équipage. Gère l'état (`condition`) et la méthode `check_preparation()`. |
| `Member.py` | Classe de Base | Définit les attributs de base (prénom, nom, âge, genre) de l'équipage. |
| `Operator.py` | Spécialisation | Hérite de `Member`. Ajoute les attributs `rôle` et `expérience`. |
| `Mentalist.py` | Spécialisation | Hérite de `Member`. Ajoute l'attribut `mana`. |

## ⚙️ Détails des Fonctionnalités Implémentées

### 1. POO et Héritage

* **Classes de Base/Dérivées :** Le modèle utilise l'héritage, où `Operator` et `Mentalist` sont des spécialisations de la classe de base `Member`.
* **Encapsulation :** Tous les attributs sont privés (`_attribut`) avec des accesseurs (`@property`) et mutateurs (`@setter`).

### 2. Persistance et Sérialisation

* **Format :** Utilisation du fichier `data.json`.
* **Méthode :** La sérialisation est basée sur l'accès aux dictionnaires internes des objets Python (`obj.__dict__`) pour assurer la sauvegarde complète et la reconstruction des attributs privés (`_Classe__attribut`).
* **Robustesse :** La fonction `load_data` gère la reconstruction correcte des objets spécialisés (`Operator` et `Mentalist`) via la détection d'attributs de rôle ou de mana.

### 3. Logique Applicative

* **Validation :** Les opérations de création de vaisseaux et de membres utilisent des listes de validation définies dans `data.py`.
* **Préparation du Vaisseau :** La méthode `Spaceship.check_preparation()` vérifie la présence obligatoire d'un `Operator` de rôle **pilote** et d'un `Operator` de rôle **technicien**.
* **Événements Aléatoires :** La fonction `random_event` simule des événements (attaque/renfort) dont les effets sont immédiatement appliqués à la flotte et sauvegardés.

## 🚀 Lancement

1.  Assurez-vous que les 8 fichiers Python se trouvent dans le même répertoire.
2.  Exécutez le point d'entrée :
    ```bash
    python main.py
    ```
