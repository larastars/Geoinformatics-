# -*- coding: utf-8 -*-
"""
Created on Tue May 30 13:13:44 2017

@author: larakamal
"""
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import pandas as pd
import numpy as np
from math import log10
import math
import csv 

 
#load model 
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
#load weights into new model
loaded_model.load_weights("model.h5")
#print("Loaded model from disk")

model.compile(optimizer='rmsprop',loss='binary_crossentropy', metrics=['accuracy'])
#print("Model compiled")              

dataframe1 = pd.read_csv("labelled_queries/gravity.csv")
dataframe2 = pd.read_csv("labelled_queries/ocean_pressure.csv")
dataframe3 = pd.read_csv("labelled_queries/ocean_temperature.csv")
dataframe4 = pd.read_csv("labelled_queries/ocean_wind.csv")
dataframe5 = pd.read_csv("labelled_queries/pathfinder.csv")
dataframe6 = pd.read_csv("labelled_queries/quikscat.csv")
dataframe7 = pd.read_csv("labelled_queries/radar.csv")
dataframe8 = pd.read_csv("labelled_queries/saline_density.csv")
dataframe9 = pd.read_csv("labelled_queries/sea_ice.csv")

features1 = dataframe1.ix[:,0:10]
features2 = dataframe2.ix[:,0:10]
features3 = dataframe3.ix[:,0:10]
features4 = dataframe4.ix[:,0:10]
features5 = dataframe5.ix[:,0:10]
features6 = dataframe6.ix[:,0:10]
features7 = dataframe7.ix[:,0:10]
features8 = dataframe8.ix[:,0:10]
features9 = dataframe9.ix[:,0:10]

#scale relatively to standarize to have mean of 0 and std dev of 1  
features1 = scaler.transform(features1)
features2 = scaler.transform(features2)
features3 = scaler.transform(features3)
features4 = scaler.transform(features4)
features5 = scaler.transform(features5)
features6 = scaler.transform(features6)
features7 = scaler.transform(features7)
features8 = scaler.transform(features8)
features9 = scaler.transform(features9)


pair_list1 = []
pair_list2 = []
pair_list3 = []
pair_list4 = []
pair_list5 = []
pair_list6 = []
pair_list7 = []
pair_list8 = []
pair_list9 = []

#find the difference of every pair and append the difference to pair_list list
for i in range(len(features1)):
    for j in range(len(features1)):
        final = features1[i] - features1[j]
        pair_list1.append(final.reshape(1,-1))

for i in range(len(features2)):
    for j in range(len(features2)):
        final = features2[i] - features2[j]
        pair_list2.append(final.reshape(1,-1))

for i in range(len(features3)):
    for j in range(len(features3)):
        final = features3[i] - features3[j]
        pair_list3.append(final.reshape(1,-1))
        
for i in range(len(features4)):
    for j in range(len(features4)):
        final = features4[i] - features4[j]
        pair_list4.append(final.reshape(1,-1))
        
for i in range(len(features5)):
    for j in range(len(features5)):
        final = features5[i] - features5[j]
        pair_list5.append(final.reshape(1,-1))
        
for i in range(len(features6)):
    for j in range(len(features6)):
        final = features6[i] - features6[j]
        pair_list6.append(final.reshape(1,-1))
        
for i in range(len(features7)):
    for j in range(len(features7)):
        final = features7[i] - features7[j]
        pair_list7.append(final.reshape(1,-1))
        
for i in range(len(features8)):
    for j in range(len(features8)):
        final = features8[i] - features8[j]
        pair_list8.append(final.reshape(1,-1))
        
for i in range(len(features9)):
    for j in range(len(features9)):
        final = features9[i] - features9[j]
        pair_list9.append(final.reshape(1,-1))
        
#initialize rank list with zeros 
rank1 = []
rank2 = []
rank3 = []
rank4 = []
rank5 = []
rank6 = []
rank7 = []
rank8 = []
rank9 = []

for i in range(len(features1)):
    rank1.append(0)

for i in range(len(features2)):
    rank2.append(0)
    
for i in range(len(features3)):
    rank3.append(0)
    
for i in range(len(features4)):
    rank4.append(0)

for i in range(len(features5)):
    rank5.append(0)

