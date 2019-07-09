#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:17:17 2019

@author: nadabeili
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#importing the dataset
df = pd.read_csv (r'Cleaned_data_with-tags.csv',encoding = 'unicode_escape')
## delete the rows with ctr=0
#df = df[df.CTR != 0]
#df= df[['AD_ID','CTR','flag','AD_TARGETING_AGE']]
################################################
# try to analyse CTR of positive/ Negative/Neutral ADS
dataPositive= df.loc[df['flag']== 'positive']
dataNegative= df.loc[df['flag']== 'negative']
dataNeutral= df.loc[df['flag']== 'neutral']

###Plot
fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(dataPositive['AD_ID'],dataPositive['CTR'],'Xr', label="Positive Ads")
ax.plot(dataNegative['AD_ID'],dataNegative['CTR'],'Xb', label="Negative Ads")
ax.plot(dataNeutral['AD_ID'],dataNeutral['CTR'],'Xg', label="Neutral Ads")
ax.legend()
##############Age target

for index, row in df.iterrows():
    type (row['AD_TARGETING_AGE'])
    
age_list = df['AD_TARGETING_AGE'].tolist()

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
df["Teen"]=teen
df["Young Adult"]=youngAdult
df["Adult"]=adult
df["Middle Age"]=middleAge
###
df = df[df.CTR != 0]
df= df[['AD_ID','CTR','flag','AD_TARGETING_AGE','Teen','Young Adult','Adult','Middle Age']]
#########
dataTeen= df.loc[(df['Teen']== 1 )& (df['Young Adult']!= 1 )& (df['Adult'] != 1 )& (df['Middle Age']!= 1)]
dataYoungAdult= df.loc[(df['Teen']!= 1 )& (df['Young Adult']== 1 )& (df['Adult'] != 1 )& (df['Middle Age']!= 1)]
dataAdult= df.loc[(df['Teen']!= 1 )& (df['Young Adult']!= 1 )& (df['Adult'] == 1 )& (df['Middle Age']!= 1)]
dataMiddleAge= df.loc[(df['Teen']!= 1 )& (df['Young Adult']!= 1 )& (df['Adult'] != 1 )& (df['Middle Age']== 1)]
##Plot
fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(dataTeen['AD_ID'],dataTeen['CTR'],'*r', label="Teen Ads")
ax.plot(dataYoungAdult['AD_ID'],dataYoungAdult['CTR'],'.b', label="Young Adult Ads")
ax.plot(dataAdult['AD_ID'],dataAdult['CTR'],'+g', label="Adult Ads")
ax.plot(dataMiddleAge['AD_ID'],dataMiddleAge['CTR'],'+', label="Young Adult Ads")
ax.legend()
ax.set_xlabel('Ads ID')
ax.set_ylabel('CTR')
ax.set_title('CTR of different Ads targeting specific group');


dataTeenY= df.loc[(df['Teen']== 1 )& (df['Young Adult']== 1 )& (df['Adult'] != 1 )& (df['Middle Age']!= 1)]
dataAdultM= df.loc[(df['Teen']!= 1 )& (df['Young Adult']!= 1 )& (df['Adult'] == 1 )& (df['Middle Age']== 1)]
dataAdultY= df.loc[(df['Teen']!= 1 )& (df['Young Adult']== 1 )& (df['Adult'] == 1 )& (df['Middle Age']!= 1)]
dataAll= df.loc[(df['Teen']== 1 )& (df['Young Adult']== 1 )& (df['Adult'] == 1 )& (df['Middle Age']== 1)]

###
fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(dataTeenY['AD_ID'],dataTeenY['CTR'],'*r', label="Teen and Young Adult Ads")
ax.plot(dataAdultM['AD_ID'],dataAdultM['CTR'],'.g', label=" Adult and Middle Age Ads")
ax.plot(dataAdultY['AD_ID'],dataAdultY['CTR'],'+b', label=" Adult and Young Adult Ads")
ax.plot(dataAll['AD_ID'],dataAll['CTR'],'*', label=" Targeting all the groups Ads")
ax.legend()
ax.set_xlabel('Ads ID')
ax.set_ylabel('CTR')
ax.set_title('CTR of Ads targeting different groups');

#####positive and negative Ads for the Ads targeting all the groups
dataAllPositive= dataAll.loc[dataAll['flag']== 'positive']
dataAllNegative= dataAll.loc[dataAll['flag']== 'negative']
dataAllNeutral= dataAll.loc[dataAll['flag']== 'neutral']
####plot
###
fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(dataAllPositive['AD_ID'],dataAllPositive['CTR'],'*r', label="positive Ads")
ax.plot(dataAllNegative['AD_ID'],dataAllNegative['CTR'],'.g', label=" Negative Ads")
ax.plot(dataAllNeutral['AD_ID'],dataAllNeutral['CTR'],'+b', label=" Neutral Ads")

ax.legend()
ax.set_xlabel('Ads ID')
ax.set_ylabel('CTR')
ax.set_title('CTR of positive, negative and neutral Ads targeting all the groups');
######################
##Ads targeting teen and young Adult
dataTeenYPositive= dataTeenY.loc[dataTeenY['flag']== 'positive']
dataTeenYNegative= dataTeenY.loc[dataTeenY['flag']== 'negative']
dataTeenYNeutral= dataTeenY.loc[dataTeenY['flag']== 'neutral']
#########plot
fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(dataTeenYPositive['AD_ID'],dataTeenYPositive['CTR'],'*r', label="positive Ads")
ax.plot(dataTeenYNegative['AD_ID'],dataTeenYNegative['CTR'],'.g', label=" Negative Ads")
ax.plot(dataTeenYNeutral['AD_ID'],dataTeenYNeutral['CTR'],'+b', label=" Neutral Ads")

ax.legend()
ax.set_xlabel('Ads ID')
ax.set_ylabel('CTR')
ax.set_title('CTR of positive, negative and neutral Ads targeting Teenager and young Adult');
######################
