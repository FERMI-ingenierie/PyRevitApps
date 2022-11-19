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
from Models.Object import ManufacturerProduct

doc = __revit__.ActiveUIDocument.Document
activeview = doc.ActiveView.Id
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application

progressbar_counter = 0
progressbar_step = 40



products = []
product_parameters = ManufacturerProduct().parameters_names

if __name__ == '__main__':

    # Récupérer les instances des éléments du projete lectrique ok
    # Récupérer les types des éléments du projet ok

    # Récupérer les paramètres de type

    # Symbols = Symbols.get_unique_types
    # elements = selection.all_elements_MEP_electrical


    with ProgressBar(title='Processing ... ({value} de {max_value})',
                     cancellable=True,
                     step = progressbar_step) as pb:

        symbols = SelectMepElectricalElements(document=doc).get_unique_types

        for symbol in symbols:
            product = ManufacturerProduct()

            if pb.cancelled:
                break
            else :
                try:
                    maxvalue = symbols.Count * len(product_parameters)
                    for parameter in product_parameters:
                        progressbar_counter += 1
                        pb.update_progress(progressbar_counter, maxvalue)
                        result = symbol.LookupParameter(parameter).AsValueString()
                        setattr(product,parameter, symbol.LookupParameter(parameter).AsValueString())

                    products.append(product)

                except :
                    pass

        print ('-' * 100)
        print products
        print ('-' * 100)
        for p in products:
            print p.test

