# -*- coding: utf-8 -*-

__title__ = "Link nested électrical connector parameters with shared parameters"
__author__ = "SAS FERMI"
__doc__ = "Link nested électrical connector parameters with shared parameters"

uidoc = __revit__.ActiveUIDocument

from Snipets.Selection import get_selected_elements

if __name__ == '__main__':
    print(get_selected_elements(uidoc))
