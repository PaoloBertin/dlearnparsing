"""" Modulo schede """


class Card1012:
    """ Proprieta' materiali elemento 2D """

    def __init__(self):
        self.m = None
        self.e = None
        self.pois = None
        self.rho = None
        self.rdampm = None
        self.rdampk = None
        self.th = None

    def initialize(self, content, i) -> int:
        """Inizialiiza scheda Card 10.1.2"""

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
                case "pois":
                    self.pois = float(val)
                case "rho":
                    self.rho = float(val)
                case "rdampm":
                    self.rdampm = float(val)
                case "rdampk":
                    self.rdampk = float(val)
                case "th":
                    self.th = float(val)
        return i

    def to_string(self) -> list[str]:
        """Formattazione"""

        lb = [
                f"{self.m:5d}" +
                f"{' ':5}" +
                f"{self.e:10}" +
                f"{self.pois:10}" +
                f"{self.rho:10.3f}" +
                f"{self.rdampm:10.3f}" +
                f"{self.rdampk:10.3f}" +
                f"{self.th:10.3f}" +
                "\n"
        ]

        return lb
