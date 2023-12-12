from cards.card10241 import Card10241


class Card1024:
    """Definizione nodi e materiale elementi truss"""

    def __init__(self):
        self.card10241s = []

    def initialize(self, content, i) -> int:
        """Inizializzazione scheda 10.2.4"""

        rows = len(content)
        while content[i + 1] != "" and i <= rows:
            card10241 = Card10241()
            i = card10241.initialize(content, i)
            self.card10241s.append(card10241)

        return i

    def to_string(self) -> list[str]:
        """Formattazione"""

        lb = []
        for card10241 in self.card10241s:
            lb = lb + card10241.to_string()

        return lb
