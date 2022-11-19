# -*- coding: UTF-8 -*-

__title__ = "TEST"
__author__ = "FERMI"
__helpurl__ = "www.fermi.fr"
__highlight__ = "new"                               # Button will have an orange dot + Description in Revit UI
__min_revit_ver__ = 2022                            # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.
__max_revit_ver = 2023                             # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.
__context__     = ["doc-project"]
__doc__ = """Version = 0.1
Date    = November 2022
_____________________________________________________________________
Description:
Select all MEP élec elements in current document

_____________________________________________________________________
Last update:
- [November 2022]
_____________________________________________________________________
To-Do:
- update lists in selection
_____________________________________________________________________
Author: SAS FERMI"""

import clr
clr.AddReference("System")
clr.AddReference("RevitServices")
from System.Collections.Generic import List

from Autodesk.Revit.DB import FilteredElementCollector,\
                                BuiltInCategory,\
                                ElementId,\
                                BuiltInParameter,\
                                Element,ElementFilter,ElementMulticategoryFilter


from Snipets.Selection import SelectMepElectricalElements
from Snipets.Views import GetActiveView, GetCurrentLevel



# from pyrevit import revit, forms


doc = __revit__.ActiveUIDocument.Document
activeview = doc.ActiveView.Id
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application





if __name__ == '__main__':
    # Récupérer les instances des éléments du projete lectrique
    # Récupérer les types des éléments du projet
    # Récupérer les paramètres de type
    Symbols = SelectMepElectricalElements(document=doc).get_unique_types
    # Symbols = Symbols.get_unique_types
    # elements = selection.all_elements_MEP_electrical

    print Symbols


    # schedulable = SelectMEP_All_ElectricalElements.schedulable(elements)