for i in range(len(features6)):
    rank6.append(0)
    
for i in range(len(features7)):
    rank7.append(0)
    
for i in range(len(features8)):
    rank8.append(0)
    
for i in range(len(features9)):
    rank9.append(0)
 
index = 0
var = 0
for i in range(len(pair_list1)):      
    if (var == int(math.sqrt(len(pair_list1)))-1):
        index = index+1
        var = 0
    else:
        #prediction = model.predict(pair_list[i])
        class_prediction = model.predict_classes(pair_list1[i])
        rank1[index] = rank1[index] +  class_prediction
        var = var + 1

index = 0
var = 0
for i in range(len(pair_list2)):      
    if (var == int(math.sqrt(len(pair_list2)))-1):
        index = index+1
        var = 0
    else:
        #prediction = model.predict(pair_list[i])
        class_prediction = model.predict_classes(pair_list2[i])
        rank2[index] = rank2[index] +  class_prediction
        var = var + 1

index = 0
var = 0
for i in range(len(pair_list3)):      
    if (var == int(math.sqrt(len(pair_list3)))-1):
        index = index+1
        var = 0
    else:
        #prediction = model.predict(pair_list[i])
        class_prediction = model.predict_classes(pair_list3[i])
        rank3[index] = rank3[index] +  class_prediction
        var = var + 1
        
index = 0
var = 0
for i in range(len(pair_list4)):      
    if (var == int(math.sqrt(len(pair_list4)))-1):
        index = index+1
        var = 0
    else:
        #prediction = model.predict(pair_list[i])
        class_prediction = model.predict_classes(pair_list4[i])
        rank4[index] = rank4[index] +  class_prediction
        var = var + 1
        
index = 0
var = 0
for i in range(len(pair_list5)):      
    if (var == int(math.sqrt(len(pair_list5)))-1):
        index = index+1
        var = 0
    else:
        #prediction = model.predict(pair_list[i])
        class_prediction = model.predict_classes(pair_list5[i])
        rank5[index] = rank5[index] +  class_prediction
        var = var + 1

index = 0
var = 0
for i in range(len(pair_list6)):      
    if (var == int(math.sqrt(len(pair_list6)))-1):
        index = index+1
        var = 0
    else:
        #prediction = model.predict(pair_list[i])
        class_prediction = model.predict_classes(pair_list6[i])
        rank6[index] = rank6[index] +  class_prediction
        var = var + 1       

index = 0
var = 0
for i in range(len(pair_list7)):      
    if (var == int(math.sqrt(len(pair_list7)))-1):
        index = index+1
        var = 0
    else:
        #prediction = model.predict(pair_list[i])
        class_prediction = model.predict_classes(pair_list7[i])
        rank7[index] = rank7[index] +  class_prediction
        var = var + 1  
        
index = 0
var = 0
for i in range(len(pair_list8)):      
    if (var == int(math.sqrt(len(pair_list8)))-1):
        index = index+1
        var = 0
    else:
        #prediction = model.predict(pair_list[i])
        class_prediction = model.predict_classes(pair_list8[i])
        rank8[index] = rank8[index] +  class_prediction
        var = var + 1
        
index = 0
var = 0
for i in range(len(pair_list9)):      
    if (var == int(math.sqrt(len(pair_list9)))-1):
        index = index+1
        var = 0
    else:
        #prediction = model.predict(pair_list[i])
        class_prediction = model.predict_classes(pair_list9[i])
        rank9[index] = rank9[index] +  class_prediction
        var = var + 1
        
        
#sort the list and the index accordingly 
#list that has the sorted documents 
rank_doc_list1 = [b[0] for b in sorted(enumerate(rank1), key=lambda i:i[1], reverse = True)]
rank_doc_list2 = [b[0] for b in sorted(enumerate(rank2), key=lambda i:i[1], reverse = True)]
rank_doc_list3 = [b[0] for b in sorted(enumerate(rank3), key=lambda i:i[1], reverse = True)]
rank_doc_list4 = [b[0] for b in sorted(enumerate(rank4), key=lambda i:i[1], reverse = True)]
rank_doc_list5 = [b[0] for b in sorted(enumerate(rank5), key=lambda i:i[1], reverse = True)]
rank_doc_list6 = [b[0] for b in sorted(enumerate(rank6), key=lambda i:i[1], reverse = True)]
rank_doc_list7 = [b[0] for b in sorted(enumerate(rank7), key=lambda i:i[1], reverse = True)]
rank_doc_list8 = [b[0] for b in sorted(enumerate(rank8), key=lambda i:i[1], reverse = True)]
rank_doc_list9 = [b[0] for b in sorted(enumerate(rank9), key=lambda i:i[1], reverse = True)]

