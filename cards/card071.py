""" Modulo schede """
from cards.card02 import Card02
from cards.card073 import Card073
from cards.card072 import Card072


class Card071:
    """Forza su nodo n"""

    def __init__(self):
        self.n = None
        self.numgp = None
        self.f = []

        self.card072s = []
        self.card073 = Card073()

    def initialize(self, content, i) -> int:
        """Inizializza la scheda 7.1"""

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
                case "fx":
                    self.f.append(float(val))
                case "fy":
                    self.f.append(float(val))
                case "fz":
                    self.f.append(float(val))

        if self.numgp > 1:
            for j in range(self.numgp - 1):
                card072 = Card072()
                i = card072.initialize(content, i)
                self.card072s.append(card072)
            i = self.card073.initialize(content, i)

        return i

    def to_string(self) -> list[str]:
        """Formattazione"""
        lb = []
        sb = f"{self.n:5d}{self.numgp:5d}"
        ndof = Card02.ndof
        for j in range(ndof):
            sb = sb + f"{self.f[j]:10.3f}"
        sb = sb + "\n"
        lb.append(sb)

        if self.numgp > 1:
            for card072 in self.card072s:
                lb = lb + card072.to_string()

            lb = lb + self.card073.to_string()
            lb = lb + ["\n"]
        # lb = lb + ["\n"]

        return lb
