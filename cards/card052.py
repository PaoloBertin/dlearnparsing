""" Modulo schede """
from cards.card02 import Card02 as cd02


class Card052:
    """Generazione nodi"""

    def __init__(self):
        self.m = None
        self.mgen = None
        self.temp = []

    def initialize(self, content, i) -> int:
        """Inizializza la scheda 5.2"""
        i += 1
        line_card = content[i].split(",")
        for parameters in line_card:
            token = parameters.split("=")
            var = token[0].strip()
            val = token[1].strip()
            match var:
                case "m":
                    self.m = int(val)
                case "mgen":
                    self.mgen = int(val)
                case "tx":
                    self.temp.insert(0, float(val))
                case "ty":
                    self.temp.insert(1, float(val))
                case "tz":
                    self.temp.insert(2, float(val))

        return i

    def to_string(self) -> list[str]:
        """ Formattazione """

        sb = f"{self.m:5d}{self.mgen:5d}"
        nsd = cd02.nsd
        for j in range(nsd):
            sb = sb + f"{self.temp[j]:10.2f}"
        sb = sb + "\n"

        return [sb]
