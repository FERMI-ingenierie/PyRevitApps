# -*- coding: UTF-8 -*-

__title__ = "Update altimetry of hosted elements"
__author__ = "FERMI"
__helpurl__ = "www.fermi.fr"
__highlight__ = "new"                               # Button will have an orange dot + Description in Revit UI
__min_revit_ver__ = 2022                            # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.
__max_revit_ver = 2023                             # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.
__context__     = ["doc-project"]

from collections import Iterable
from Autodesk.Revit.DB import FilteredElementCollector,\
                                BuiltInCategory,\
                                ElementId,\
                                BuiltInParameter,\
                                Element

import clr
clr.AddReference("System")
clr.AddReference("RevitServices")
from System.Collections.Generic import List
from RevitServices.Persistence import DocumentManager

import Snipets._Views as FER_View
import Snipets._Parameters as FER_Parameters
import Snipets._Selection as FER_Selection




from Snipets._Parameters import GetInstanceScheduleElementLevel

# from pyrevit import revit, forms
# from Lib.Snipets._Selection import get_selected_elements

# List_example = List[ElementId]()          # use .Add() instead of append or put python list of ElementIds in parentesis.


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
    # get curent view  > ok
    # get elements in view   > ok
    # filter hosted
    # Update schedule level
    # get elements parameter Elevation par rapport au niveau
    # update altimetrie shared parameter
    # end report

    activeView = FER_View.GetActiveView(document=doc)
    elementsInView = ElementsElectricalFixtures().hosted_elements(document=doc, active_view=activeview)
    currentLevel = FER_View.GetCurrentLevel(document=doc)
    List_ElementsIds = FER_Selection.Select_elements_in_active_view_by_element(elementsInView)
    uidoc.Selection.SetElementIds(List_ElementsIds)