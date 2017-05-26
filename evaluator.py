# -*- coding: utf-8 -*-
"""
@author: larakamal
"""

import pandas as pd
import numpy as np
from math import log10

def getNDCG(list, k):
    #convert to double 
   dcg = float(getDCG(list,k))
   idcg = float(getIDCG(list,k))
   ndcg = 0.0
   if (idcg > 0.0):
       ndcg = dcg/idcg
   return ndcg 


def getPrecision(list, k):
    size = len(list)
    if (size == 0 or k == 0):
        return 0.0
        
    if(k > size):
        k = size
    rel_doc_num = getRelevantDocNum(list,k)
    #convert to double 
    precision = float(float(rel_doc_num)/float(k))
    return precision 

      
def getRelevantDocNum(list,k):
    size = len(list)
    if (size == 0 or k == 0):
        return 0
    if (k > size):
        k = size
    rel_num = 0
    for i in range(k):
       if list[i] > 3:
           rel_num = rel_num + 1
    return rel_num 


def getDCG(list,k):
    size = len(list)
    if (size == 0 or k == 0):
        return 0.0
    if (k > size):
        k = size
    #convert to double
    dcg = list[0]
    dcg = float(dcg)

    for i in range(1,k):
        rel = list[i]
        pos = i+1
        rel_log = log10(pos)/log10(2)
        rel_log = float(rel_log)
        dcg = dcg + (rel/rel_log)
    return dcg 


def getIDCG(list, k):
    # sort list
    sortedList = list
    sortedList = sorted(sortedList, key=int, reverse=True)
    idcg = getDCG(sortedList, k)
    return float(idcg) 

    
dataframe = pd.read_csv("labelled_queries/sea_ice.csv")
label = dataframe.ix[:,10:11]


temp_list = label['label'].tolist()
     
#print(score_list[0])
label_list = [];

for i in range(len(temp_list)):
   # print(score_list[i])
    if temp_list[i] == 'Excellent':
        label_list.append(7) 
    elif temp_list[i] == 'Very good':
        label_list.append(6) 
    elif temp_list[i] == 'Good':
        label_list.append(5) 
    elif temp_list[i] == 'Ok':
        label_list.append(4) 
    elif temp_list[i] == 'Bad':
        label_list.append(3) 
    elif temp_list[i] == 'Very bad':
        label_list.append(2) 
    elif temp_list[i] == 'Terrible':
        label_list.append(1) 
    else:
        label_list.append(0)
        
for i in range(40):
    k = i
    NDCG_label = getNDCG(label_list,k)
    precision_label = getPrecision(label_list,k)
    print(NDCG_label)
    print(precision_label)
    
    