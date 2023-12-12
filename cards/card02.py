class Card02:
    """Controllo esecuzione"""

    iexec = None
    iacode = None
    ireadr = None
    iwritr = None
    iprtin = None
    irank = None
    numseq = None
    ndout = None
    nsd = None
    numnp = None
    ndof = None
    nlvect = None
    nltftn = None
    nptslf = None
    numeg = None

    @staticmethod
    def initialize(content, i) -> int:
        """Inizializza la scheda 2"""

        i += 1
        line_card = content[i].split(",")
        for parameters in line_card:
            token = parameters.split("=")
            var = token[0].strip()
            val = token[1].strip()
            match var:
                case "iexec":
                    Card02.iexec = int(val)
                case "iacode":
                    Card02.iacode = int(val)
                case "ireadr":
                    Card02.ireadr = int(val)
                case "iwritr":
                    Card02.iwritr = int(val)
                case "iprtin":
                    Card02.iprtin = int(val)
                case "irank":
                    Card02.irank = int(val)
                case "numseq":
                    Card02.numseq = int(val)
                case "ndout":
                    Card02.ndout = int(val)
                case "nsd":
                    Card02.nsd = int(val)
                case "numnp":
                    Card02.numnp = int(val)
                case "ndof":
                    Card02.ndof = int(val)
                case "nlvect":
                    Card02.nlvect = int(val)
                case "nltftn":
                    Card02.nltftn = int(val)
                case "nptslf":
                    Card02.nptslf = int(val)
                case "numeg":
                    Card02.numeg = int(val)
        return i

    @staticmethod
    def to_string() -> list[str]:
        """Formattazione"""

        sb = (f"{Card02.iexec:5d}" +
              f"{Card02.iacode:5d}" +
              f"{Card02.ireadr:5d}" +
              f"{Card02.iwritr:5d}" +
              f"{Card02.iprtin:5d}" +
              f"{Card02.irank:5d}" +
              f"{Card02.numseq:5d}" +
              f"{Card02.ndout:5d}" +
              f"{Card02.nsd:5d}" +
              f"{Card02.numnp:5d}" +
              f"{Card02.ndof:5d}" +
              f"{Card02.nlvect:5d}" +
              f"{Card02.nltftn:5d}" +
              f"{Card02.nptslf:5d}" +
              f"{Card02.nptslf:5d}" +
              "\n")

        return [sb]
