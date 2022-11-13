# -*- coding: utf-8 -*-
# ! python3

__title__ = "Update altimetry of hosted elements"
__doc__ = """Version = 0.1
Date    = Novembre 2022
_____________________________________________________________________
Description:

Mise à jour de
  - level
  - altimetry parameter on hosted elements 
_____________________________________________________________________
How-to:

-> Click on the button
        script select all elements on active level
        scripts assign correct level
        script update altimetry on hosted elements
-> wait & enjoy
_____________________________________________________________________
Last update:
- [novembre 2022]
_____________________________________________________________________
To-Do:
- all
_____________________________________________________________________
Author: SAS FERMI"""

# EXTRA: You can remove them.
__author__ = "FERMI"
__helpurl__ = "www.fermi.fr"
__highlight__ = "new"  # Button will have an orange dot + Description in Revit UI
__min_revit_ver__ = 2022  # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.
__max_revit_ver = 2023  # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.
# __context__     = ['Walls', 'Floors', 'Roofs']    # Make your button available only when certain categories are selected. Or Revit/View Types.

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# ==================================================
import os

from Autodesk.Revit.DB import *
from pyrevit import *



# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝
doc = __revit__.ActiveUIDocument.Document  # Document   class from RevitAPI that represents project. Used to Create, Delete, Modify and Query elements from the project.
uidoc = __revit__.ActiveUIDocument  # UIDocument class from RevitAPI that represents Revit project opened in the Revit UI.
app = __revit__.Application  # Represents the Autodesk Revit Application, providing access to documents, options and other application wide data and settings.
PATH_SCRIPT = os.path.dirname(__file__)  # Absolute path to the folder where script is placed.


# GLOBAL VARIABLES

# - Place global variables here.

# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝ FUNCTIONS
# ==================================================

# - Place local functions here. If you might use any functions in other scripts, consider placing it in the lib folder.

FilteredElementCollector.O


# ╔═╗╦  ╔═╗╔═╗╔═╗╔═╗╔═╗
# ║  ║  ╠═╣╚═╗╚═╗║╣ ╚═╗
# ╚═╝╩═╝╩ ╩╚═╝╚═╝╚═╝╚═╝ CLASSES
# ==================================================

# - Place local classes here. If you might use any classes in other scripts, consider placing it in the lib folder.

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
# ==================================================
if __name__ == '__main__':
    # START CODE HERE

    # AVOID  placing Transaction inside of your loops! It will drastically reduce perfomance of your script.
    # t = Transaction(doc,__title__)  # Transactions are context-like objects that guard any changes made to a Revit model.

    # You need to use t.Start() and t.Commit() to make changes to a Project.
    # t.Start()  # <- Transaction Start

    # - CHANGES TO REVIT PROJECT HERE

    # t.Commit()  # <- Transaction End

    # Notify user that script is complete.
    print('-' * 50)
    print('Script is finished.')
    print('Template has been developed by FERMI _ Jérôme PETITJEAN.')
