""" Modulo schede """


class Card10142:
    """Generazione elementi 2D"""

    def __init__(self) -> None:
        self.nel = [0, 0]
        self.incel = [0, 0]
        self.inc = [0,0]

    def initialize(self, content, i) -> int:
        """Inizializza"""

        i += 1
        line_card = content[i].split(",")
        for parameters in line_card:
            token = parameters.split("=")
            var = token[0].strip()
            val = token[1].strip()
            match var:
                case "nel1":
                    self.nel[0] = int(val)
                case "incel1":
                    self.incel[0] = int(val)
                case "inc1":
                    self.inc[0] = int(val)
                case "nel2":
                    self.nel[1] = int(val)
                case "incel2":
                    self.incel[1] = int(val)
                case "inc2":
                    self.inc[1] = int(val)
        return i

    def to_string(self) -> list[str]:
        """Formattazione"""

        lb = [f"{self.nel[0]:5d}{self.incel[0]:5d}{self.inc[0]:5}{self.nel[1]:5d}{self.incel[1]:5d}{self.inc[1]:5}" f"\n"]

        return lb
