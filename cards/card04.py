class Card04:
    """Storie nodali"""

    def __init__(self):
        self.idhist = []

    def initialize(self, content, i) -> int:
        """Inizializzazione"""
        return i

    def to_string(self) -> list[str]:
        """Formatting"""

        sb = []
        if len(self.idhist) > 0 and self.idhist is not None:
            sb.append(f"{self.idhist:5d}")

        return sb
