""" Modulo schede """
from cards.card10141 import Card10141


class Card1014:
    """Definizione nodi e materiale elementi truss"""

    def __init__(self):
        self.card10141s = []

    def initialize(self, content, i) -> int:
        """Inizializzazione scheda 10.1.4"""

        rows = len(content)
        while content[i + 1] != "" and i <= rows:
            card10141 = Card10141()
            i = card10141.initialize(content, i)
            self.card10141s.append(card10141)

        return i

    def to_string(self) -> list[str]:
        """Formattazione"""

        lb = []
        for card10141 in self.card10141s:
            lb = lb + card10141.to_string()

        return lb
