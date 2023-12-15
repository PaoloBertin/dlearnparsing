""" Modulo schede """
from cards.card1011 import Card1011
from cards.card1012 import Card1012
from cards.card1013 import Card1013
from cards.card1014 import Card1014


class Card101:
    """Elemento 2D elasticita' isotropa"""

    def __init__(self):
        """Inizializzazione"""

        self.card1011 = Card1011()
        self.card1012s = []
        self.card1013 = Card1013()
        self.card1014 = Card1014()

    def initialize(self, content, i):
        """ Inizializzazione """

        # lettura proprieta' del gruppo
        self.card1011 = Card1011()
        i = self.card1011.initialize(content, i)

        # lettura proprieta' materiali
        for j in range(self.card1011.numat):
            card1012 = Card1012()
            i = card1012.initialize(content, i)
            self.card1012s.append(card1012)

        # lettura componenti accelerazione di gravita'
        i = self.card1013.initialize(content, i)

        # lettura nodi elementi
        i = self.card1014.initialize(content, i)

        return i

    def to_string(self) -> list[str]:
        """Formattazione"""

        lb = []

        # dati generali gruppo
        lb = lb + self.card1011.to_string()

        # proprieta' materiali
        for card1012 in self.card1012s:
            lb = lb + card1012.to_string()

        # componenti accelerazione gravita'
        lb = lb + self.card1013.to_string()

        # nodi elementi
        lb = lb + self.card1014.to_string()

        return lb
