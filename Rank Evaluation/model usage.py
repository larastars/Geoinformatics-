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
import math 
import csv 


#load model 
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

model.compile(optimizer='rmsprop',loss='binary_crossentropy', metrics=['accuracy'])
print("Model compiled")              

dataframe = pd.read_csv("labelled_queries/gravity.csv")
features = dataframe.ix[:,0:10]
features = scaler.transform(features)



rank = []  
for i in range(len(features)):
    rank.append(0)
    print(i)

index = 0   
var = 0
for i in range(len(features)):
    for j in range(len(features)):
        if(var == len(features)-1):
            var = 0
            index += 1
        else:
            class_prediction = model.predict_classes((features[i] - features[j]).reshape(1,-1))
            rank[index] = rank[index] +  class_prediction
            var += 1
            
    
#sort list
rank_doc_list = [b[0] for b in sorted(enumerate(rank), key=lambda i:i[1], reverse = True)]
rows = dataframe.ix[:,0:11]

sorted_rows =[]
for i in range(len(rank_doc_list)):
    sorted_rows.append(rows.values[rank_doc_list[i]])
    

with open('gravity_new.csv', 'w', encoding = 'utf-8-sig') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(['term_score', 'releaseDate_score', 'versionNum_score', 'processingL_score', 'allPop_score','monthPop_score', 'userPop_score', 'spatialR_score','temporalR_score','click_score','label'])
    for i in sorted_rows:
        writer.writerow(i)
        
