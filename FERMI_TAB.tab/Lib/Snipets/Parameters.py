# -*- coding: utf-8 -*-

import collections
from Autodesk.Revit.DB import Element,\
                                BuiltInParameter

import clr
clr.AddReference("System")
from System.Collections.Generic import List

# FAMILY_WPB_DEFAULT_ELEVATION => Elévation par défaut
# INSTANCE_ELEVATION_PARAM => Élévation par rapport au niveau
# INSTANCE_SCHEDULE_ONLY_LEVEL_PARAM => Niveau de nomenclature
# ELEM_TYPE_PARAM => Type
# ELEM_FAMILY_PARAM => Famille

# PHASE_DEMOLISHED => Phase de démolition
# PHASE_CREATED => Phase de création
# ELEM_ROOM_NAME => Nom de la pièce
# ELEM_ROOM_NUMBER => Numéro de la pièce
# ALL_MODEL_TYPE_NAME => Nom du type
# ALL_MODEL_FAMILY_NAME => Nom de la famille






# class GetInstanceScheduleElementLevel:
#     _parameter = "Niveau de nomenclature"
#
#     def __init__(self):
#         pass
#
#     @classmethod
#     def as_string(cls, elements):
#         """
#         Return all elements parameter 'Niveau de nomenclature' value as string
#
#         :param elements: List of elements
#         :type elements: List
#         :return: List of values as string
#         :rtype: List
#         """
#         if isinstance(elements, collections.Iterable):
#             return [element.GetParameters(cls._parameter)[0].AsValueString() for element in elements]
#         else:
#             return elements.GetParameters(cls._parameter).AsValueString


def SetParameterId():
    pass


def SetParameterValue():
    pass


        #     ElementId
        # parameterId,
        # ParameterValue
        # pValue
# INSTANCE_SCHEDULE_ONLY_LEVEL_PARAM

@classmethod
class PyParameters:
    def __init__(self,elements):
        self.element = elements
        pass

    def Id(self):
        return Element.GetParameters(BuiltInParameter.INSTANCE_SCHEDULE_ONLY_LEVEL_PARAM)

    def name(self, Id):
        return True



class PyFamilySharedParameters :

    def __init__(self):
        self.shared_parameters = "test"

    @property
    def shared_parameters (self):
        return self.shared_parameters

    @shared_parameters.setter
    def shared_parameters(self,value):
        self.shared_parameters = "test"


    @shared_parameters.deleter
    def shared_parameters(self):
        self.shared_parameters = "test"
