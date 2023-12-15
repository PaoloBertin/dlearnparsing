""" Modulo schede """


class Card1011:
    """Controllo gruppo elemento"""

    def __init__(self):
        self.ntype = None
        self.numel = None
        self.numat = None
        self.nsurf = None
        self.nsout = None
        self.iopt = None
        self.istprt = None
        self.lfsurf = None
        self.lfbody = None
        self.nicode = None
        self.ibbar = None
        self.imass = None
        self.impexp = None

    def initialize(self, content, i) -> int:
        """Inizializzazione"""

        i += 1
        line_card = content[i].split(",")
        for parameters in line_card:
            token = parameters.split("=")
            var = token[0].strip()
            val = token[1].strip()
            match var:
                case "ntype":
                    self.ntype = int(val)
                case "numel":
                    self.numel = int(val)
                case "numat":
                    self.numat = int(val)
                case "nsurf":
                    self.nsurf = int(val)
                case "nsout":
                    self.nsout = int(val)
                case "iopt":
                    self.iopt = int(val)
                case "istprt":
                    self.istprt = int(val)
                case "lfsurf":
                    self.lfsurf = int(val)
                case "lfbody":
                    self.lfbody = int(val)
                case "nicode":
                    self.nicode = int(val)
                case "ibbar":
                    self.ibbar = int(val)
                case "imass":
                    self.imass = int(val)
                case "impexp":
                    self.impexp = int(val)

        return i

    def to_string(self) -> list[str]:
        """Formattazione"""

        sb = [
            f"{self.ntype:5d}"
            f"{self.numel:5d}"
            f"{self.numat:5}"
            f"{self.nsurf:5}"
            f"{self.nsout:5}"
            f"{self.iopt:5}"
            f"{self.istprt:5}"
            f"{self.lfsurf:5}"
            f"{self.lfbody:5}"
            f"{self.nicode:5}"
            f"{self.ibbar:5}"
            f"{self.imass:5}"
            f"{self.impexp:5}"
            f"\n"
        ]

        return sb
