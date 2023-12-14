""" Modulo schede """


class Card01:
    """ Card01 Titolo lavoro"""

    def __init__(self):
        self.title = None

    def initialize(self, content, i) -> int:
        """Inizializzazione"""

        i += 1
        line_card = content[i].split("=")
        match line_card[0]:
            case "title":
                self.title = line_card[1]

        return i

    def to_string(self) -> list[str]:
        """Formattazione"""

        return [self.title, "\n"]
