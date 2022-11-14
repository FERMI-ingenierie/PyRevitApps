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
__min_revit_ver__ = 2022                            # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.
__max_revit_ver = 2023                             # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.
__context__     = ["doc-family"]

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ Regular + Autodesk + pyRevit + Custom + .NET
# =====================================================================================================================

from Autodesk.Revit.DB import Transaction
from Snipets._Selection import get_all_shared_parameters

from pyrevit.forms import ProgressBar
from pyrevit import forms

import clr
clr.AddReference("System")
# from System.Collections.Generic import List


doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument


if __name__ == '__main__':


    selected_parameters = forms.select_family_parameters()
    if selected_parameters:
        pass



    #
    # parameters = get_all_shared_parameters(doc)
    #
    # with Transaction(doc) as transaction:
    #     transaction.Start()
    #
    #     try:
    #         for parameter in parameters:
    #             doc.Delete(parameter.Id)
    #     except (Exception)
    #         Forms.
    #
    #     transaction.Commit()
