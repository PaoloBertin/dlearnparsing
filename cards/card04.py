""" Modulo schede """


class Card04:
    """Storie nodali"""

    def __init__(self):
        self.idhist = []

    def initialize(self, content, i) -> int:
        """Inizializzazione"""

        i += 1
        line_card = content[i].split(",")
        for parameters in line_card:
            token = parameters.split("=")
            var = token[0].strip()
            val = token[1].strip()
            match var:
                case "idhist1":
                    self.idhist[0] = int(val)
                case "idhist2":
                    self.idhist[1] = int(val)
                case "idhist3":
                    self.idhist[2] = int(val)

        return i

    def to_string(self) -> list[str]:
        """Formatting"""

        sb = []
        if len(self.idhist) > 0 and self.idhist is not None:
            sb.append(f"{self.idhist:5d}")

        return sb
