# -*- coding: utf-8 -*-

import clr
clr.AddReference("System")
from System.Collections.Generic import List

from Autodesk.Revit.DB import SharedParameterElement,\
                                ParameterElement,\
                                FilteredElementCollector,\
                                Element,\
                                ElementId,\
                                BuiltInCategory,\
                                ElementParameterFilter,ParameterValueProvider,BuiltInParameter, ElementMulticategoryFilter, ElementFilter

doc = __revit__.ActiveUIDocument.Document



def MEP_Electrical_Categories():
    categories = List[BuiltInCategory]()
    builtincategories = [BuiltInCategory.OST_ElectricalFixtures,
                            BuiltInCategory.OST_ElectricalEquipment,
                            BuiltInCategory.OST_LightingFixtures,
                            BuiltInCategory.OST_LightingDevices,
                            BuiltInCategory.OST_DataDevices,
                            BuiltInCategory.OST_FireAlarmDevices,
                            BuiltInCategory.OST_SecurityDevices,
                            BuiltInCategory.OST_CommunicationDevices,
                            BuiltInCategory.OST_Site]
    for category in builtincategories:
        categories.Add(category)

    return ElementMulticategoryFilter(categories)
