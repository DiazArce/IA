#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 09:12:49 2019

@author: osboxes
"""

from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import numpy as np

#Pairs de rafales du domaine A

#X = [[0.5,60],[1.6,22],[4.2,30],[1.1,22],[4.0,75],[4.2,21],[1.8,22],[2.4,83],[4.2,25]]

#X_real sont les donnees Reels, apres la distribution gaussienne, where a, b, c identifient les pages

a=np.array([0.99654576,0.88235294,0.96064557,0.99503719,0,0,0,0,0])
b=np.array([0.58123819,0.4472136,0.51148386,0.6401844,0.48860337,0.64764842,0.78935222,0.57746472,0.54865644])
c=np.array([0.89442719,0.7739573,0.80873608,0.5547002,0.8454889,0,0,0,0])

X_real=np.array([a,b,c])

# y : array contenant 0,1, et 2 correpondant a ,b et c respectivement

labels=[0,1,2]
y=np.array(labels)

#aprentisagge par regresion logistique model
model=LogisticRegression()
model=model.fit(X_real,y)

#donnees de la vicitme

X_victime=np.array([[0.894,0.77,0.8,0.55,0.8454,0,0,0,0],[0.99,0.84,0.9,0.995,0,0,0,0,0]])
#print(X_victime)
# la prediction initial avec les donnees de la victime
initPredict=model.predict(X_victime)
print(initPredict)
initPredict_proba=model.predict_proba(X_victime)
print(initPredict_proba)
#print(model.score(X_victime,y))