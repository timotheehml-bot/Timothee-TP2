

from Member import Member
from typing import Dict, Any

class Operator(Member):
    """Modélise un opérateur spécialisé."""
    def __init__(self, first_name: str, last_name: str, gender: str, age: int, role: str, experience: int = 0):
        super().__init__(first_name, last_name, gender, age)
        self._role = role
        self._experience = experience

    @property
    def role(self): return self._role
    @property
    def experience(self): return self._experience
    
    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data["role"] = self.role
        data["experience"] = self.experience
        return data

    @staticmethod
    def from_dict(data: Dict[str, Any]):
        return Operator(data["first_name"], data["last_name"], data["gender"], data["age"], data["role"], data["experience"])
