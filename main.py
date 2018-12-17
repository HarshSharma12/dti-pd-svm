# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 17:34:04 2018

@author: Harsh Sharma
"""

import os
import pandas as pd
from saveDataNp import load_train_data, load_test_data
from sklearn.svm import SVC
from sklearn.model_selection import KFold,StratifiedKFold
import numpy as np
from sklearn.metrics import confusion_matrix, recall_score, precision_score, f1_score
import pickle, time
import warnings
warnings.filterwarnings("ignore")

dataPath = 'data'
cVal = 50
kernelType = 'rbf'
numSplits = 30
saveModel = False


trainDataFile = os.path.join(dataPath, 'train.csv')
testDataFile = os.path.join(dataPath, 'test.csv')

trainData = pd.read_csv(trainDataFile)
testData = pd.read_csv(testDataFile)

FA_trainData, MD_trainData = load_train_data()
labels_trainData = trainData.category

FA_testData, MD_testData = load_test_data()
labels_testData = testData.category


# Define shuffed Stratified Cross validator
skfFA = StratifiedKFold(n_splits=numSplits,shuffle=True)
skfMD = StratifiedKFold(n_splits=numSplits,shuffle=True)

# Define the SVM Model
svcFA = SVC(kernel=kernelType, C=cVal)
svcMD = SVC(kernel=kernelType, C=cVal)

faModelFileName = 'faSvmModel_'+str(kernelType)+'_'+str(cVal)+'_'+str(time.time())
mdModelFileName = 'mdSvmModel_'+str(kernelType)+'_'+str(cVal)+'_'+str(time.time())

print ("\n\n\nKernel: ", kernelType)
print ("cVal: ", cVal)
print ("\nTraining for FA")


trainAccsFA = []
for train, test in skfFA.split(FA_trainData, labels_trainData):
	labels_train = labels_trainData.values[train]
	svcFA.fit(FA_trainData[train], labels_train)
	prediction = svcFA.predict(FA_trainData[test])
	trainAccFA = (prediction == labels_trainData.values[test]).sum()/ float(len(labels_trainData.values[test]))
	trainAccsFA.append(trainAccFA)

if (saveModel):
	print ("Saving model")
	with open('models/'+faModelFileName+'.pkl', 'wb') as mdl:
		pickle.dump(svcFA,mdl)

predictionFA = svcFA.predict(FA_testData)
# print ("SVC Params: \n",svcFA.get_params())
print ("Train Accuracies: ", trainAccsFA)
print ("Mean train accuracy: ",np.mean(np.array(trainAccsFA)))
print("Test Accuracy: ",(predictionFA == labels_testData.values).sum()
     / float(len(predictionFA)))
#print (prediction)
print ("Confusion Matrix: ",confusion_matrix(labels_testData.values,predictionFA))
print ("Recall Score: ", recall_score(labels_testData.values,predictionFA))
print ("Prediction Score: ",precision_score(labels_testData.values,predictionFA))
print ("F1 Score: ",f1_score(labels_testData.values,predictionFA))
print ("**************************************")
print ("\nTraining for MD")


trainAccsMD = []
for train, test in skfMD.split(MD_trainData, labels_trainData):
	labels_train = labels_trainData.values[train]
	svcMD.fit(MD_trainData[train], labels_train)
	prediction = svcMD.predict(MD_trainData[test])
	trainAccMD = (prediction == labels_trainData.values[test]).sum()/ float(len(labels_trainData.values[test]))
	trainAccsMD.append(trainAccMD)

if (saveModel):
	print ("Saving model")
	with open('models/'+mdModelFileName+'.pkl', 'wb') as mdl:
		pickle.dump(svcMD,mdl)

predictionMD = svcMD.predict(MD_testData)
print ("Train Accuracies: ", trainAccsMD)
print ("Mean train accuracy: ",np.mean(np.array(trainAccsMD)))
print("Test Accuracy: ",(predictionMD == labels_testData.values).sum()
     / float(len(predictionMD)))

print ("Confusion Matrix: ",confusion_matrix(labels_testData.values,predictionMD))
print ("Recall Score: ", recall_score(labels_testData.values,predictionMD))
print ("Prediction Score: ",precision_score(labels_testData.values,predictionMD))
print ("F1 Score: ",f1_score(labels_testData.values,predictionMD))

print ("*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")