rows1 = dataframe1.ix[:,0:11]
rows2 = dataframe2.ix[:,0:11]
rows3 = dataframe3.ix[:,0:11]
rows4 = dataframe4.ix[:,0:11]
rows5 = dataframe5.ix[:,0:11]
rows6 = dataframe6.ix[:,0:11]
rows7 = dataframe7.ix[:,0:11]
rows8 = dataframe8.ix[:,0:11]
rows9 = dataframe9.ix[:,0:11]


#create sorted rows list
sorted_rows1 =[]
sorted_rows2 =[]
sorted_rows3 =[]
sorted_rows4 =[]
sorted_rows5 =[]
sorted_rows6 =[]
sorted_rows7 =[]
sorted_rows8 =[]
sorted_rows9 =[]

#sort rows 
for i in range(len(rank_doc_list1)):
    sorted_rows1.append(rows1.values[rank_doc_list1[i]])

for i in range(len(rank_doc_list2)):
    sorted_rows2.append(rows2.values[rank_doc_list2[i]])
    
for i in range(len(rank_doc_list3)):
    sorted_rows3.append(rows3.values[rank_doc_list3[i]])
    
for i in range(len(rank_doc_list4)):
    sorted_rows4.append(rows4.values[rank_doc_list4[i]])
    
for i in range(len(rank_doc_list5)):
    sorted_rows5.append(rows5.values[rank_doc_list5[i]])
    
for i in range(len(rank_doc_list6)):
    sorted_rows6.append(rows6.values[rank_doc_list6[i]])
    
for i in range(len(rank_doc_list7)):
    sorted_rows7.append(rows7.values[rank_doc_list7[i]])
    
for i in range(len(rank_doc_list8)):
    sorted_rows8.append(rows8.values[rank_doc_list8[i]])
    
for i in range(len(rank_doc_list9)):
    sorted_rows9.append(rows9.values[rank_doc_list9[i]])
    
    

with open('results/test/gravity_sorted.csv', 'w', encoding = 'utf-8-sig') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(['term_score', 'releaseDate_score', 'versionNum_score', 'processingL_score', 'allPop_score','monthPop_score', 'userPop_score', 'spatialR_score','temporalR_score','click_score','label'])
    for i in sorted_rows1:
        writer.writerow(i)
        
with open('results/test/ocean_pressure_sorted.csv', 'w', encoding = 'utf-8-sig') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(['term_score', 'releaseDate_score', 'versionNum_score', 'processingL_score', 'allPop_score','monthPop_score', 'userPop_score', 'spatialR_score','temporalR_score','click_score','label'])
    for i in sorted_rows2:
        writer.writerow(i)
        
with open('results/test/ocean_temperature_sorted.csv', 'w', encoding = 'utf-8-sig') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(['term_score', 'releaseDate_score', 'versionNum_score', 'processingL_score', 'allPop_score','monthPop_score', 'userPop_score', 'spatialR_score','temporalR_score','click_score','label'])
    for i in sorted_rows3:
        writer.writerow(i)
        
with open('results/test/ocean_wind_sorted.csv', 'w', encoding = 'utf-8-sig') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(['term_score', 'releaseDate_score', 'versionNum_score', 'processingL_score', 'allPop_score','monthPop_score', 'userPop_score', 'spatialR_score','temporalR_score','click_score','label'])
    for i in sorted_rows4:
        writer.writerow(i)
 
with open('results/test/pathfinder_sorted.csv', 'w', encoding = 'utf-8-sig') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(['term_score', 'releaseDate_score', 'versionNum_score', 'processingL_score', 'allPop_score','monthPop_score', 'userPop_score', 'spatialR_score','temporalR_score','click_score','label'])
    for i in sorted_rows5:
        writer.writerow(i)
        
