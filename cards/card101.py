""" Modulo schede """


class Card101:
    """Elemento 2D elasticita' isotropa"""

    def __init__(self):
        """Inizializzazione"""
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
        #
        self.card1022s = []
        self.card1023 = Card1023()
        self.card1024s = []


    def initialize(self, content, i):
        """Inizializzazione"""

        return i
