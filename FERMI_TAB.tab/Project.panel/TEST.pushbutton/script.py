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


from pyrevit.forms import ProgressBar as PB

class ProgressBar (PB):
    super(PB).__init__()
    counter = 0

    def update (self):
        self.counter += 1
        self.update_progress(self.counter, self.max_value)

progressbar = ProgressBar()


max_value = 1000
with ProgressBar() as pb:
    for counter in range(0, max_value):
        pb.update_progress(counter, max_value)



if __name__ == '__main__':
    # Récupérer les instances des éléments du projete lectrique ok
    # Récupérer les types des éléments du projet ok

    # Récupérer les paramètres de type
    symbols = SelectMepElectricalElements(document=doc).get_unique_types
    # Symbols = Symbols.get_unique_types
    # elements = selection.all_elements_MEP_electrical

    progressbar.max_value = len(symbols)

    for s in symbols:
        progressbar.update()
        print s.get_Parameter(BuiltInParameter.ALL_MODEL_DESCRIPTION).AsValueString()

    print ('-' * 100)

    for s in symbols:
        try:
            param = s.LookupParameter('SP_FER_SCH_Schedulable').AsInteger()
            print param
        except AttributeError:
            print "0 - correction"

    print ('-' * 100)
    print symbols.Count

    # schedulable = SelectMEP_All_ElectricalElements.schedulable(elements)
