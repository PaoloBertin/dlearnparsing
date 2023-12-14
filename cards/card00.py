""" Modulo schede """


class Card00:
    """Echo dati"""

    def __init__(self):
        self.iecho = None

    def initialize(self, content, i) -> int:
        """Inizializzazione scheda 0"""
        i += 1
        line_card = content[i].split("=")
        match line_card[0]:
            case "iecho":
                self.iecho = int(line_card[1])

        return i

    def to_string(self) -> list[str]:
        """Formattazione campi classe"""

        sb = [f"{self.iecho:5d}", "\n"]

        return sb
