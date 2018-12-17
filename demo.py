import os
import pandas as pd
from saveDataNp import load_train_data, load_test_data
from sklearn.svm import SVC
from sklearn.model_selection import KFold,StratifiedKFold
import numpy as np
from sklearn.metrics import confusion_matrix, recall_score, precision_score, f1_score
import pickle, time

FA_modelFileName = os.path.join('models','faSvmModel.pkl')
MD_modelFileName = os.path.join('models','mdSvmModel.pkl')

dataPath = 'data'
testDataFile = os.path.join(dataPath, 'test.csv')

print ("\n\n\nLoading Test Data")
testData = pd.read_csv(testDataFile)

FA_testData, MD_testData = load_test_data()
labels_testData = testData.category


print ("\n--------Fractional Anisotropy--------")

print ("Loading Model")
svcFA = pickle.load(open(FA_modelFileName, 'rb'))

print ("Running Predicitions")
predictionFA = svcFA.predict(FA_testData)

print("Test Accuracy: ",(predictionFA == labels_testData.values).sum()
     / float(len(predictionFA)))
#sprint (prediction)
print ("Confusion Matrix: ",confusion_matrix(labels_testData.values,predictionFA))
print ("Recall Score: ", recall_score(labels_testData.values,predictionFA))
print ("Prediction Score: ",precision_score(labels_testData.values,predictionFA))
print ("F1 Score: ",f1_score(labels_testData.values,predictionFA))


print ("\n\n\n----------Mean Diffusivity---------")
print ("Loading Model")
svcMD = pickle.load(open(MD_modelFileName, 'rb'))

print ("Running Predicitions")
predictionMD = svcMD.predict(MD_testData)
print("Test Accuracy: ",(predictionMD == labels_testData.values).sum()
     / float(len(predictionMD)))

print ("Confusion Matrix: ",confusion_matrix(labels_testData.values,predictionMD))
print ("Recall Score: ", recall_score(labels_testData.values,predictionMD))
print ("Prediction Score: ",precision_score(labels_testData.values,predictionMD))
print ("F1 Score: ",f1_score(labels_testData.values,predictionMD))

print ("\n\n\n*#*#*#*#*#*#*#*# Finish :) *#*#*#*#*#*#*#*#*#*#")


