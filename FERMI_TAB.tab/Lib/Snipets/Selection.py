# -*- coding: utf-8 -*-

from collections import Iterable

import clr
clr.AddReference("System")
from System.Collections.Generic import List

from Autodesk.Revit.DB import *
# from Autodesk.Revit.DB import SharedParameterElement,\
#                                 ParameterElement,\
#                                 FilteredElementCollector,\
#                                 Element,\
#                                 ElementId,\
#                                 ElementType,\
#                                 BuiltInCategory,\
#                                 ElementParameterFilter,\
#                                 ParameterValueProvider,\
#                                 BuiltInParameter,\
#                                 ElementMulticategoryFilter,\
#                                 ElementFilter,FamilySymbol, ElementSet

from Snipets.Filters import MEP_Electrical_Categories



uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document





class SelectMEP_All_ElectricalElements:

    List_Elements = List[Element]()
    List_ElementsId = List[ElementId]()
    filter = MEP_Electrical_Categories()

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

    @staticmethod
    def get_unique_types(elements):
        """
        return all type Symbols for MEP electrical elements as unique

        :param elements: Elements instance as iterable
        :type elements: Iterable
        :return: Symbol(s)
        :rtype: List
        """
        List_types = List[FamilySymbol]()

        elements = [elements] if not isinstance(elements, Iterable) else elements
        types = ElementSet()

        for element in elements:
            types.Insert(element.Symbol)

        for typ in types:
            List_types.Add(typ)

        return List_types

    @staticmethod
    def get_types_ids(symbols):
        """
        return all type Ids for MEP electrical elements

        :param symbols: Symbols elements as iterable
        :type symbols: Iterable
        :return: List[Symbols]
        :rtype: List
        """
        List_Ids = List[ElementId]()
        symbols = [symbols] if not isinstance(symbols, Iterable) else symbols

        for symbol in symbols:
            List_Ids.Add(symbol.Id)

        return List_Ids




    @classmethod
    def schedulable(cls, elements):
        types = cls.get_unique_types(elements)

        for typ in types:
            print typ.GetParameter("SP_FER_SCH_Schedulable").AsInteger()






        ids = cls.get_types_ids(types)
        print ('-' * 100)
        for id in ids:
            print id


        # typeId = [element.Symbol for element in elements]
        # for type in types:
        #     shared = type.get_Parameter(BuiltInParameter.ALL_MODEL_TYPE_COMMENTS)
        #     print shared.AsValueString()






# def get_parameter_value_by_name(elements, parameterName):
#     if isinstance(elements, Iterable):
#         for element in elements:
#             print element.LookupParameter(parameterName).AsValueString()




        # print Type.get_Parameter(BuiltInParameter.ALL_MODEL_TYPE_COMMENTS)





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
