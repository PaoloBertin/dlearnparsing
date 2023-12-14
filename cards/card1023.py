""" //TODO """
from cards.card02 import Card02


class Card1023:
    """Gravità agente su elementi truss"""

    def __init__(self):
        self.gravs = [0.0, 0.0, 0.0]

    def initialize(self, content, i) -> int:
        """Inizializzazione schda lettura componenti di gravita'"""

        i += 1
        line_card = content[i].split(",")
        for parameters in line_card:
            token = parameters.split("=")
            var = token[0].strip()
            val = token[1].strip()
            match var:
                case "gravx":
                    self.gravs[0] = float(val)
                case "gravy":
                    self.gravs[1] = float(val)
                case "gravz":
                    self.gravs[2] = float(val)
        return i

    def to_string(self) -> list[str]:
        """Formattazione"""

        sb = ""

        nsd = Card02.nsd
        for i in range(nsd):
            sb = sb + f"{self.gravs[i]:10}"
        sb = sb + "\n"

        return [sb]
