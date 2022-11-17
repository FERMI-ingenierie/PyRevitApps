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
                                ElementId,\
                                BuiltInParameter,\
                                Element

import clr
clr.AddReference("System")
clr.AddReference("RevitServices")
from System.Collections.Generic import List # List<ElementType>() <- it's special type of list from .NET framework that RevitAPI requires
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

    activeView = FER_View.GetActiveView(doc=doc)
    elementsInView = ElementsElectricalFixtures().hosted_elements(document=doc, active_view=activeview)
    # currentLevel = FER_View.GetCurrentLevel(doc=doc)
    print (elementsInView)
    elementsIds = List
    for element in elementsInView:
        elementsIds.Add(element.Id)

    # elementsIds. = [element.Id for element in elementsInView]
    # selection = uidoc.Selection.SetElementIds(elementsIds)
    print (elementsIds)
    print (type(elementsIds))




    # for element in elementsInView:
    #     parameter = element.get_Parameter(BuiltInParameter.SCHEDULE_LEVEL_PARAM)
    #     print parameter.AsValueString()
    #     parameter.UserModifiable.(True)


# Autodesk.Revit.UI.Selection.Selection.PickObjects()
# Autodesk.Revit.UI.Selection.Selection.SetElementIds()
# https://www.revitapidocs.com/2015/a2847bd6-bcac-9233-584f-77ca54c4a800.htm

# https://teocomi.com/dynamo-select-revit-element-by-id/



# Autodesk.Revit.DB.Parameter.UserModifiable






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

