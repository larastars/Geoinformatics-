# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 13:37:51 2017

@author: larakamal
"""

#input docs
dataframe = pd.read_csv("labelled_queries/sea_ice.csv")

#get click score column
feature = dataframe.ix[:,1:2]
#make a list out of the column 
feature = feature['releaseDate_score'].tolist()
rank = [b[0] for b in sorted(enumerate(feature), key=lambda i:i[1], reverse = True)]

#sort docs
rows = dataframe.ix[:,0:11]
sorted_rows =[]
for i in range(len(rank)):
    sorted_rows.append(rows.values[rank[i]])

#save docs 
with open('results/release/sea_ice_sorted.csv', 'w', encoding = 'utf-8-sig') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(['term_score', 'releaseDate_score', 'versionNum_score', 'processingL_score', 'allPop_score','monthPop_score', 'userPop_score', 'spatialR_score','temporalR_score','click_score','label'])
    for i in sorted_rows:
        writer.writerow(i)