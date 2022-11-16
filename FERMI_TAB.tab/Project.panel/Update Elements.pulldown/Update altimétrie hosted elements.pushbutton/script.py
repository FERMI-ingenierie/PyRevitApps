# -*- coding: utf-8 -*-

__title__ = "Update altimetry of hosted elements"
__author__ = "FERMI"
__helpurl__ = "www.fermi.fr"
__highlight__ = "new"                               # Button will have an orange dot + Description in Revit UI
__min_revit_ver__ = 2022                            # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.

import Autodesk.Revit.DB

__max_revit_ver = 2023                             # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.
__context__     = ["doc-project"]

# import os, sys, math, datetime, time
# from Autodesk.Revit.DB import *
from Autodesk.Revit.DB import FilteredElementCollector,\
                                BuiltInCategory,\
                                ElementClassFilter

# from pyrevit import revit, forms
# from Lib.Snipets._Selection import get_selected_elements

# import clr                                  # Common Language Runtime. Makes .NET libraries accessinble
# clr.AddReference("System")                  # Refference System.dll for import.
# from System.Collections.Generic import List # List<ElementType>() <- it's special type of list from .NET framework that RevitAPI requires
# List_example = List[ElementId]()          # use .Add() instead of append or put python list of ElementIds in parentesis.





doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application





class Elements :
    def __init__(self):
        self._elements = FilteredElementCollector(doc) \
            .OfCategory(BuiltInCategory.OST_ElectricalFixtures) \
            .WhereElementIsNotElementType() \
            .ToElements()
        self._Filtered =[]

    @property
    def elements (self):
        return self._elements

    @property
    def hosts (self):
        return [element.Host for element in self.elements]

    @property
    def hosted(self):
        filter_hosted = [element.HostFace for element in self._elements if element.HostFace]
        print (filter_hosted)

        # filterFixture = ElementClassFilter(BuiltInCategory.OST_ElectricalFixtures)
        # return FilteredElementCollector.WhereElementIsElementType(filterFixture)








if __name__ == '__main__':

    elements = Elements().hosted





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

