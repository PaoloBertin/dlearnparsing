""" Importa schede  """

import os

from cards.card00 import Card00
from cards.card01 import Card01
from cards.card02 import Card02
from cards.card03 import Card03
from cards.card04 import Card04
from cards.card05 import Card05
from cards.card06 import Card06
from cards.card07 import Card07
from cards.card08 import Card08
from cards.card09 import Card09
from cards.card10 import Card10


class Cards:
    """Creazione contenuto schede ed assemblaggio"""

    cd00 = Card00()
    cd01 = Card01()
    cd02 = Card02()
    cd03 = Card03()
    cd04 = Card04()
    cd05 = Card05()
    cd06 = Card06()
    cd07 = Card07()
    cd08 = Card08()
    cd09 = Card09()
    cd10 = Card10()

    content = []

    def __init__(self, file_name_input, file_name_output):
        self.file_name_input = file_name_input
        self.file_name_output = file_name_output

    def initialize(self):
        """Inizializzazione schede"""

        with open(self.file_name_input, "r", encoding="utf-8") as open_file_input:
            self.content = open_file_input.read().splitlines()

            rows = len(self.content) - 1
            i = 0
            parameters = self.content[i].split(",")
            title = parameters[0]
            while title != "*end" and i < rows:
                if parameters[0].startswith("*"):
                    match title:
                        case "*card00":
                            i = self.cd00.initialize(self.content, i)
                        case "*card01":
                            i = self.cd01.initialize(self.content, i)
                        case "*card02":
                            i = self.cd02.initialize(self.content, i)
                        case "*card03":
                            i = self.cd03.initialize(self.content, i)
                        case "*card04":
                            i = self.cd04.initialize(self.content, i)
                        case "*card05":
                            i = self.cd05.initialize(self.content, i)
                        case "*card06":
                            i = self.cd06.initialize(self.content, i)
                        case "*card07":
                            i = self.cd07.initialize(self.content, i)
                        case "*card08":
                            i = self.cd08.initialize(self.content, i)
                        case "*card09":
                            i = self.cd09.initialize(self.content, i)
                        case "*card10":
                            i = self.cd10.initialize(self.content, i)
                i += 1
                parameters = self.content[i].split(",")
                title = parameters[0]

    def write_to_file(self) -> list[str]:
        """Crea contenuto in output"""

        lb = []

        lb = (lb
              + self.cd00.to_string()
              + self.cd01.to_string()
              + self.cd02.to_string()
              + self.cd03.to_string()
              + self.cd04.to_string()
              + self.cd05.to_string()
              + self.cd06.to_string()
              + self.cd07.to_string()
              + self.cd08.to_string()
              + self.cd09.to_string()
              + self.cd10.to_string()
              + ["\n"]
              + ["*end"]
              )

        with open(self.file_name_output, "w", encoding="utf-8") as output:
            for item in lb:
                output.write(item)
            print("Done")

        return lb
