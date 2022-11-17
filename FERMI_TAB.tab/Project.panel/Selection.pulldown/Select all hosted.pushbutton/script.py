# -*- coding: UTF-8 -*-

__title__ = "Select all hosted elements"
__author__ = "FERMI"
__helpurl__ = "www.fermi.fr"
__highlight__ = "new"                               # Button will have an orange dot + Description in Revit UI
__min_revit_ver__ = 2022                            # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.
__max_revit_ver = 2023                             # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.
__context__     = ["doc-project"]
__doc__ = """Version = 1.0
Date    = November 2022
_____________________________________________________________________
Description:
Select all MEP élec elements in current view

_____________________________________________________________________
Last update:
- [November 2022]
_____________________________________________________________________
To-Do:
- all
_____________________________________________________________________
Author: SAS FERMI"""

import clr
clr.AddReference("System")
clr.AddReference("RevitServices")

from Autodesk.Revit.DB import FilteredElementCollector,\
                                BuiltInCategory,\
                                ElementId,\
                                BuiltInParameter,\
                                Element
from Snipets.Selection import SelectElementsInView
from Snipets.Views import GetActiveView, GetCurrentLevel
# from pyrevit import revit, forms


doc = __revit__.ActiveUIDocument.Document
activeview = doc.ActiveView.Id
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application


class ElementsElectricalFixtures :
    def __init__(self):
        pass

    @staticmethod
    def _get_elements(document, active_view):
        return FilteredElementCollector(document, active_view) \
            .OfCategory(BuiltInCategory.OST_ElectricalFixtures) \
            .WhereElementIsNotElementType() \
            .ToElements()

    @classmethod
    def all_elements (cls, document, active_view):
        return cls._get_elements(document=document, active_view=active_view)

    @classmethod
    def hosted_elements(cls, document, active_view):
        elements = cls.all_elements(document=document, active_view=active_view)
        return [element for element in elements if element.HostFace]


#
# def setNiveauDeNomenclature(elements, level):
#     for element in elements:
#         parameter = FER_Parameters.SetParameterValue()
#         FER_Parameters.SetParameterValue()
#         pass


        # SetParameterValue(
        #     ElementId
        # parameterId,
        # ParameterValue
        # pValue

# Elévation par rapport au niveau
# Niveau de nomenclature
# recup du niveau par Id : classe niveau AsElementId, Id, Elevation




if __name__ == '__main__':
    activeView = GetActiveView(document=doc)
    elementsInView = ElementsElectricalFixtures().hosted_elements(document=doc, active_view=activeview)
    List_ElementsIds = SelectElementsInView.ByElementId(elements=elementsInView)
    uidoc.Selection.SetElementIds(List_ElementsIds)