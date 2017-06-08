# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 13:22:42 2017

@author: larakamal
"""

from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import pandas as pd
import numpy as np
from math import log10
import csv 
     
#load model 
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")
#print("Loaded model from disk")

model.compile(optimizer='rmsprop',loss='binary_crossentropy', metrics=['accuracy'])
#print("Model compiled")              

dataframe = pd.read_csv("labelled_queries/quikscat.csv")
features = dataframe.ix[:,0:10]
features = scaler.transform(features)

rank = []
for i in range(len(features)):
    rank.append(i)
    
    
for i in range(1, len(features)):
        j = i-1
        temp = features[i]
        temp2 = rank[i]
        while(model.predict_classes((features[j] - temp).reshape(1,-1)) == 0 and (j >=0)):
            features[j+1] = features[j]
            rank[j+1] = rank[j]
            j = j - 1
            features[j+1] = temp
            rank[j+1] = temp2
            
            
rows = dataframe.ix[:,0:11]
sorted_rows =[]
for i in rank:
    sorted_rows.append(rows.values[i])


with open('results/enhanced/quikscat_sorted.csv', 'w', encoding = 'utf-8-sig') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(['term_score', 'releaseDate_score', 'versionNum_score', 'processingL_score', 'allPop_score','monthPop_score', 'userPop_score', 'spatialR_score','temporalR_score','click_score','label'])
    for i in sorted_rows:
        writer.writerow(i)
        
