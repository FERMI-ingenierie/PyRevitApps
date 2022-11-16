# -*- coding: utf-8 -*-
from  Autodesk.Revit.DB import *



def GetCurrentLevel(doc):
    activeView = doc.ActiveView
    # activelevel = activeView.LookupParameter("Associated Level")
    return activeView.GenLevel
    #
    # Document
    # doc = uiapp.ActiveUIDocument.Document;
    # View
    # activeView = doc.ActiveView;
    # Level
    # level = activeView.GenLevel;
    # ElementId
    # levelId = level.Id;
    # string
    # levelName = level.Name;