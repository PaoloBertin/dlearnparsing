""" Analisi elemento reticolare """
from cards.card_manager import Cards

FILE_INPUT = "truss.dat"
FILE_OUTPUT = "/home/paolo-bertin/Documenti/FortranProjects/dlearn/data/truss.dat"
controller = Cards(FILE_INPUT, FILE_OUTPUT)
controller.initialize()
controller.write_to_file()
