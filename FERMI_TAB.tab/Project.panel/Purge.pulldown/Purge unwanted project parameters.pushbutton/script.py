# -*- coding: utf-8 -*-
#! python3

__title__ = "TEST"
__author__ = "SAS FERMI"
__doc__ = "Get and delete shared parameters with shared parameters"

from Snipets._Selection import get_all_shared_parameters

uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document


if __name__ == '__main__':
    params = get_all_shared_parameters(doc)
    print(params)
    for p in params:
        print(p.Name)
