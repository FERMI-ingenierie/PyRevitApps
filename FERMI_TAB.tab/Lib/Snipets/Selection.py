# -*- coding: utf-8 -*-

from collections import Iterable

import clr
clr.AddReference("System")
from System.Collections.Generic import List

from Autodesk.Revit.DB import SharedParameterElement,\
                                ParameterElement,\
                                FilteredElementCollector,\
                                Element,\
                                ElementId,\
                                BuiltInCategory,\
                                ElementParameterFilter,\
                                ParameterValueProvider,\
                                BuiltInParameter,\
                                ElementMulticategoryFilter,\
                                ElementFilter

from Snipets.Filters import all_MEP_electrical

uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document

class SelectMEP_All_ElectricalElements:

    List_Elements = List[Element]()
    List_ElementsId = List[ElementId]()
    filter = all_MEP_electrical()

    def __init__(self, document):
        self.List_Elements = FilteredElementCollector(document)\
                                .WherePasses(self.filter)\
                                .WhereElementIsNotElementType()\
                                .ToElements()
    @property
    def all_elements_MEP_electrical(self):
        """
        return all element MEP electrical define by filter

        :return: Elements
        :rtype: List
        """
        return self.List_Elements

    @property
    def all_elementsIds_MEP_electrical(self):
        """
        return all element Ids MEP electrical define by filter

        :return: Elements
        :rtype: List
        """
        for element in self.List_Elements:
            self.List_ElementsId.Add(element.Id)

        return self.List_ElementsId



# def get_parameter_value_by_name(elements, parameterName):
#     if isinstance(elements, Iterable):
#         for element in elements:
#             print element.LookupParameter(parameterName).AsValueString()



def get_schedulable_elements(elements):
    print elements
    for element in elements:
        print element.GetType.get_Parameter(BuiltInParameter.ALL_MODEL_TYPE_COMMENTS)







        # print (element.GetParameters('SP_FER_SCH_Schedulable').AsInteger())






    #
    # @property
    # def get_MEP_class(self):
    #     return None
    #
    # @property
    # def get_MEP_subclass(self):
    #     return None
    #
    # @property
    # def get_MEP_schedulable(self):
    #     return None
    #
    # @property
    # def filename(self):
    #     return None
    #
    # @property
    # def geturl(self):
    #     return None



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
