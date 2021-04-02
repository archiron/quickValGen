#! /usr/bin/env python
#-*-coding: utf-8 -*-

# A new presentation/use is made in order to use very precisely the DataSets.
# You can add a DataSet inside a given function and look what happened for only the considered Datatsets.
# This seems more efficient than use "hard coding" and complex search function for the separate cases.

# new way to load datasets items into the menu. datasets are presented as [name, True/False] with True/False the default choice to be checked or not.

def DataLocation(self):
    '''
    WARNING : if you add/remove a line for a path
    DO NOT FORGET to update the pathToURL() function below.
    '''
    table=[
    ["Remote eos dev", 1, '/eos/project/c/cmsweb/www/egamma/validation/Electrons/Dev/', 'dev'],
    ["Remote eos std", 0, '/eos/project/c/cmsweb/www/egamma/validation/Electrons/Releases/', 'std'],
    ]
    return table

def DataSetsFilter(self, fieldname):
    import sys
    #fieldname = 'FullvsFull' # default
    #fieldname = fieldname + 'RECO'
    table=getattr(sys.modules[__name__], fieldname)(self)

    return table

def DataSetsFilter_FullvsFullRECO(self):
    table=[
    ["SingleElectronPt10", 0], # 1 : displayed
    ["SingleElectronPt10_UP15", 0],
    ["SingleElectronPt35", 0],
    ["SingleElectronPt35_UP15", 0], # 0 : not displayed
    ["SingleElectronPt1000", 0],
    ["SingleEFlatPt2To100", 1],
    ["QCD_Pt_80_120_13", 0],
    ["TTbar_13", 0],
    ["ZEE_13", 0],
    ["TTbar_14TeV", 1],
    ["ZEE_14", 1],
    ]
    return table

def DataSetsFilter_FastvsFastRECO(self):
    table=[
    ["TTbar_13", 1],
    ["ZEE_13", 1],
    ["TTbar_13_UP17", 1],
    ["ZEE_13_UP17", 1],
    ["TTbar_13_UP18", 1],
    ["ZEE_13_UP18", 1],
    ]
    return table

def DataSetsFilter_FastvsFullRECO(self):
    table=[
    ["TTbar_13", 1],
    ["ZEE_13", 1],
    ["TTbar_13_UP17", 1],
    ["ZEE_13_UP17", 1],
    ["TTbar_13_UP18", 1],
    ["ZEE_13_UP18", 1],
    ]
    return table

def DataSetsFilter_FullvsFullPU(self):
    table=[
    ["TTbar_13", 0],
    ["ZEE_13", 0],
    ["TTbar_14TeV", 1],
    ["ZEE_14", 1],
    ]
    return table

def DataSetsFilter_FastvsFastPU(self):
    table=[
    ["TTbar_13", 1],
    ["ZEE_13", 1],
    ]
    return table

def DataSetsFilter_FastvsFullPU(self):
    table=[
    ["TTbar_13", 1],
    ["ZEE_13", 1],
    ]
    return table

def DataSetsFilter_FullvsFullpmx(self):
    table=[
    ["TTbar_13", 1],
    ["ZEE_13", 1],
    ]
    return table

def DataSetsFilter_FastvsFastpmx(self):
    table=[
    ["TTbar_13", 1],
    ["ZEE_13", 1],
    ]
    return table

def DataSetsFilter_FastvsFullpmx(self):
    table=[
    ["TTbar_13", 1],
    ["ZEE_13", 1],
    ]
    return table

def DataSetsFilter_FullvsFullminiAOD(self):
    table=[
    ["SingleElectronPt10", 0],
    ["SingleEFlatPt2To100", 1],
    ["TTbar_13", 0],
    ["ZEE_13", 0],
    ["TTbar_14TeV", 1],
    ["ZEE_14", 1],
    ]
    return table

def DataSetsFilter_FastvsFastminiAOD(self):
    table=[
    ["TTbar_13", 1],
    ["ZEE_13", 1],
    ]
    return table

def DataSetsFilter_FastvsFullminiAOD(self):
    table=[
    ["TTbar_13", 1],
    ["ZEE_13", 1],
    ]
    return table
