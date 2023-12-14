""" Modulo schede """
from cards.card02 import Card02

from cards.card052 import Card052
from cards.card053 import Card053


class Card051:
    """Definizione nodo"""

    def __init__(self):
        self.n = None
        self.numgp = None
        self.x = [0.0, 0.0, 0.0]

        self.card052s = []
        self.card053 = Card053()

    def initialize(self, content, i) -> int:
        """Inizializza la scheda 5.1"""

        i += 1
        line_card = content[i].split(",")
        for parameters in line_card:
            token = parameters.split("=")
            var = token[0].strip()
            val = token[1].strip()
            match var:
                case "n":
                    self.n = int(val)
                case "numgp":
                    self.numgp = int(val)
                case "x":
                    self.x[0] = float(val)
                case "y":
                    self.x[1] = float(val)
                case "z":
                    self.x[2] = float(val)

        if self.numgp > 1:
            for j in range(self.numgp - 1):
                card052 = Card052()
                i = card052.initialize(content, i)
                self.card052s.append(card052)

            i = self.card053.initialize(content, i)

        return i

    def to_string(self) -> list[str]:
        """Formattazione"""

        lb = []
        sb = f"{self.n:5d}{self.numgp:5d}"
        nsd = Card02.nsd
        for i in range(nsd):
            sb = sb + f"{self.x[i]:10.2f}"
        lb.append(sb)

        for card052 in self.card052s:
            lb = lb + card052.to_string()

        lb = lb + self.card053.to_string()

        return lb
