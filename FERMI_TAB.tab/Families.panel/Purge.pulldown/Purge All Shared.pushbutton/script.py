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

import time

__max_revit_ver = 2023                             # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.
__context__     = ["doc-family"]

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ Regular + Autodesk + pyRevit + Custom + .NET
# =====================================================================================================================
import time
from Autodesk.Revit.DB import Transaction, TransactionStatus
from Snipets._Selection import get_all_shared_parameters
from pyrevit.forms import ProgressBar, alert
from pyrevit.revit import Transaction

import clr
clr.AddReference("System")
# from System.Collections.Generic import List


doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument


if __name__ == '__main__':
    parameters = get_all_shared_parameters(doc)

    pb_cur_value, pb_max_value = 0, len(parameters)

    with Transaction(__title__) as transaction:
        with ProgressBar(title='Erase Shared parameters ... ({value} of {max_value})') as pb:
            for parameter in parameters:
                doc.Delete(parameter.Id)
                pb_cur_value =+1
                pb.update_progress(pb_cur_value, pb_max_value)
                time.sleep(0.05)

    # alert('Tous les paramètres partagés sont supprimés.', exitscript=True)

