""" Importazione parametri generali """
from cards.card02 import Card02


class Card06:
    """Condizioni al contorno"""

    def __init__(self):
        self.card061s = []

    def initialize(self, content, i) -> int:
        """Inizializza"""
        while content[i + 1] != "" and content[i + 1] != "*end":
            card061 = Card061()
            i = card061.initialize(content, i)
            self.card061s.append(card061)

        return i

    def to_string(self) -> list[str]:
        """Formattazione"""

        lb = []
        for card061 in self.card061s:
            lb = lb + card061.to_string()
        lb = lb + ["\n"]

        return lb


class Card061:
    """Condizioni al contorno"""

    def __init__(self):
        self.n = None
        self.ne = None
        self.ng = None
        self.id = []

    def initialize(self, content, i) -> int:
        """Inizializza la scheda 6.1"""

        i += 1
        line_card = content[i].split(",")
        for parameters in line_card:
            token = parameters.split("=")
            var = token[0].strip()
            val = token[1].strip()
            match var:
                case "n":
                    self.n = int(val)
                case "ne":
                    self.ne = int(val)
                case "ng":
                    self.ng = int(val)
                case "id1":
                    self.id.append(int(val))
                case "id2":
                    self.id.append(int(val))
                case "id3":
                    self.id.append(int(val))
                case "id4":
                    self.id.append(int(val))
                case "id5":
                    self.id.append(int(val))
                case "id6":
                    self.id.append(int(val))
        return i

    def to_string(self) -> list[str]:
        """Formattazione"""
        sb = f"{self.n:5d}{self.ne:5d}{self.ng:5d}"

        nsd = Card02.nsd
        for i in range(nsd):
            sb = sb + f"{self.id[i]:5d}"
        sb = sb + "\n"

        return [sb]
