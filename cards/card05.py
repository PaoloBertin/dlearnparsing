""" Modulo schede """
from cards.card051 import Card051


class Card05:
    """Coordinate nodali"""

    def __init__(self):
        self.card051s = []

    def initialize(self, content, i) -> int:
        """Inizializza scheda 5"""

        while content[i + 1] != "" and content[i + 1] != "*end":
            card051 = Card051()
            i = card051.initialize(content, i)
            self.card051s.append(card051)
        return i

    def to_string(self) -> list[str]:
        """Formattazione"""

        sb = []
        for card051 in self.card051s:
            sb = sb + card051.to_string()
        sb = sb + ["\n"]

        return sb
