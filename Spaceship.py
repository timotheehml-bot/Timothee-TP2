# Spaceship.py

from typing import List, Dict, Any, Tuple
from Member import Member
from Operator import Operator
from Mentalist import Mentalist
from data import RED, GREEN, YELLOW, RESET # <--- Changement

class Spaceship:
    """Modélise un vaisseau, conteneur d'équipage."""
    MAX_CREW_CAPACITY = 10

    def __init__(self, name: str, shipType: str, condition: str = "opérationnel"):
        self._name = name
        self._shipType = shipType
        self._crew: List[Member] = []
        self._condition = condition

    @property
    def name(self): return self._name
    @property
    def crew(self): return self._crew
    @property
    def condition(self): return self._condition
    @property
    def shipType(self): return self._shipType
    @condition.setter
    def condition(self, value): self._condition = value
    
    def append_member(self, member: Member) -> bool:
        if len(self.crew) < self.MAX_CREW_CAPACITY:
            self.crew.append(member)
            print(f"{GREEN}✔ {member.first_name} {member.last_name} ({member.role}) ajouté à l'équipage.{RESET}")
            return True
        else:
            print(f"{RED}⚠ Échec : Capacité maximale ({self.MAX_CREW_CAPACITY}) atteinte pour {self.name}.{RESET}")
            return False

    def remove_member(self, last_name: str) -> bool:
        for m in list(self.crew):
            if m.last_name.lower() == last_name.lower():
                self.crew.remove(m)
                print(f"{YELLOW}Membre retiré : {m.first_name} {m.last_name} de {self.name}.{RESET}")
                return True
        return False

    def check_preparation(self) -> Tuple[bool, List[str]]:
        """Vérifie qu'au moins un pilote et un technicien sont présents."""
        has_pilot = any(isinstance(m, Operator) and m.role.lower() == "pilote" for m in self.crew)
        has_technician = any(isinstance(m, Operator) and m.role.lower() == "technicien" for m in self.crew)
        
        reasons = []
        if not has_pilot: reasons.append("Manque de Pilote.")
        if not has_technician: reasons.append("Manque de Technicien.")

        is_ready = has_pilot and has_technician
        return is_ready, reasons

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "shipType": self.shipType,
            "condition": self.condition,
            "crew": [m.to_dict() for m in self.crew]
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]):
        s = Spaceship(data["name"], data["shipType"], data["condition"])
        for m_data in data.get("crew", []):
            member_class_name = m_data.get('__class__')
            # Import des classes pour la reconstruction JSON
            if member_class_name == 'Operator':
                from Operator import Operator
                s.crew.append(Operator.from_dict(m_data))
            elif member_class_name == 'Mentalist':
                from Mentalist import Mentalist
                s.crew.append(Mentalist.from_dict(m_data))
            else:
                from Member import Member
                s.crew.append(Member.from_dict(m_data)) 
        return s