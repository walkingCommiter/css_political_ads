#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 14:52:31 2019

@author: nadabeili
"""

#import the librairies
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#importing the dataset
dataset= pd.read_excel('Cleaning_data.xlsx')
data= dataset.iloc [:,:].values

#splitting the dataset into two
from sklearn.cross_validation import  train_test_split
x_Part1 ,x_Part2 = train_test_split(data,test_size=0.05,random_state=0)
df = pd.DataFrame(x_Part2)
Dataset_to_be_labelled = open("Dataset_to_be_labelled.csv", "w+")
df.columns = list(dataset.columns.values)
df.to_csv(Dataset_to_be_labelled, encoding='utf-8', index=False)

#################################
####################CTR or Click Through Rate in internet marketing = Clicks / Impressions * 100
dataset["CTR"] = ""
for index, row in dataset.iterrows():
    if row['AD_CLICKS']==0 or row['AD_IMPRESSIONS']==0:
        dataset.set_value(index,'CTR',0)
    else:
       ctr= row['AD_CLICKS']/row['AD_IMPRESSIONS']*100
       dataset.set_value(index,'CTR',ctr)

#######################################        
for index, row in dataset.iterrows(): 
    spend_list= str(row['AD_SPEND'])
    spend_list = spend_list.split()
    del(spend_list[-1])   
    dataset.set_value(index,'AD_SPEND',spend_list)
    if not spend_list :
        dataset.set_value(index,'AD_SPEND',0)
    else:
        dataset.set_value(index,'AD_SPEND',float(spend_list[0]))
        
       
       
##############################       
plt.figure(figsize=(20,10))
plt.xlabel('AD_ID')
plt.ylabel('CTR')
plt.plot(dataset['AD_ID'], dataset['CTR'], 'ro')
plt.axis([0, 3517, 0,100 ])
plt.show()

#########################3
plt.figure(figsize=(20,80))
plt.xlabel('AD_ID')
plt.ylabel('AD_SPEND')
plt.plot(dataset['AD_ID'], dataset['AD_SPEND'], 'ro')
plt.axis([0, 3600, 0,(dataset['AD_SPEND'].max()+100) ])
plt.yticks(np.arange(0,dataset['AD_SPEND'].max(),2000))

plt.show()

################################
plt.figure(figsize=(20,80))
plt.xlabel('CTR')
plt.ylabel('AD_SPEND')
plt.plot(dataset['CTR'], dataset['AD_SPEND'], '*')
plt.axis([0, 101, 0,dataset['AD_SPEND'].max() ])
plt.yticks(np.arange(0,dataset['AD_SPEND'].max(),5000))
plt.xticks(np.arange(0,dataset['CTR'].max(),5))

plt.show()

################################
plt.figure(figsize=(20,20))
plt.xlabel('CTR')
plt.ylabel('AD_TARGETING_AGE')
plt.plot(dataset['CTR'], dataset['AD_TARGETING_AGE'], '*')
plt.axis([0, 101, 0,dataset['AD_TARGETING_AGE'].max() ])
#plt.yticks(np.arange(0,dataset['AD_SPEND'].max(),5000))
plt.xticks(np.arange(0,100,5))

plt.show()
####################################
##import numpy as np
from scipy.stats import kurtosis, skew

##x = np.random.normal(0, 2, 10000)   # create random values based on a normal distribution

print( 'excess kurtosis of normal distribution (should be 0): {}'.format( kurtosis(dataset['AD_SPEND']) ))
print( 'skewness of normal distribution (should be 0): {}'.format( skew(dataset['AD_SPEND']) ))
#######################

for index, row in dataset.iterrows():
    type (row['AD_TARGETING_AGE'])
    
age_list = dataset['AD_TARGETING_AGE'].tolist()

teen =  []
youngAdult = []
adult = []
middleAge=[] 
Senior =[] 
l=[]
i=0
while i < len(age_list):
    k=age_list[i].replace("+","")
    k= k.split("-")
    l.append(k)
    i+=1
j=0

while j < len(l):
    if((int(l[j][0])>= 13 and int(l[j][0]) <=17)or(int(l[j][1])>= 13 and int(l[j][1]) <=17)):
        teen.insert(j,1)
    else:teen.insert(j,0)
    if((int(l[j][0])>= 18 and int(l[j][0]) <=35)or(int(l[j][1])>= 35 )):
        youngAdult.insert(j,1)
    else:youngAdult.insert(j,0)
    if((int(l[j][0])>= 36 and int(l[j][0]) <=45)or(int(l[j][1])>= 44 )):
        adult.insert(j,1)
    else:adult.insert(j,0)
    if((int(l[j][0])>= 45 and int(l[j][0]) <=65)or(int(l[j][1])>= 45 and int(l[j][1]) <=65)):
        middleAge.insert(j,1)
    else:middleAge.insert(j,0)
    j+=1
    
###
dataset["Teen"]=teen
dataset["Young Adult"]=youngAdult
dataset["Adult"]=adult
dataset["Middle Age"]=middleAge
####
Adsteen=len([x for x in teen if x > 0])
AdsYoung=len([x for x in youngAdult if x > 0])
AdsAdult=len([x for x in adult if x > 0])
AdsMiddle=len([x for x in middleAge if x > 0])

#####
CTR_Age=[0,0,0,0]
for index, row in dataset.iterrows():
    if row['Teen']==1 :
        CTR_Age[0]+= row['CTR']
        
    else:
        CTR_Age[0]+= 0
 
    if row['Young Adult']==1 :
        CTR_Age[1]+= row['CTR']
    else:
        CTR_Age[1]+= 0
        
    if row['Adult']==1 :
        CTR_Age[2]+= row['CTR']
    else:
        CTR_Age[2]+= 0
        
    if row['Middle Age']==1 :
        CTR_Age[3]+= row['CTR']
        
    else:
        CTR_Age[3]+= 0
CTR_Age[0]=CTR_Age[0]/Adsteen
CTR_Age[1]=CTR_Age[1]/AdsYoung
CTR_Age[2]=CTR_Age[2]/AdsAdult
CTR_Age[3]=CTR_Age[3]/AdsMiddle
