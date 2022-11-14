# -*- coding: utf-8 -*-

# from Autodesk.Revit.DB import *
from Autodesk.Revit.DB import SharedParameterElement\
                                ,ParameterElement\
                                ,FilteredElementCollector

uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document


def get_selected_elements(uidoc):
    """ Retrieve all elements which are selected in Revit
    :param uidoc:   uidoc where elements are selected
    :return:        List of elements
    """
    return [uidoc.Document.GetElement(elem_id) for elem_id in uidoc.Selection.GetElementIds()]


def get_all_parameters(doc):
    """ Retrieve all parameters in active doc
    :param doc:   current active document
    :return:      List of parameters
    """
    return FilteredElementCollector(doc).OfClass(ParameterElement)

def get_all_shared_parameters(doc):
    """ Retrieve all shared parameters in active doc
    :param doc:   current active document
    :return:      List of shared parameters
    """
    return [parameter for parameter in get_all_parameters(doc) if isinstance(parameter, SharedParameterElement)]
