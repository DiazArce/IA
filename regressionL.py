#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 20:12:11 2019

@author: osboxes
"""
from sklearn import datasets
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
import numpy as np

#X = [[0.5,60],[1.6,22],[4.2,30],[1.1,22],[4.0,75],[4.2,21],[1.8,22],[2.4,83],[4.2,25]]
#print(X)
#donnees Real

a=np.array([0.9,1,0,0,1])
b=np.array([0.9,0.8,1,0,0])
c=np.array([1,0.9,0,1,0])

X_real=np.array([a,b,c])
print(X_real)
labels=[0,1,2]
y=np.array(labels)
#y2=np.array([0,0,0,0,0,1,1,1,1,1,2,2,2,2,2])
#aprentisagge 1
#label=OneVsRestClassifier(LinearSVC(random_state=0)).fit(X_real, y)
#label.fit(X_real, y)
#aprentisagge 2 par regresion model
model=LogisticRegression()
model=model.fit(X_real,y)

#donnees de la vicitme

X_victime=np.array([[1,1,0,1,0]])

#a1=np.array([0,0,0,0,0])
#b1=np.array([0.9,0.8,1,0,0])
#c1=np.array([0,0,0,0,0])

#X_victime=np.array([a1,b1,c1])

initPredict=model.predict(X_victime)
print(initPredict)

