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




        
