# Fleet.py

from typing import List, Dict, Any
from Spaceship import Spaceship
from Operator import Operator
from Mentalist import Mentalist
from data import RED, RESET # <--- Changement

class Fleet:
    """Modélise une flotte de vaisseaux, conteneur principal."""
    MAX_SPACESHIP_CAPACITY = 15

    def __init__(self, name: str):
        self._name = name
        self._spaceships: List[Spaceship] = []

    @property
    def name(self): return self._name
    @property
    def spaceships(self): return self._spaceships
    @name.setter
    def name(self, value): self._name = value
    
    def append_spaceship(self, spaceship: Spaceship) -> bool:
        if len(self.spaceships) < self.MAX_SPACESHIP_CAPACITY:
            self._spaceships.append(spaceship)
            return True
        else:
            print(f"{RED}⚠ Échec : Capacité maximale ({self.MAX_SPACESHIP_CAPACITY}) atteinte pour la flotte.{RESET}")
            return False

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "spaceships": [s.to_dict() for s in self.spaceships]
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]):
        from Spaceship import Spaceship
        f = Fleet(data["name"])
        f._spaceships = [Spaceship.from_dict(s) for s in data.get("spaceships", [])]
        return f

    def statistics(self) -> Dict[str, Any]:
        roles_count: Dict[str, int] = {}
        total_experience = 0
        operator_count = 0
        operational = 0
        damaged = 0

        for ship in self.spaceships:
            if ship.condition.lower() == "opérationnel":
                operational += 1
            else:
                damaged += 1
                
            for member in ship.crew:
                if isinstance(member, Operator):
                    roles_count[member.role.lower()] = roles_count.get(member.role.lower(), 0) + 1
                    total_experience += member.experience
                    operator_count += 1
                elif isinstance(member, Mentalist):
                    roles_count['mentaliste'] = roles_count.get('mentaliste', 0) + 1
                else:
                    roles_count['membre simple'] = roles_count.get('membre simple', 0) + 1

        avg_exp = total_experience / operator_count if operator_count > 0 else 0

        return {
            "total_ships": len(self.spaceships),
            "roles_count": roles_count,
            "operational": operational,
            "damaged": damaged,
            "avg_exp": avg_exp
        }