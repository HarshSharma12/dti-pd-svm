# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 23:24:37 2018

@author: Harsh Sharma

"""

from __future__ import print_function

import os
import glob
import numpy as np
import nibabel as nib
import pandas as pd


baseDataPath = 'data'
trainDataPath = os.path.join(baseDataPath , 'train')
testDataPath = os.path.join(baseDataPath , 'test')
trainDataFile = os.path.join(baseDataPath , 'train.csv')
testDataFile = os.path.join(baseDataPath, 'test.csv')

FA_trainDataFileName = 'fa_data_train_lin.npy'
MD_trainDataFileName = 'md_data_train_lin.npy'
FA_testDataFileName = 'fa_data_test_lin.npy'
MD_testDataFileName = 'md_data_test_lin.npy'

image_height = 116 #rows
image_width  = 116 #cols
image_depth  =  72 #depth

def create_data(isTrain): 
    dataPath = trainDataPath if isTrain else testDataPath
    csvData = pd.read_csv(trainDataFile) if isTrain else pd.read_csv(testDataFile)
    
    FA_imgs_list = csvData.FA
    MD_imgs_list = csvData.MD

    total = len(FA_imgs_list)
    FA_imgs = np.ndarray((total, image_height*image_width*image_depth), dtype=np.float32)
    MD_imgs = np.ndarray((total, image_height*image_width*image_depth), dtype=np.float32)

    print ("\n\n\n\nStarting Process for path: "+dataPath)
    i=0

    for file in FA_imgs_list:
        fa_in = nib.load(os.path.join(dataPath, file))
        fa_raw = fa_in.get_data().astype('float32') #116x116x72      
        flatData = fa_raw.flatten()
        FA_imgs[i] = np.array([flatData])

        if i % 20 == 0:
            print('FA - Done: {0} images'.format(i))
        i += 1

    print('FA - Done: {0} images'.format(i))


    i=0
    for file in MD_imgs_list:
        md_in = nib.load(os.path.join(dataPath, file))
        md_raw = md_in.get_data().astype('float32') #116x116x72        
        flatData = md_raw.flatten()
        MD_imgs[i] = np.array([flatData])
        if i % 20 == 0:
            print('MD - Done: {0} images'.format(i))
        i += 1

    print('MD - Done: {0} images'.format(i))


    
    print('Starting saving process.')
    if (isTrain):
        np.save(FA_trainDataFileName, FA_imgs)
        np.save(MD_trainDataFileName, MD_imgs)
    else:
        np.save(FA_testDataFileName, FA_imgs)
        np.save(MD_testDataFileName, MD_imgs)
    
    print('Saving to .npy files done.')


def load_train_data():
    baseDataPath = 'data'
    faFile = os.path.join(baseDataPath, FA_trainDataFileName)
    mdFile = os.path.join(baseDataPath, MD_trainDataFileName)

    fa_data_train = np.load(faFile)
    md_data_train = np.load(mdFile)
    return fa_data_train, md_data_train

def load_test_data():
    baseDataPath = 'data'
    faFile = os.path.join(baseDataPath, FA_testDataFileName)
    mdFile = os.path.join(baseDataPath, MD_testDataFileName)

    fa_data_test = np.load(faFile)
    md_data_test = np.load(mdFile)
    return fa_data_test, md_data_test

if __name__ == '__main__':
   create_data(True)
   create_data(False)