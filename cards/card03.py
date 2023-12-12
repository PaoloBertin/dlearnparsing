class Card03:
    """Sequenze temporali"""

    def __init__(self):
        self.n = None
        self.nstep = None
        self.ndprt = None
        self.nsprt = None
        self.nhplt = None
        self.niter = None
        self.alpha = None
        self.beta = None
        self.gamma = None
        self.dt = None

    def initialize(self, content, i) -> int:
        """Inizializza la scheda 3"""
        i += 1
        line_card = content[i].split(",")
        for parameters in line_card:
            token = parameters.split("=")
            var = token[0].strip()
            val = token[1].strip()
            match var:
                case "n":
                    self.n = int(val)
                case "nstep":
                    self.nstep = int(val)
                case "ndprt":
                    self.ndprt = int(val)
                case "nsprt":
                    self.nsprt = int(val)
                case "nhplt":
                    self.nhplt = int(val)
                case "niter":
                    self.niter = int(val)
                case "alpha":
                    self.alpha = float(val)
                case "beta":
                    self.beta = float(val)
                case "gamma":
                    self.gamma = float(val)
                case "dt":
                    self.dt = float(val)
        return i + 1

    def to_string(self) -> list[str]:
        """Formattazione"""

        sb = (f"{self.n:5d}" +
              f"{self.nstep:5d}" +
              f"{self.ndprt:5d}" +
              f"{self.nsprt:5d}" +
              f"{self.nhplt:5d}" +
              f"{self.niter:5d}" +
              f"{self.alpha:10.4f}" +
              f"{self.beta:10.4f}" +
              f"{self.gamma:10.4f}" +
              f"{self.dt:10.4f}" +
              "\n")

        return [sb]
