# -*- coding: utf-8 -*-


def GetActiveView(document):
    return document.ActiveView

def GetCurrentLevel(document):
    return document.ActiveView.GenLevel