with open('results/test/quikscat_sorted.csv', 'w', encoding = 'utf-8-sig') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(['term_score', 'releaseDate_score', 'versionNum_score', 'processingL_score', 'allPop_score','monthPop_score', 'userPop_score', 'spatialR_score','temporalR_score','click_score','label'])
    for i in sorted_rows6:
        writer.writerow(i)
        
with open('results/test/radar_sorted.csv', 'w', encoding = 'utf-8-sig') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(['term_score', 'releaseDate_score', 'versionNum_score', 'processingL_score', 'allPop_score','monthPop_score', 'userPop_score', 'spatialR_score','temporalR_score','click_score','label'])
    for i in sorted_rows7:
        writer.writerow(i)

with open('results/test/saline_density_sorted.csv', 'w', encoding = 'utf-8-sig') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(['term_score', 'releaseDate_score', 'versionNum_score', 'processingL_score', 'allPop_score','monthPop_score', 'userPop_score', 'spatialR_score','temporalR_score','click_score','label'])
    for i in sorted_rows8:
        writer.writerow(i)

with open('results/test/sea_ice_sorted.csv', 'w', encoding = 'utf-8-sig') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(['term_score', 'releaseDate_score', 'versionNum_score', 'processingL_score', 'allPop_score','monthPop_score', 'userPop_score', 'spatialR_score','temporalR_score','click_score','label'])
    for i in sorted_rows9:
        writer.writerow(i)
        
##################################### EVALUATE ##########################################

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

    
dataframe1 = pd.read_csv("results/test/gravity_sorted.csv")
dataframe2 = pd.read_csv("results/test/ocean_pressure_sorted.csv")
dataframe3 = pd.read_csv("results/test/ocean_temperature_sorted.csv")
dataframe4 = pd.read_csv("results/test/ocean_wind_sorted.csv")
dataframe5 = pd.read_csv("results/test/pathfinder_sorted.csv")
dataframe6 = pd.read_csv("results/test/quikscat_sorted.csv")
dataframe7 = pd.read_csv("results/test/radar_sorted.csv")
dataframe8 = pd.read_csv("results/test/saline_density_sorted.csv")
dataframe9 = pd.read_csv("results/test/sea_ice_sorted.csv")


label1 = dataframe1.ix[:,10:11]
label2 = dataframe2.ix[:,10:11]
label3 = dataframe3.ix[:,10:11]
label4 = dataframe4.ix[:,10:11]
label5 = dataframe5.ix[:,10:11]
label6 = dataframe6.ix[:,10:11]
label7 = dataframe7.ix[:,10:11]
label8 = dataframe8.ix[:,10:11]
label9 = dataframe9.ix[:,10:11]

temp_list1 = label1['label'].tolist()
temp_list2 = label2['label'].tolist()
temp_list3 = label3['label'].tolist()
temp_list4 = label4['label'].tolist()
temp_list5 = label5['label'].tolist()
temp_list6 = label6['label'].tolist()
temp_list7 = label7['label'].tolist()
temp_list8 = label8['label'].tolist()
temp_list9 = label9['label'].tolist()

label_list1 = [];
label_list2 = [];
label_list3 = [];
label_list4 = [];
label_list5 = [];
label_list6 = [];
label_list7 = [];
label_list8 = [];
label_list9 = [];


for i in range(len(temp_list1)):
    if temp_list1[i] == 'Excellent':
        label_list1.append(7) 
    elif temp_list1[i] == 'Very good':
        label_list1.append(6) 
    elif temp_list1[i] == 'Good':
        label_list1.append(5) 
    elif temp_list1[i] == 'Ok':
        label_list1.append(4) 
    elif temp_list1[i] == 'Bad':
        label_list1.append(3) 
    elif temp_list1[i] == 'Very bad':
        label_list1.append(2) 
    elif temp_list1[i] == 'Terrible':
        label_list1.append(1) 
    else:
        label_list1.append(0)
        
