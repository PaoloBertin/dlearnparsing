from cards.card1022 import Card1022
from cards.card1023 import Card1023
from cards.card1024 import Card1024


class Card1021:
    """Controllo gruppo elementi truss"""

    def __init__(self):
        self.ntype = None
        self.numel = None
        self.numat = None
        self.nen = None
        self.nsout = None
        self.istprt = None
        self.lfbody = None
        self.nint = None
        self.imass = None
        self.impexp = None
        #
        self.card1022s = []
        self.card1023 = Card1023()
        self.card1024s = []

    def initialize(self, content, i) -> int:
        """Inizializza"""

        i += 1
        line_card = content[i].split(",")
        for parameters in line_card:
            token = parameters.split("=")
            var = token[0].strip()
            val = token[1].strip()
            match var:
                case "ntype":
                    self.ntype = int(val)
                case "numel":
                    self.numel = int(val)
                case "numat":
                    self.numat = int(val)
                case "nen":
                    self.nen = int(val)
                case "nsout":
                    self.nsout = int(val)
                case "istprt":
                    self.istprt = int(val)
                case "lfbody":
                    self.lfbody = int(val)
                case "nint":
                    self.nint = int(val)
                case "imass":
                    self.imass = int(val)
                case "impexp":
                    self.impexp = int(val)

        # lettura caratteristiche materiali del gruppo
        for j in range(self.numat):
            card1022 = Card1022()
            i = card1022.initialize(content, i)
            self.card1022s.append(card1022)

        # lettura componenti forze di gravita'
        i = self.card1023.initialize(content, i)

        # lettura definizione elementi
        # while content[i + 1] is not None and i <= len(content):
        rows = len(content)
        while content[i + 1] != "" and i <= rows:
            card1024 = Card1024()
            i = card1024.initialize(content, i)
            self.card1024s.append(card1024)

        return i

    def to_string(self) -> list[str]:
        """Formattazione"""

        lb = []
        sb = (f"{self.ntype:5d}" +
              f"{self.numel:5d}" +
              f"{self.numat:5d}" +
              f"{self.nen:5d}" +
              f"{self.nsout:5d}" +
              f"{self.istprt:5d}" +
              f"{self.lfbody:5d}" +
              f"{self.nint:5d}" +
              f"{self.imass:5d}" +
              f"{self.impexp:5d}"+
              "\n")
        lb.append(sb)

        # proprietà materiali
        for card1022 in self.card1022s:
            lb = lb + card1022.to_string()

        # cmponenti accelerazione gravità
        lb = lb + self.card1023.to_string()

        # definizione elementi
        for card1024 in self.card1024s:
            lb = lb + card1024.to_string()

        return lb
