""" Modulo """
from cards.card02 import Card02


class Card08:
    """Funzioni di carico"""

    def __init__(self):
        self.card081s = []

    def initialize(self, content, i) -> int:
        """Inizializza card08"""
        nltftn = Card02.nltftn
        for j in range(nltftn):
            cd081 = Card081()
            i = cd081.initialize(content, i)
            self.card081s.append(cd081)

        return i

    def to_string(self) -> list[str]:
        """Formattazione card08"""
        sb = []
        for card081 in self.card081s:
            for item in card081.to_string():
                sb.append(item)

        return sb


class Card081:
    """Funzione di carico"""

    def __init__(self):
        self.gv = []

    def initialize(self, content, i) -> int:
        """Inizializza la funzione di carico"""

        nptslf = Card02.nptslf
        for j in range(nptslf):
            vr = []
            i += 1
            line_card = content[i].split(",")
            for parameters in line_card:
                token = parameters.split("=")
                var = token[0].strip()
                val = token[1].strip()
                match var:
                    case "l":
                        vr.append(float(val))
                    case "t":
                        vr.append(float(val))
            self.gv.append(vr)
        return i

    def to_string(self) -> list[str]:
        """Formattazione"""

        lb = []
        sb = ""
        for gk in self.gv:
            sb = f"{gk[0]:10.2f}{gk[1]:10.2f}\n"
            lb.append(sb)

        return lb
