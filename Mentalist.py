

from Member import Member
from typing import Dict, Any

class Mentalist(Member):
    """Modélise un mentaliste avec une jauge de mana."""
    def __init__(self, first_name: str, last_name: str, gender: str, age: int, mana: int = 100):
        super().__init__(first_name, last_name, gender, age)
        self._mana = mana

    @property
    def mana(self): return self._mana
    @property
    def role(self): return "Mentaliste"
    
    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data["mana"] = self.mana
        return data

    @staticmethod
    def from_dict(data: Dict[str, Any]):
        return Mentalist(data["first_name"], data["last_name"], data["gender"], data["age"], data["mana"])