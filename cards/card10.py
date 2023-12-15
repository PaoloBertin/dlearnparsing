""" Modulo schede """
from cards.card02 import Card02

from cards.card101 import Card101
from cards.card102 import Card102


class Card10:
    """Definizione elementi"""

    def __init__(self):
        self.gntype = []
        self.card10s = []

    def initialize(self, content, i) -> int:
        """Inizializzazione scheda 10"""

        numeg = Card02.numeg
        for j in range(numeg):
            line_card = content[i + 1].split(",")
            parameters = line_card[0]
            token = parameters.split("=")
            ntype = int(token[1].strip())
            match ntype:
                case 1:
                    card101 = Card101()
                    i = card101.initialize(content, i)
                    self.card10s.append(card101)
                    self.gntype.append(ntype)
                case 2:
                    card102 = Card102()
                    i = card102.initialize(content, i)
                    self.card10s.append(card102)
            return i

    def to_string(self) -> list[str]:
        """Formattazione"""

        lb = []
        for card10 in self.card10s:
            lb = lb + card10.to_string()

        return lb
