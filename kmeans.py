#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 21:30:44 2019

@author: osboxes
"""


from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

#si file csv
data=pd.read_csv('output.csv',sep=',')
df=pd.DataFrame(data)

print(df);
X=df.values
#print(X)

#obtener X

X=np.array(X)
s=X[:,1]
e=X[:,2]
X=np.array(list(zip(s,e))).reshape(len(s),2)
print('before clustering')

plt.plot(s,e,'b.')
plt.xlabel('sortant')
plt.ylabel('entrant')
plt.show()
#print("(e,s)  ===>  Cluster")
k=3
kmeans_model = KMeans(n_clusters = k).fit(X)

#2eme facon de afficher

colors=["r.","b.","y.","c.","m."]
labels=kmeans_model.predict(X)
#labels=sorted(labels)

print('After clustering')

listeCluster=[[],[],[],[],[]]

for i in range(len(X)):
    
    print("Cluster",labels[i], ":" , X[i])
   
    #listeCluster[labels[i]].append(X[i])

    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=10)
plt.xlabel('entrant')
plt.ylabel('sortant')
plt.show()

#print(listeCluster)
print("Cluster normalise")

for i in range(len(X)):
    X_normalize=preprocessing.Normalizer()
    X_normal=X_normalize.fit_transform([X[i]])
    
    print("Cluster",labels[i], ":" , X_normal[:,1
          ])
   
    #listeCluster[labels[i]].append(X[i])

#X_normalize=preprocessing.Normalizer()
#normal=X_normalize.fit_transform(X)
#liste=clf.predict_proba(X,y)
#print(normal)
