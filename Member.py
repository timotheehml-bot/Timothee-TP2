

from typing import Dict, Any

class Member:
    """Modélise un membre d'équipage de base."""
    def __init__(self, first_name: str, last_name: str, gender: str, age: int):
        self._first_name = first_name
        self._last_name = last_name
        self._gender = gender
        self._age = age


    @property
    def first_name(self): return self._first_name
    @property
    def last_name(self): return self._last_name
    @property
    def gender(self): return self._gender
    @property
    def age(self): return self._age
    @property
    def role(self): return "Membre Simple"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender": self.gender,
            "age": self.age
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]):
        return Member(data["first_name"], data["last_name"], data["gender"], data["age"])