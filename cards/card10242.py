""" Modulo schede """


class Card10242:
    """Generazione elementi truss"""

    def __init__(self) -> None:
        self.nel = None
        self.incel = None
        self.inc = None

    def initialize(self, content, i) -> int:
        """Inizializza"""

        i += 1
        line_card = content[i].split(",")
        for parameters in line_card:
            token = parameters.split("=")
            var = token[0].strip()
            val = token[1].strip()
            match var:
                case "nel":
                    self.nel = int(val)
                case "incel":
                    self.incel = int(val)
                case "inc":
                    self.inc = int(val)
        return i

    def to_string(self) -> list[str]:
        """Formattazione"""

        lb = [f"{self.nel:5d}" f"{self.incel:5d}" f"{self.inc:5}" f"\n"]

        return lb
