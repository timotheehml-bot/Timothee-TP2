
RESET = "\033[0m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"


VALID_SHIP_TYPES = ["marchand", "guerre", "transport"]
VALID_MEMBER_TYPES = ["operateur", "mentaliste", "membre"]
VALID_OP_ROLES = ["pilote", "technicien", "commandant", "armurier"]
VALID_GENDERS = ["femme", "homme", "autre"]
FICHIER_JSON = "fleet_data.json"


def safe_input(prompt: str) -> str:
    """Permet de gérer les inputs dans un environnement non-interactif."""
    try:
        return input(prompt)
    except (OSError, EOFError):
     
        raise RuntimeError("interactive-unavailable")