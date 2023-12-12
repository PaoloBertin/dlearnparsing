class Card052:
    """Generazione nodi"""

    def __init__(self):
        self.m = None
        self.mgen = None
        self.temp = [0.0, 0.0, 0.0]

    def initialize(self, content, i) -> int:
        """Inizializza la scheda 5.2"""
        i += 1
        line_card = content[i].split(",")
        for parameters in line_card:
            token = parameters.split("=")
            var = token[0].strip()
            val = token[1].strip()
            match var:
                case "m":
                    self.m = int(val)
                case "mgen":
                    self.mgen = int(val)
                case "tx":
                    self.temp[0] = float(val)
                case "ty":
                    self.temp[1] = float(val)
                case "tz":
                    self.temp[2] = float(val)

        return i

    def to_string(self) -> list[str]:
        """ Formattazione """

        sb = f"{self.m:5d}{self.mgen:5d}"
        for i in range(len(self.temp)):
            sb = sb + f"{self.temp[i]:10.2f}"
        sb = sb + "\n"

        return [sb]
