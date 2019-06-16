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
import random

#importing the dataset
dataset= pd.read_excel('data_IRA_Ads.xlsx')
data= dataset.iloc [:,:].values

#splitting the dataset into two
from sklearn.cross_validation import  train_test_split
x_Part1 ,x_Part2 = train_test_split(data,test_size=0.05,random_state=0)
df = pd.DataFrame(x_Part2)
Dataset_to_be_lebeled = open("Dataset_to_be_lebeled.csv", "x")
columns1 = list(dataset.columns.values)
df.columns = [columns1]
df.to_csv(Dataset_to_be_lebeled, encoding='utf-8', index=False)