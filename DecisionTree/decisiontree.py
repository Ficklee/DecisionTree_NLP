import re
import numpy as np
from math import log
from collections import Counter
def EntropyCalculator(Featurelst):
    result = {}
    for feature in Featurelst:
        if result.get(feature):
            result[feature]+=1
        else:
            result[feature]=1
    TCount = len(Featurelst)
    Entropy = 0.0
    problist = [float(FeatureTuple[1])/TCount for FeatureTuple in result.iteritems()]
    ent_sub = [-prob*log(prob,2) if prob!=0 else 0.0 for prob in problist]
    Entropy = sum(ent_sub)
    return Entropy

def ConditionalEntropyCalculator(XFeatureLst, ClassificationLst):
    XFeature = list(set(XFeatureLst))
    Xfeature_dict ={}
    NumCase = len(XFeatureLst)
    for i in xrange(NumCase):
        if Xfeature_dict.get(XFeatureLst[i]):
            Xfeature_dict[XFeatureLst[i]].append(ClassificationLst[i])
        else:
            Xfeature_dict[XFeatureLst[i]] = [ClassificationLst[i]]
    XFeatureClassLst = [xfeaturetuple[1] for xfeaturetuple in Xfeature_dict.iteritems()]
    Entropy = sum(map(lambda x:float(len(x))/NumCase*EntropyCalculator(x),XFeatureClassLst))
    return Entropy
def InformationGain(Feature,Classification):
    return EntropyCalculator(Classification)-ConditionalEntropyCalculator(Feature,Classification)
def Info_gainratio(FeatureLst,Classification):
    featureLst = list(set(FeatureLst))
    Numcase = len(Classification)
    feature_dict={}
    for feature in featureLst:
        if feature_dict.get(feature):
            feature_dict[feature]+=1
        else:
            feature_dict[feature]=1
    featureNumLst = [Ftuple[1] for Ftuple in feature_dict.iteritems()]
    EntropyLst = [0.0 if feature_c==0 else float(feature_c)/Numcase*log(float(feature_c)/Numcase,2) for feature_c in featureNumLst]
    Had= sum(EntropyLst)
    Had *= -1
    return InformationGain(FeatureLst,Classification)/Had

#a=[2,2,2,3]
#print EntropyCalculator(a)
#rint Info_gainratiol([1,1,1,1,1,2,2,2,2,2,3,3,3,3,3],[0,0,1,1,0,0,0,1,1,1,1,1,1,1,0])
'''
class treenode(object):
    def __init__(self,featureIndex=None,featureValue=None):
        self.featureIndex = featureIndex
        self.featureValue = featureValue
        self.succeeding=[]
        self.single =False
    def ID3FeatureSetup(self,featureList,categorylist):
        if featureList ==[]:
            self.featureIndex = -1
            Category = list(set(categorylist))
            featureCount = [(x,categorylist.count(x)) for x in Category]
            self.featureValue = max(featureCount,key=lambda x:x[1])[0]
            self.single= True
            return self
        if len(list(set(categorylist)))==1:
            self.single = True
            self.featureIndex = -1
            self.featureValue = list(set(categorylist))[0]
            return self
        caseNum = len(categorylist)
        info_gain_list = [InformationGain(x,categorylist) for x in featureList]
        TargetFeatureIndex = max(enumerate(info_gain_list),key=lambda x:x[1])[0]
        TargetFeatureVariant = list(set(featureList[TargetFeatureIndex]))
        for TargetFeatureValue in TargetFeatureVariant:
            CaseIndex = [x for x in xrange(caseNum) if featureList[TargetFeatureIndex][x]==TargetFeatureValue]
            CurrentFeatureList = []
            for feaInd in xrange(len(featureList)):
                if feaInd == TargetFeatureIndex:
                    CurrentFeatureList.append([])
                if feaInd !=TargetFeatureIndex:
                    CurrentFeatureList.append([featureList[feaInd][x] for x in xrange(caseNum)])
            CurrentCategoryList = [categorylist[x] for x in xrange(caseNum)]
            self.succeeding.append(treenode(TargetFeatureIndex,TargetFeatureValue))
'''
class Node(object):
    def __init__(self,fname=None,value=None):
        self.featurename=fname
        self.value = value
        self.succ = []

def DecisionTreeBuildUp(FeatureList_dict,Classification):
    TreeRoot = Node()
    if FeatureList_dict =={}:
            Category = list(set(Classification))
            featureCount = [(x,Classification.count(x)) for x in Category]
            TreeRoot.value = max(featureCount,key=lambda x:x[1])[0]
            return TreeRoot
    if len(list(set(Classification)))==1:
        TreeRoot.value = list(set(Classification))[0]
        return TreeRoot
    caseNum = len(Classification)
    infogainlist = [(x[0],InformationGain(x[1],Classification)) for x in FeatureList_dict.iteritems()]
    MaxFeature = max(infogainlist,key=lambda x:x[1])
    MaxFeatureName = MaxFeature[0]
    TargetFeatureValue = list(set(FeatureList_dict[MaxFeatureName]))
    print "use the feature " + MaxFeatureName
    for each_feature_value in TargetFeatureValue:
        target_index_list = [x for x in xrange(caseNum) if FeatureList_dict[MaxFeatureName][x]==each_feature_value]
        CurrentClassfication = [Classification[i] for i in target_index_list]
        CurrentFeatureList_dict = {}
        for pair in FeatureList_dict.iteritems():
            if pair[0]!=MaxFeatureName:
                CurrentFeatureList_dict[pair[0]] = [pair[1][i1] for i1 in target_index_list ]
        print CurrentFeatureList_dict
        print CurrentClassfication
        TreeRoot.succ.append(DecisionTreeBuildUp(CurrentFeatureList_dict,CurrentClassfication))
        TreeRoot.succ[-1].fname = MaxFeatureName
    return TreeRoot
a=DecisionTreeBuildUp({'age':[1,1,1,1,1,2,2,2,2,2,3,3,3,3,3],'job':[0,0,1,1,0,0,0,1,0,0,0,0,1,1,0]},[0,0,1,1,0,0,0,1,1,1,1,1,1,1,0])
print len(a.succ)
print len(a.succ[0].succ)