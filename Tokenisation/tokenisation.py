# -*- coding: utf-8 -*-
"""tokenisation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OHl0TSa5-UyidgCrpeOSI09ayamW59Sc
"""

import pandas as pd
doc=pd.read_excel('C:/Users/Naik/Desktop/Lab Session2 Data.xlsx')

print(doc)

import nltk
from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords

stops = set(stopwords.words('english'))
print(stops)

len(stops)



df = pd.DataFrame(doc, columns=['Student', 'Report'])

print(df['Report'][10])

temp = df['Report'][10]
temp.split()

num_stu= df.shape[0]
num_stu

for i in range(num_stu):
    print(i)

token_population = []
#initialise the token population with the first string 
temp = df['Report'][0]
#token_population.append(temp.split())
token_population =temp.split()
token_population 
for i in range(1,num_stu):
    temp = df['Report'][i]
    temp2 = temp.split()
    for j in temp2:
        if not j in token_population:
            token_population.append(j)
            
token_population
#len(token_population)

bag_words=  token_population
    

for i in stops:
    #print(i)
   
    if i in token_population:
       
        bag_words.remove(i)
print(bag_words)

bag_num = len(bag_words)
bag_num

import numpy as np
arr = np.empty([num_stu, bag_num], dtype=int)
arr1 = np.empty([num_stu, bag_num], dtype=int)

for i in range(0, num_stu):
    for j in range(0,bag_num):
        if bag_words[j] in df['Report'][i]:
            arr1[i][j]= df['Report'][i].count(bag_words[j])
            arr[i][j]= 1
        else:
            arr[i][j]= 0
            arr1[i][j]=0

#arr[:,0]
arr[1,:]
#arr1[0,:]

from sklearn.metrics import jaccard_score
jacc_sim = np.zeros([num_stu, num_stu], dtype=float)
for i in range(0,num_stu):
    for j in range(0,num_stu):
         jacc_sim[i][j]= jaccard_score(arr[i,:], arr[j,:])

jaccard_score(arr[1,:], arr[2,:])

jacc_sim



jacc_sim.shape

from sklearn.metrics.pairwise import cosine_similarity
cos_sim = np.zeros([num_stu, num_stu], dtype=float)
for i in range(0,num_stu):
    for j in range(0,num_stu):
        cos_sim[i][j] =cosine_similarity(arr1[i,:], arr1[j,:])
cos_sim

cos_sim = cosine_similarity(arr1[:], arr1[:])

import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize = (37,37))

sns.heatmap(jacc_sim, annot = True)

import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize = (37,37))

sns.heatmap(cos_sim, annot = True)





