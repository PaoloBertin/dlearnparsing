""" Modulo schede """
class Card053:
    """Incremento nodi"""

    def __init__(self):
        self.ninc = []
        self.inc = []
        self.incr = []

    def initialize(self, content, i) -> int:
        """Inizializza la scheda 5.3"""
        i += 1
        line_card = content[i].split(",")
        for parameters in line_card:
            token = parameters.split("=")
            var = token[0].strip()
            val = token[1].strip()
            match var:
                case "ninc1":
                    # self.ninc.append(int(val))
                    self.incr.insert(0, int(val))
                case "inc1":
                    # self.inc.append(int(val))
                    self.incr.insert(1, int(val))
                case "ninc2":
                    # self.ninc.append(int(val))
                    self.incr.insert(2, int(val))
                case "inc2":
                    # self.inc.append(int(val))
                    self.incr.insert(3, int(val))
                case "ninc3":
                    # self.ninc.append(int(val))
                    self.incr.insert(4, int(val))
                case "inc3":
                    # self.inc.append(int(val))
                    self.incr.insert(5, int(val))
        return i

    def to_string(self) -> list[str]:
        """ Formatting """

        sb = ""
        # for j in enumerate(self.ninc):
        for j in self.incr:
            sb = sb + f"{j:5d}"
        sb = sb + "\n"

        return [sb]
