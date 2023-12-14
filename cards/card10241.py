""" Modulo schede """
from cards.card10242 import Card10242


class Card10241:
    """Definizione nodi e matriale elemento truss"""

    def __init__(self):
        self.n = None
        self.m = None
        self.ien = []
        self.ng = None

        self.card10242 = None

    def initialize(self, content, i):
        """Inizializza scheda 10.4.1"""
        i += 1
        line_card = content[i].split(",")
        for parameters in line_card:
            token = parameters.split("=")
            var = token[0].strip()
            val = token[1].strip()
            match var:
                case "n":
                    self.n = int(val)
                case "m":
                    self.m = int(val)
                case "ien1":
                    self.ien.insert(0, int(val))
                case "ien2":
                    self.ien.insert(1, int(val))
                case "ien3":
                    self.ien.insert(2, int(val))
                case "ng":
                    self.ng = int(val)

        # lettura scheda generazione elementi
        if self.ng == 1:
            self.card10242 = Card10242()
            i = self.card10242.initialize(content, i)

        return i

    def to_string(self) -> list[str]:
        """Formattazione"""

        lb = []
        sb = f"{self.n:5}{self.m:5}"
        nen = len(self.ien)
        for i in range(nen):
            sb = sb + f"{self.ien[i]:5}"
        sb = sb + f"{self.ng:5}"
        sb = sb + "\n"
        lb.append(sb)

        if self.ng == 1:
            lb = lb + self.card10242.to_string()

        return lb
