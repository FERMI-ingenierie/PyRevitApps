# -*- coding: utf-8 -*-

__title__ = "Update altimetry of hosted elements"
__author__ = "FERMI"
__helpurl__ = "www.fermi.fr"
__highlight__ = "new"                               # Button will have an orange dot + Description in Revit UI
__min_revit_ver__ = 2022                            # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.
__max_revit_ver = 2023                             # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.
__context__     = ["doc-project"]


from Autodesk.Revit.DB import FilteredElementCollector,\
                                BuiltInCategory,\
                                BuiltInParameter
from Snipets._Views import GetCurrentLevel
from Snipets._Parameters import PyParameters


# from pyrevit import revit, forms
# from Lib.Snipets._Selection import get_selected_elements

# import clr                                  # Common Language Runtime. Makes .NET libraries accessinble
# clr.AddReference("System")                  # Refference System.dll for import.
# from System.Collections.Generic import List # List<ElementType>() <- it's special type of list from .NET framework that RevitAPI requires
# List_example = List[ElementId]()          # use .Add() instead of append or put python list of ElementIds in parentesis.





doc = __revit__.ActiveUIDocument.Document
activeview = doc.ActiveView.Id
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application





class Elements :
    def __init__(self):
        self._elements = FilteredElementCollector(doc,activeview) \
            .OfCategory(BuiltInCategory.OST_ElectricalFixtures) \
            .WhereElementIsNotElementType() \
            .ToElements()

    @property
    def elements (self):
        return self._elements

    @property
    def hosted_elements(self):
        return [element for element in self._elements if element.HostFace]
#     INSTANCE_FREE_HOST_PARAM

class UpdateHeightHosted:
    def __init__(self, doc, activeview, elements):
        self._doc = doc
        self._activeView = activeview
        self._elements = elements
        self._currentLevel= GetCurrentLevel(self._doc)

    def setNiveauDeNomenclature(self):
        niv = self._currentLevel.Name
        print (niv)

        # SetParameterValue(
        #     ElementId
        # parameterId,
        # ParameterValue
        # pValue

# Elévation par rapport au niveau
# Niveau de nomenclature
# recup du niveau par Id : classe niveau AsElementId, Id, Elevation

from Snipets._Views import GetCurrentLevel
from Snipets._Parameters import PyParameters

if __name__ == '__main__':

    elements = Elements().elements
    print (elements)

    for e in elements:
        h = e.GetParameters("Niveau de nomenclature")
        print (h[0].AsString())





    # print ("go")
    # selected = FilteredElementCollector(doc) \
    #     .OfCategory(BuiltInCategory.OST_ElectricalFixtures) \
    #     .WhereElementIsNotElementType() \
    #     .ToElements()
    #
    # hosted = [select.Host for select in selected]
    #
    #
    #
    #
    # print ("hosted")
    # for h in hosted:
    #     print (h, " / ", h)

