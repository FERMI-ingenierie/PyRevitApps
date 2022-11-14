# -*- coding: utf-8 -*-


__title__ = "Get and delete all shared parameters"
__doc__ = """Version = 0.1
Date    = November 2022
_____________________________________________________________________
Description:

delete all shared parameters in open family

_____________________________________________________________________
How-to:

-> open a family
-> Execute
-> Enjoy
_____________________________________________________________________
Last update:
- [November 2022]
_____________________________________________________________________
To-Do:
- all
_____________________________________________________________________
Author: SAS FERMI"""

__author__ = "FERMI"
__helpurl__ = "www.fermi.fr"
__highlight__ = "new"                               # Button will have an orange dot + Description in Revit UI
__min_revit_ver__ = 2022                            # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.
__max_revit_ver = 2023                             # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.
__context__     = ["doc-family"]

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ Regular + Autodesk + pyRevit + Custom + .NET
# =====================================================================================================================

from Autodesk.Revit.DB import *
from Snipets._Selection import get_all_shared_parameters

import clr
clr.AddReference("System")
# from System.Collections.Generic import List


doc = __revit__.ActiveUIDocument.Document
familyManager= doc.FamilyManager

uidoc = __revit__.ActiveUIDocument


if __name__ == '__main__':
    with Transaction(doc, __title__) as t:
        t.Start()
        parameters = get_all_shared_parameters(doc)
        for parameter in parameters:
            doc.Delete(parameter.Id)
        t.Commit()
