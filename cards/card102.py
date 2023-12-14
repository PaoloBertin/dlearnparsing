""" Modulo schede """
from cards.card1021 import Card1021


class Card102:
    """Gruppo elementi truss 3D con materiale elastico"""

    def __init__(self):
        self.card1021s = []

    def initialize(self, content, i) -> int:
        """Inizializzazione gruppo elementi truss"""

        card1021 = Card1021()
        i = card1021.initialize(content, i)
        self.card1021s.append(card1021)

        return i

    def to_string(self) -> list[str]:
        """Formattazione"""

        lb = []
        for card1021 in self.card1021s:
            lb = lb + card1021.to_string()

        return lb
