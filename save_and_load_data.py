# save_and_load_data.py

import json
import ast
import os
from typing import Any, Dict

# Import des outils pour le nom de fichier et les couleurs
from data import FICHIER_JSON, GREEN, YELLOW, RED, RESET 

# Import des classes pour la désérialisation
from Fleet import Fleet 
from Spaceship import Spaceship 
from Operator import Operator
from Mentalist import Mentalist
from Member import Member 

def save_data(fleet: Fleet, file_name: str = FICHIER_JSON):
    """
    Sauvegarde la flotte en JSON en utilisant __dict__ pour capturer les attributs privés.
    """
    try:
        json_string = json.dumps(fleet.__dict__, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        json_dict = ast.literal_eval(json_string)
        
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(json_dict, f, indent=4, ensure_ascii=False)
        
        print(f"{GREEN}✔ Flotte sauvegardée dans {file_name}.{RESET}")
    except Exception as e:
        print(f"{RED}⚠ Erreur lors de la sauvegarde : {e}{RESET}")


def load_data(file_name: str = FICHIER_JSON) -> Fleet:
    """
    Charge la flotte à partir d'un fichier JSON, en reconstruisant les objets 
    à partir des attributs privés.
    """
    if not os.path.exists(file_name):
        print(f"{YELLOW}Aucune sauvegarde trouvée ({file_name}). Création d'une nouvelle flotte.{RESET}")
        return Fleet("Galactica")
        
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"{RED}⚠ Erreur lors du chargement ({e}). Création d'une nouvelle flotte.{RESET}")
        return Fleet("Galactica")


    fleet_name = data.get("_Fleet__name", "Flotte inconnue")
    fleet = Fleet(fleet_name)

    for ship_data in data.get("_Fleet__spaceships", []):
        ship_name = ship_data.get("_Spaceship__name", "Inconnu")
        ship_type = ship_data.get("_Spaceship__shipType", "transport") 
        ship_condition = ship_data.get("_Spaceship__condition", "opérationnel") 
        ship = Spaceship(ship_name, ship_type, ship_condition)

        for member_data in ship_data.get("_Spaceship__crew", []):
            first = member_data.get("_Member__first_name", "Inconnu")
            last = member_data.get("_Member__last_name", "Inconnu")
            gender = member_data.get("_Member__gender", "autre")
            age = member_data.get("_Member__age", 0)

            # Reconstruction du membre selon le type
            if "_Operator__role" in member_data:
                role = member_data.get("_Operator__role", "technicien")
                experience = member_data.get("_Operator__experience", 0)
                member = Operator(first, last, gender, age, role, experience) 
            
            elif "_Mentalist__mana" in member_data:
                mana = member_data.get("_Mentalist__mana", 100) 
                member = Mentalist(first, last, gender, age, mana)
            
            else:
                member = Member(first, last, gender, age)

            ship.append_member(member)

        fleet.append_spaceship(ship)

    print(f"{GREEN}✔ Flotte chargée depuis {file_name}.{RESET}")
    return fleet