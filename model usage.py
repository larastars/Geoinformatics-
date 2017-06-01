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
# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

model.compile(optimizer='rmsprop',loss='binary_crossentropy', metrics=['accuracy'])
print("Model compiled")              

dataframe = pd.read_csv("labelled_queries/sea_ice.csv")
features = dataframe.ix[:,0:10]

#scale relatively to standarize to have mean of 0 and std dev of 1  
features = scaler.transform(features)

pair_list = []
#find the difference of every pair and append the difference to pair_list list
for i in range(len(features)):
    for j in range(len(features)):
        final = features[i] - features[j]
        pair_list.append(final.reshape(1,-1))
  
#initialize rank list with zeros 
rank = []
for i in range(len(features)):
    rank.append(0)

 
index = 0
var = 0
for i in range(len(pair_list)):      
    if (var == int(math.sqrt(len(pair_list)))-1):
        index = index+1
        var = 0
    else:
        #prediction = model.predict(pair_list[i])
        class_prediction = model.predict_classes(pair_list[i])
        rank[index] = rank[index] +  class_prediction
        var = var + 1


#sort the list and the index accordingly 
#list that has the sorted documents 
rank_doc_list = [b[0] for b in sorted(enumerate(rank), key=lambda i:i[1], reverse = True)]
rows = dataframe.ix[:,0:11]

#create sorted rows list
sorted_rows =[]
#sort rows 
for i in range(len(rank_doc_list)):
    sorted_rows.append(rows.values[rank_doc_list[i]])
    

with open('results/sea_ice_sorted.csv', 'w', encoding = 'utf-8-sig') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(['term_score', 'releaseDate_score', 'versionNum_score', 'processingL_score', 'allPop_score','monthPop_score', 'userPop_score', 'spatialR_score','temporalR_score','click_score','label'])
    for i in sorted_rows:
        writer.writerow(i)
        
#np.savetxt("results/ocean_pressure_sorted.csv", sorted_rows, delimiter=",", fmt='%s')