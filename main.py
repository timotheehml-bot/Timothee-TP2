# main.py

import random
import sys

# Import de toutes les classes
from Fleet import Fleet
from Spaceship import Spaceship
from Member import Member
from Operator import Operator
from Mentalist import Mentalist

# Import des fonctions de persistance et des outils
from save_and_load_data import save_data, load_data
from data import safe_input, VALID_SHIP_TYPES, VALID_MEMBER_TYPES, VALID_OP_ROLES, VALID_GENDERS
from data import RESET, CYAN, GREEN, YELLOW, RED, MAGENTA


# --- Fonctions de Logique (définies dans main.py) ---

def random_event(fleet: Fleet):
    """Déclenche un événement aléatoire (attaque ou renfort)."""
    if not fleet.spaceships:
        print("La flotte est vide, aucun événement aléatoire possible.")
        return
        
    event = random.choice(["attaque", "renfort"])
    ship = random.choice(fleet.spaceships)

    if event == "attaque":
        ship.condition = "endommagé"
        print(f"⚠️ Attaque ennemie ! Le vaisseau {ship.name} est {RED}endommagé{RESET}.")
    elif event == "renfort":
        new_member = Member("Renfort", f"Op-{random.randint(1,99)}", "homme", 25)
        if ship.append_member(new_member):
             print(f"🛠️ Renfort ({new_member.first_name} {new_member.last_name}) ajouté au vaisseau {ship.name}.")
        
    save_data(fleet)

def display_global_statistics(fleet: Fleet):
    """Affiche les statistiques globales."""
    stats = fleet.statistics()

    print(f"\n{MAGENTA}📊 Statistiques globales de {fleet.name} :{RESET}")
    print(f"- Nombre total de vaisseaux : {stats['total_ships']}")
    print(f"- Vaisseaux opérationnels : {GREEN}{stats['operational']}{RESET}, endommagés : {RED}{stats['damaged']}{RESET}")
    
    print("\nRépartition des Rôles :")
    sorted_roles = sorted(stats['roles_count'].items(), key=lambda item: item[1], reverse=True)
    for role, count in sorted_roles:
        print(f"  - {role.capitalize()}: {count}")

    print(f"Niveau moyen d'expérience des Opérateurs: {stats['avg_exp']:.2f}")

def select_spaceship(fleet: Fleet):
    """Aide à sélectionner un vaisseau via un index."""
    fleet_ships = fleet.spaceships
    if not fleet_ships:
        print(f"{RED}Aucun vaisseau dans la flotte.{RESET}")
        return None, -1

    print("\n--- Liste des Vaisseaux ---")
    for i, ship in enumerate(fleet_ships):
        status_color = GREEN if ship.condition == "opérationnel" else RED
        print(f"{i+1} - {ship.name} (Type: {ship.shipType}, Équipage: {len(ship.crew)}, État: {status_color}{ship.condition.capitalize()}{RESET})")

    idx_input = safe_input("Choisissez un vaisseau (ou 'cancel') : ").strip()
    if idx_input.lower() == "cancel":
        return None, -1

    try:
        idx = int(idx_input) - 1
        if 0 <= idx < len(fleet_ships):
            return fleet_ships[idx], idx
    except ValueError:
        print(f"{RED}Oups ! Ce n'était pas un numéro.{RESET}")
    
    print(f"{RED}Numéro invalide.{RESET}")
    return None, -1

def create_and_add_spaceship(fleet: Fleet):
    """Permet de créer un nouveau vaisseau et de l'ajouter à la flotte."""
    name = safe_input("Nom du nouveau vaisseau : ").strip()
    if not name:
        print(f"{RED}Nom invalide.{RESET}")
        return

    ship_type = ""
    while ship_type not in VALID_SHIP_TYPES:
        ship_type = safe_input(f"Type ({'/'.join(VALID_SHIP_TYPES)}) : ").strip().lower()

    new_ship = Spaceship(name, ship_type)
    if fleet.append_spaceship(new_ship):
        print(f"{GREEN}Vaisseau {name} ajouté à la flotte.{RESET}")
        handle_save("Ajout de vaisseau")
    else:
        print(f"{RED}Échec de l'ajout (capacité maximale atteinte).{RESET}")

def create_and_add_member(ship: Spaceship):
    """Permet de créer un nouveau membre pour un vaisseau sélectionné."""
    if len(ship.crew) >= ship.MAX_CREW_CAPACITY:
        print(f"{RED}L'équipage de {ship.name} est déjà au maximum ({ship.MAX_CREW_CAPACITY}).{RESET}")
        return

    first_name = safe_input("Prénom : ").strip()
    last_name = safe_input("Nom : ").strip()
    age = int(safe_input("Âge : ").strip() or 0)
    
    gender = ""
    while gender not in VALID_GENDERS:
        gender = safe_input(f"Genre ({'/'.join(VALID_GENDERS)}) : ").strip().lower()

    member_type = ""
    while member_type not in VALID_MEMBER_TYPES:
        member_type = safe_input(f"Type de membre ({'/'.join(VALID_MEMBER_TYPES)}) : ").strip().lower()
    
    new_member = None
    if member_type == "operateur":
        role = ""
        while role not in VALID_OP_ROLES:
            role = safe_input(f"Rôle ({'/'.join(VALID_OP_ROLES)}) : ").strip().lower()
        experience = int(safe_input("Expérience (années) : ").strip() or 0)
        new_member = Operator(first_name, last_name, gender, age, role, experience)
        
    elif member_type == "mentaliste":
        mana = int(safe_input("Mana (1-100) : ").strip() or 100)
        new_member = Mentalist(first_name, last_name, gender, age, mana)
        
    elif member_type == "membre":
        new_member = Member(first_name, last_name, gender, age)

    if new_member and ship.append_member(new_member):
        handle_save(f"Ajout de membre à {ship.name}")

