# -*- coding: utf-8 -*-

from Autodesk.Revit.DB import *
from pyrevit import revit


class GetInstanceScheduleElementLevel:
    _parameter = "Niveau de nomenclature"
    def __init__(self):
        self._parameter = "Niveau de nomenclature"

    def _get_parameters (self, elements):
        return [element.GetParameters(self._parameter) for element in elements][0]

    @classmethod
    def as_string(cls,elements):
        parameter = [element.GetParameters(cls._parameter) for element in elements][0]
        return parameter.AsValueString()



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
