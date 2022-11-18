# -*- coding: utf-8 -*-

from collections import Iterable

import clr
clr.AddReference("System")
from System.Collections.Generic import List

from Autodesk.Revit.DB import SharedParameterElement,\
                                ParameterElement,\
                                FilteredElementCollector,\
                                Element,\
                                ElementId
from Autodesk.Revit.DB.Electrical import *

uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document


class SelectMEP_All_ElectricalElements:

    def __init__(self, document):
        self.List_Elements = List[Element]()
        self.List_ElementsId = List[ElementId]()
        all_electrical = FilteredElementCollector(document)\
                                .OfClass(ElectricalSystem)\
                                .WhereElementIsNotElementType()\
                                .ToElements()
        print all_electrical
        for element in all_electrical:
            self.List_Elements.Add(element)
            self.List_ElementsId.Add(element.Id)
            print element
            print element.Id

    @property
    def all_elements_MEP_electrical(self):
        return self.List_Elements

    @property
    def all_elements_MEP_electricalIds(self):
        return self.List_ElementsId

    @property
    def get_MEP_class(self):
        return None

    @property
    def get_MEP_subclass(self):
        return None

    @property
    def get_MEP_schedulable(self):
        return None

    @property
    def filename(self):
        return None

    @property
    def geturl(self):
        return None



class SelectElementsInView:
    List_ElementsIds = List[ElementId]()

    def __init__(self):
        pass

    @classmethod
    def ByElementId(cls,elements):
        """
        Select all element in active view.
        By Id

        :param elements: Element as iterable
        :return: None
        """
        if not isinstance(elements, Iterable):
            cls.List_ElementsIds.Add(elements.Id)
        else:
            for element in elements:
                cls.List_ElementsIds.Add(element.Id)
        return cls.List_ElementsIds



def Select_elements_in_active_view_by_element(elements):
    """
    Retrieve all elements which are selected in Revit

    :param elements: Element as iterable
    :type elements: List[Element]()
    :return: None
    :rtype: None
    """

    List_ElementsIds = List[ElementId]()

    if not isinstance(elements, Iterable):
        List_ElementsIds.Add(elements.Id)
    else:
        for element in elements:
            List_ElementsIds.Add(element.Id)
    return List_ElementsIds

def get_selected_elements(uidoc):
    """
    Retrieve all elements which are selected in Revit

    :param uidoc:   uidoc where elements are selected
    :type uidoc:   __revit__.ActiveUIDocument
    :return:        List of elements
    :rtype:        Element
    """
    return [uidoc.Document.GetElement(elem_id) for elem_id in uidoc.Selection.GetElementIds()]

def get_all_parameters(document):
    """ Retrieve all parameters in active doc
    :param document:   current active document
    :return:      List of parameters
    """
    return FilteredElementCollector(document).OfClass(ParameterElement)

def get_all_shared_parameters(document):
    """ Retrieve all shared parameters in active doc
    :param document:   current active document
    :return:      List of shared parameters
    """
    return [parameter for parameter in get_all_parameters(document) if isinstance(parameter, SharedParameterElement)]
