# -*- coding: utf-8 -*-

__title__ = "Update altimetry of hosted elements"
__author__ = "FERMI"
__helpurl__ = "www.fermi.fr"
__highlight__ = "new"                               # Button will have an orange dot + Description in Revit UI
__min_revit_ver__ = 2022                            # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.
__max_revit_ver = 2023                             # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.
__context__     = ["doc-project"]

# import os, sys, math, datetime, time
from Autodesk.Revit.DB import *
# from pyrevit import revit, forms
# from Lib.Snipets._Selection import get_selected_elements

# import clr                                  # Common Language Runtime. Makes .NET libraries accessinble
# clr.AddReference("System")                  # Refference System.dll for import.
# from System.Collections.Generic import List # List<ElementType>() <- it's special type of list from .NET framework that RevitAPI requires
# List_example = List[ElementId]()          # use .Add() instead of append or put python list of ElementIds in parentesis.





doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application



















if __name__ == '__main__':
    print ("go")
    select = FilteredElementCollector(doc) \
        .OfCategory(BuiltInCategory.OST_ElectricalEquipment) \
        .WhereElementIsNotElementType() \
        .ToElements()
    print ("selected")
    for s in select:
        print s.name

    print (select)