for i in range(len(temp_list2)):
    if temp_list2[i] == 'Excellent':
        label_list2.append(7) 
    elif temp_list2[i] == 'Very good':
        label_list2.append(6) 
    elif temp_list2[i] == 'Good':
        label_list2.append(5) 
    elif temp_list2[i] == 'Ok':
        label_list2.append(4) 
    elif temp_list2[i] == 'Bad':
        label_list2.append(3) 
    elif temp_list2[i] == 'Very bad':
        label_list2.append(2) 
    elif temp_list2[i] == 'Terrible':
        label_list2.append(1) 
    else:
        label_list2.append(0)

for i in range(len(temp_list3)):
    if temp_list3[i] == 'Excellent':
        label_list3.append(7) 
    elif temp_list3[i] == 'Very good':
        label_list3.append(6) 
    elif temp_list3[i] == 'Good':
        label_list3.append(5) 
    elif temp_list3[i] == 'Ok':
        label_list3.append(4) 
    elif temp_list3[i] == 'Bad':
        label_list3.append(3) 
    elif temp_list3[i] == 'Very bad':
        label_list3.append(2) 
    elif temp_list3[i] == 'Terrible':
        label_list3.append(1) 
    else:
        label_list3.append(0)
        
        
for i in range(len(temp_list4)):
    if temp_list4[i] == 'Excellent':
        label_list4.append(7) 
    elif temp_list4[i] == 'Very good':
        label_list4.append(6) 
    elif temp_list4[i] == 'Good':
        label_list4.append(5) 
    elif temp_list4[i] == 'Ok':
        label_list4.append(4) 
    elif temp_list4[i] == 'Bad':
        label_list4.append(3) 
    elif temp_list4[i] == 'Very bad':
        label_list4.append(2) 
    elif temp_list4[i] == 'Terrible':
        label_list4.append(1) 
    else:
        label_list4.append(0)
        
for i in range(len(temp_list5)):
    if temp_list5[i] == 'Excellent':
        label_list5.append(7) 
    elif temp_list5[i] == 'Very good':
        label_list5.append(6) 
    elif temp_list5[i] == 'Good':
        label_list5.append(5) 
    elif temp_list5[i] == 'Ok':
        label_list5.append(4) 
    elif temp_list5[i] == 'Bad':
        label_list5.append(3) 
    elif temp_list5[i] == 'Very bad':
        label_list5.append(2) 
    elif temp_list5[i] == 'Terrible':
        label_list5.append(1) 
    else:
        label_list5.append(0)
        
        
for i in range(len(temp_list6)):
    if temp_list6[i] == 'Excellent':
        label_list6.append(7) 
    elif temp_list6[i] == 'Very good':
        label_list6.append(6) 
    elif temp_list6[i] == 'Good':
        label_list6.append(5) 
    elif temp_list6[i] == 'Ok':
        label_list6.append(4) 
    elif temp_list6[i] == 'Bad':
        label_list6.append(3) 
    elif temp_list6[i] == 'Very bad':
        label_list6.append(2) 
    elif temp_list6[i] == 'Terrible':
        label_list6.append(1) 
    else:
        label_list6.append(0)
        
for i in range(len(temp_list7)):
    if temp_list7[i] == 'Excellent':
        label_list7.append(7) 
    elif temp_list7[i] == 'Very good':
        label_list7.append(6) 
    elif temp_list7[i] == 'Good':
        label_list7.append(5) 
    elif temp_list7[i] == 'Ok':
        label_list7.append(4) 
    elif temp_list7[i] == 'Bad':
        label_list7.append(3) 
    elif temp_list7[i] == 'Very bad':
        label_list7.append(2) 
    elif temp_list7[i] == 'Terrible':
        label_list7.append(1) 
    else:
        label_list7.append(0)
        
for i in range(len(temp_list8)):
    if temp_list8[i] == 'Excellent':
        label_list8.append(7) 
    elif temp_list8[i] == 'Very good':
        label_list8.append(6) 
    elif temp_list8[i] == 'Good':
        label_list8.append(5) 
    elif temp_list8[i] == 'Ok':
        label_list8.append(4) 
    elif temp_list8[i] == 'Bad':
        label_list8.append(3) 
    elif temp_list8[i] == 'Very bad':
        label_list8.append(2) 
    elif temp_list8[i] == 'Terrible':
        label_list8.append(1) 
    else:
        label_list8.append(0)
        
