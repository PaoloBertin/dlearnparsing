""" Modulo schede """
from cards.card071 import Card071


class Card07:
    """Forze nodali e condizioni cinematiche"""

    def __init__(self):
        self.card071s = []

    def initialize(self, content, i) -> int:
        """Inizializza scheda card07"""
        while content[i + 1] != "" and content[i + 1] != "*end":
            card071 = Card071()
            i = card071.initialize(content, i)
            self.card071s.append(card071)

        return i

    def to_string(self) -> list[str]:
        """Output attributi"""

        lb = []
        for card071 in self.card071s:
            for item in card071.to_string():
                lb.append(item)
        lb = lb + ["\n"]
        return lb