def remove_member_from_ship(ship: Spaceship):
    """Permet de retirer un membre de l'équipage."""
    if not ship.crew:
        print(f"{YELLOW}{ship.name} n'a pas d'équipage à retirer.{RESET}")
        return

    print("\n--- Équipage ---")
    for i, m in enumerate(ship.crew):
        print(f"{i+1}. {m.first_name} {m.last_name} ({m.role})")
    
    last_name = safe_input("Nom du membre à retirer : ").strip()
    
    if ship.remove_member(last_name):
        handle_save(f"Retrait de membre de {ship.name}")
    else:
        print(f"{RED}Membre '{last_name}' non trouvé dans l'équipage de {ship.name}.{RESET}")

def prepare_spaceship_for_launch(ship: Spaceship):
    """Vérifie la préparation d'un vaisseau pour le lancement."""
    is_ready, reasons = ship.check_preparation()
    
    print(f"\n--- Préparation de {ship.name} ---")
    if is_ready:
        print(f"{GREEN}✓ Le vaisseau est prêt au lancement (Pilote et Technicien trouvés).{RESET}")
    else:
        print(f"{RED}✗ Le vaisseau N'EST PAS prêt au lancement. Raisons : {RESET}")
        for r in reasons:
            print(f"  - {YELLOW}{r}{RESET}")

# --- Boucle Principale du Menu ---

def menu():
    global main_fleet

    def get_confirmation(prompt):
        return safe_input(prompt).strip().lower() == "o"

    def handle_save(action_name):
        if get_confirmation("Voulez-vous sauvegarder ce changement ? (o/n) : "):
            save_data(main_fleet)
            print(f"  {GREEN}{action_name} appliqué et sauvegardé.{RESET}")
            return True
        else:
            print(f"  {YELLOW}{action_name} annulé. Aucun changement permanent.{RESET}")
            return False

    while True:
        print(f"\n{CYAN}=== Gestion de la flotte : {main_fleet.name} ==={RESET}")
        print("1. Renommer la flotte")
        print("2. Ajouter un vaisseau à la flotte")
        print("3. Afficher les vaisseaux et l'équipage")
        print("4. Ajouter un membre à un vaisseau")
        print("5. Retirer un membre d'un vaisseau")
        print("6. Préparer un vaisseau pour le lancement")
        print("7. Changer l'état d'un vaisseau")
        print("8. Sauvegarder la flotte")
        print("9. Afficher les statistiques")
        print("10. Événement aléatoire (simulation)")
        print("11. Quitter")

        try:
            choice = safe_input("Choisissez une option : ")
        except RuntimeError:
            print(f"{RED}Arrêt du programme : Environnement non-interactif.{RESET}")
            break

        match choice:
            case "1": 
                new_name = safe_input("Nouveau nom de la flotte : ").strip()
                if new_name:
                    main_fleet.name = new_name
                    handle_save("Renommage de la flotte")

            case "2": 
                create_and_add_spaceship(main_fleet)
            
            case "3":
                ship, idx = select_spaceship(main_fleet)
                if ship:
                    print(f"\nÉquipage de {ship.name} ({ship.shipType}, {len(ship.crew)} membres):")
                    for m in ship.crew:
                        details = (f"Expérience: {m._experience}" if isinstance(m, Operator) else 
                                   (f"Mana: {m._mana}" if isinstance(m, Mentalist) else ""))
                        print(f"  - {m.first_name} {m.last_name} ({m.role}, {m.age} ans). {details}")

            case "4":
                ship, idx = select_spaceship(main_fleet)
                if ship:
                    create_and_add_member(ship)

            case "5":
                ship, idx = select_spaceship(main_fleet)
                if ship:
                    remove_member_from_ship(ship)

            case "6":
                ship, idx = select_spaceship(main_fleet)
                if ship:
                    prepare_spaceship_for_launch(ship)
            
            case "7":
                ship, idx = select_spaceship(main_fleet)
                if ship:
                    new_condition = safe_input("Nouvel état (opérationnel/endommagé) : ").strip().lower()
                    if new_condition in ["opérationnel", "endommagé"]:
                        ship.condition = new_condition
                        handle_save(f"Changement d'état de {ship.name}")
                    else:
                        print(f"{RED}État invalide.{RESET}")


            case "8":
                save_data(main_fleet)

            case "9":
                display_global_statistics(main_fleet)

            case "10":
                random_event(main_fleet)

            case "11":
                if get_confirmation("Sauvegarder avant de quitter ? (o/n) : "):
                    save_data(main_fleet)
                print("Au revoir !")
                break

            case _:
                print(f"{RED}Choix invalide, réessayez.{RESET}")


if __name__ == "__main__":
    main_fleet = Fleet("Galactica")
    try:
        start_choice = safe_input("Voulez-vous charger une flotte existante ? (o/n) : ")
        if start_choice.lower() == "o":
            main_fleet = load_data()
    except RuntimeError:
        pass 

    menu()