for i in range(len(temp_list9)):
    if temp_list9[i] == 'Excellent':
        label_list9.append(7) 
    elif temp_list9[i] == 'Very good':
        label_list9.append(6) 
    elif temp_list9[i] == 'Good':
        label_list9.append(5) 
    elif temp_list9[i] == 'Ok':
        label_list9.append(4) 
    elif temp_list9[i] == 'Bad':
        label_list9.append(3) 
    elif temp_list9[i] == 'Very bad':
        label_list9.append(2) 
    elif temp_list9[i] == 'Terrible':
        label_list9.append(1) 
    else:
        label_list9.append(0)

NDCG_list1 = [] 
NDCG_list2 = []   
NDCG_list3 = []
NDCG_list4 = []   
NDCG_list5 = []   
NDCG_list6 = []   
NDCG_list7 = []   
NDCG_list8 = []   
NDCG_list9 = []   
       
for i in range(1,41):
    k = i
    NDCG_list1.append(getNDCG(label_list1,k))
    NDCG_list2.append(getNDCG(label_list2,k))
    NDCG_list3.append(getNDCG(label_list3,k))
    NDCG_list4.append(getNDCG(label_list4,k))
    NDCG_list5.append(getNDCG(label_list5,k))
    NDCG_list6.append(getNDCG(label_list6,k))
    NDCG_list7.append(getNDCG(label_list7,k))
    NDCG_list8.append(getNDCG(label_list8,k))
    NDCG_list9.append(getNDCG(label_list9,k))
    
    
precision_list1 = []
precision_list2 = []
precision_list3 = []
precision_list4 = []
precision_list5 = []
precision_list6 = []
precision_list7 = []
precision_list8 = []
precision_list9 = []


for i in range(1,41):
    k = i
    precision_list1.append(getPrecision(label_list1,k))
    precision_list2.append(getPrecision(label_list2,k))
    precision_list3.append(getPrecision(label_list3,k))
    precision_list4.append(getPrecision(label_list4,k))
    precision_list5.append(getPrecision(label_list5,k))
    precision_list6.append(getPrecision(label_list6,k))
    precision_list7.append(getPrecision(label_list7,k))
    precision_list8.append(getPrecision(label_list8,k))
    precision_list9.append(getPrecision(label_list9,k))
    
    
    
total_list_NDCG = []
for i in range(len(NDCG_list1)):
    average = (NDCG_list1[i] + NDCG_list2[i]+ NDCG_list3[i] + NDCG_list4[i]+ NDCG_list5[i] + NDCG_list6[i] + NDCG_list7[i] + NDCG_list8[i] + NDCG_list9[i])/9
    array = np.array([NDCG_list1[i],NDCG_list2[i], NDCG_list3[i], NDCG_list4[i], NDCG_list5[i], NDCG_list6[i], NDCG_list7[i], NDCG_list8[i], NDCG_list9[i], average])
    total_list_NDCG.append(array)

total_list_precision = []
for i in range(len(precision_list1)):
    average = (precision_list1[i] + precision_list2[i]+ precision_list3[i] + precision_list4[i]+ precision_list5[i] + precision_list6[i] + precision_list7[i] + precision_list8[i] + precision_list9[i])/9
    array = np.array([precision_list1[i],precision_list2[i], precision_list3[i], precision_list4[i], precision_list5[i], precision_list6[i], precision_list7[i], precision_list8[i], precision_list9[i], average])
    total_list_precision.append(array)
   
with open('results/test/NDCG_graph.csv', 'w', encoding = 'utf-8-sig') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(['label'])
    writer.writerow(['gravity', 'ocean_pressure', 'ocean_temperature', 'ocean_wind', 'pathfinder','quikscat', 'radar', 'saline_density','sea_ice', 'RankSVM'])
    for i in total_list_NDCG:
        writer.writerow(i)
        
with open('results/test/precision_graph.csv', 'w', encoding = 'utf-8-sig') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(['label'])
    writer.writerow(['gravity', 'ocean_pressure', 'ocean_temperature', 'ocean_wind', 'pathfinder','quikscat', 'radar', 'saline_density','sea_ice', 'RankSVM'])
    for i in total_list_precision:
        writer.writerow(i) 
