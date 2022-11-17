# -*- coding: UTF-8 -*-

__title__ = "Update altimetry of hosted elements"
__author__ = "FERMI"
__helpurl__ = "www.fermi.fr"
__highlight__ = "new"                               # Button will have an orange dot + Description in Revit UI
__min_revit_ver__ = 2022                            # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.
__max_revit_ver = 2023                             # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.
__context__     = ["doc-project"]

from Autodesk.Revit.DB import FilteredElementCollector,\
                                BuiltInCategory,\
                                BuiltInParameter,\
                                Element
import clr
clr.AddReference("System")
from System.Collections.Generic import List # List<ElementType>() <- it's special type of list from .NET framework that RevitAPI requires
import Snipets._Views as View
import Snipets._Parameters as Parameters
import Snipets._Selection as Selection



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
    def _get_elements(doc, active_view):
        return FilteredElementCollector(doc,active_view) \
            .OfCategory(BuiltInCategory.OST_ElectricalFixtures) \
            .WhereElementIsNotElementType() \
            .ToElements()

    @classmethod
    def elements (cls, doc, active_view):
        return cls._get_elements(doc=doc, active_view=active_view)

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

if __name__ == '__main__':
    # get curent view
    # get elements in view
    # Update schedule level
    # get elements parameter Elevation par rapport au niveau
    # update altimetrie shared parameter
    # end report

    currentLevel = View.GetCurrentLevel(doc=doc)
    activeView = View.GetActiveView(doc=doc)

    elements = ElementsElectricalFixtures().elements(doc,activeview)

    print (elements)






    # test= GetInstanceScheduleElementLevel.as_string(elements=elements)


    #
    # for e in elements:
    #     params = e.GetParameters("Niveau de nomenclature")
    #     print params
    #     print params[0].AsValueString()
    #     # element = e.GetParameters("Niveau de nomenclature")
    #     # print (element)

    # Autodesk.Revit.DB.Element.GetParameters("Niveau de nomenclature")




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

