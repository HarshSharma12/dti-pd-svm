# PD using DTI

This document lists the execution flow and the list of files in the codebase 

### Execution Flow

**Training+Testing**

1. Acquire the preprocessed training and testing data set (*.npy files),
2. Acquire the label files (*.csv file)
2. Place all the files in 'data' folder
3. Update the 'dataPath' variable (if placed somewhere else) and the saveModel flag (if you plan to save the trained model)
4. Run _main.py_ file using python3.

**Only Testing**

1. Acquire the preprocessed testing data set (*.npy files),
2. Acquire the label files (*.csv file)
3. Acquire the saved model file (*.pkl files),
4. Place the data and label files in 'data' folder and model files in 'models' folder,
5. Update the 'dataPath' variable  and the model file names/location (if placed somewhere else)
6. Run _demo.py_ file using python3.


### Filelist

- preprocessing/ - Contains the shell scripts to preprocess the images. 
- models/ - location of saved SVM models
- data/ - location of training and testing data
- dataAcquisition/ - random scripts 
     1. createCSVDataset.py - create train.csv and test.csv to store the location and names of all related files for a subject along with the class
     2. csvToDat.py - create *.dat files from *.csv file for use with WEKA
- main.py - The main code file. Run this to train and test the model.
- demo.py - Reads the saved model file and predicts the classes for the test dataset
- saveDataNp.py - Methods to read and save train and test data as *npy files.

&nbsp;


### Required modules

**Training/Testing**
- pandas
- pickle
- scikit-learn
- numpy
- nibabel

**For Data Preprocessing**
- dcm2niix or mricrogl_lx
- fsl
    1. eddy
    2. bet
    3. dtifit


### Demo and Code

Code available at - [https://github.com/HarshSharma12/dti-pd-svm](https://github.com/HarshSharma12/dti-pd-svm)
Demo video is available at - [https://drive.google.com/a/ualberta.ca/file/d/1t0ADAqo9lDGTKzxX5tc2LduHRVa8eLCq/view?usp=sharing](https://drive.google.com/a/ualberta.ca/file/d/1t0ADAqo9lDGTKzxX5tc2LduHRVa8eLCq/view?usp=sharing)