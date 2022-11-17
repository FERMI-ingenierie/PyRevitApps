# -*- coding: utf-8 -*-


def GetActiveView(doc):
    return doc.ActiveView

def GetCurrentLevel(doc):
    return doc.ActiveView.GenLevel
