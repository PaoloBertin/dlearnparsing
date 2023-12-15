""" Controller  """
from cards.card_manager import Cards

FILE_INPUT = "example2.dat"
# FILE_OUTPUT = "example2.ris"
FILE_OUTPUT = "/home/paolo-bertin/Documenti/FortranProjects/dlearn/data/example2.dat"

controller = Cards(FILE_INPUT, FILE_OUTPUT)
controller.initialize()
controller.write_to_file()
