# -*- coding: UTF-8 -*-

__title__ = "TEST"
__author__ = "FERMI"
__helpurl__ = "www.fermi.fr"
__highlight__ = "new"                               # Button will have an orange dot + Description in Revit UI
__min_revit_ver__ = 2022                            # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.
__max_revit_ver = 2023                             # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.
__context__     = ["doc-project"]
__doc__ = """Version = 0.1
Date    = November 2022
_____________________________________________________________________
Description:
Select all MEP élec elements in current document

_____________________________________________________________________
Last update:
- [November 2022]
_____________________________________________________________________
To-Do:
- update lists in selection
_____________________________________________________________________
Author: SAS FERMI"""

import clr
clr.AddReference("System")
clr.AddReference("RevitServices")

from pyrevit.forms import ProgressBar
# from pyrevit import revit, forms
from Snipets.Selection import SelectMepElectricalElements

doc = __revit__.ActiveUIDocument.Document
activeview = doc.ActiveView.Id
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application

progressbar_counter = 0
progressbar_step = 3


from Models.Object import ManufacturerProduct

if __name__ == '__main__':

    # Récupérer les instances des éléments du projete lectrique ok
    # Récupérer les types des éléments du projet ok

    # Récupérer les paramètres de type
    symbols = SelectMepElectricalElements(document=doc).get_unique_types
    # Symbols = Symbols.get_unique_types
    # elements = selection.all_elements_MEP_electrical


    with ProgressBar(title='Processing ... ({value} de {max_value})',cancellable=True) as pb:
        maxvalue = symbols.Count
        pb.max_value = maxvalue
        for s in symbols:
            product = ManufacturerProduct()
            parameters = product.key_Product_URL
            if pb.cancelled:
                break
            else :
                progressbar_counter += 1
                pb.update_progress(progressbar_counter,maxvalue)

                try:
                    p = [p.append(s.LookupParameter(parameter)) for parameter in parameters]

                except AttributeError:
                    print ("AttributeError !")

                print product.product_information

        print ('-' * 100)

    # schedulable = SelectMEP_All_ElectricalElements.schedulable(elements)
