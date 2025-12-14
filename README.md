Gestion de Flotte Spatiale — Projet Python

Ce projet est un programme Python en ligne de commande qui permet de gérer une flotte de vaisseaux spatiaux.
Il a été réalisé dans le cadre d’un TP afin de mettre en pratique la programmation orientée objet et la sauvegarde de données.

Le programme permet de créer des vaisseaux, d’ajouter des membres d’équipage et de sauvegarder l’état de la flotte dans un fichier JSON.

Organisation du projet

Le projet est séparé en plusieurs fichiers afin de rendre le code plus clair et plus facile à maintenir.

main.py : fichier principal qui lance le programme et gère le menu.

data.py : contient les constantes, les listes de valeurs autorisées et une fonction pour sécuriser les entrées utilisateur.

save_and_load_data.py : gère la sauvegarde et le chargement des données avec un fichier JSON.

Fleet.py : classe qui représente la flotte et contient les vaisseaux.

Spaceship.py : classe qui représente un vaisseau spatial et son équipage.

Member.py : classe de base pour les membres de l’équipage.

Operator.py : classe héritée de Member qui ajoute un rôle et un niveau d’expérience.

Mentalist.py : classe héritée de Member qui ajoute la gestion du mana.

Fonctionnement

Le projet repose sur la programmation orientée objet.

La classe Member est la base de tous les membres d’équipage.

Les classes Operator et Mentalist héritent de Member.

Les attributs sont privés et accessibles via des getters et setters.

Les données sont sauvegardées dans un fichier data.json.
Lors du chargement, le programme reconstruit correctement les objets (vaisseaux et membres d’équipage) à partir du fichier.

Un vaisseau est considéré comme prêt uniquement s’il possède :

un opérateur avec le rôle de pilote

un opérateur avec le rôle de technicien

Le programme peut aussi générer des événements aléatoires qui ont un impact sur la flotte.
