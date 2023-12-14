""" Modulo schede """

class Card1022:
    """Proprieta' materiali elementi truss"""

    def __init__(self):
        self.m = None
        self.e = None
        self.rho = None
        self.rdampm = None
        self.rdampk = None
        self.area = None

    def initialize(self, content, i) -> int:
        """Inizialiiza scheda Card 10.2"""

        i += 1
        line_card = content[i].split(",")
        for parameters in line_card:
            token = parameters.split("=")
            var = token[0].strip()
            val = token[1].strip()
            match var:
                case "m":
                    self.m = int(val)
                case "E":
                    self.e = float(val)
                case "rho":
                    self.rho = float(val)
                case "rdampm":
                    self.rdampm = float(val)
                case "rdampk":
                    self.rdampk = float(val)
                case "area":
                    self.area = float(val)
        return i

    def to_string(self) -> list[str]:
        """Formattazione"""

        lb = [(
            f"{self.m:5d}" +
            f"{' ':5}" +
            f"{self.e:10}" +
            f"{self.rho:10.3f}" +
            f"{self.rdampm:10.3f}" +
            f"{self.rdampk:10.3f}" +
            f"{self.area:10.3f}"+
            "\n")
        ]

        return lb
