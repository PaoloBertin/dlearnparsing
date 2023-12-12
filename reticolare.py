""" Importa classi schede """
import os

from cards.card_manager import Cards

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print(f"Files in {cwd:s} {files:}")

controller = Cards("reticolare.dat", "reticolare.inp")
controller.initialize()
controller.write_to_file()
