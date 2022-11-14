# -*- coding: utf-8 -*-

from Autodesk.Revit.DB import *
from pyrevit import revit


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
