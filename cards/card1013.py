""" Modulo schede """
from cards.card02 import Card02


class Card1013:
    """ Gravità agente su elementi 2D """

    def __init__(self):
        self.grav = [0.0, 0.0]

    def initialize(self, content, i) -> int:
        """ Inizializzazione """

        i += 1
        line_card = content[i].split(",")
        for parameters in line_card:
            token = parameters.split("=")
            var = token[0].strip()
            val = token[1].strip()
            match var:
                case "gravx":
                    self.grav[0] = float(val)
                case "gravy":
                    self.grav[1] = float(val)
        return i

    def to_string(self) -> list[str]:
        """ Formattazione """

        sb = ""

        nsd = Card02.nsd
        for i in range(nsd):
            sb = sb + f"{self.grav[i]:10}"
        sb = sb + "\n"

        return [sb]
