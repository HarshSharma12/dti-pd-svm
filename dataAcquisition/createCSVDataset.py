import glob, os

dirNames = ['combined_Control','combined_PD']
dataSetFileName = 'dataSet.csv'

header='bvec,bval,original,corrected,FA,MD,L1,L2,L3,V1,V2,V3,class\n'

with open(dataSetFileName,'w') as file:
    file.write(header)

for dirName in dirNames:
	for file in glob.glob(os.path.join(dirName,"*.json")):
	    fileList = []
	    jsonFileName = file.split('/')[1]
	    baseFileName = jsonFileName.split('.')[0]

	    bvecFileName = baseFileName + '.bvec'
	    bvalFileName = baseFileName + '.bval'
	    origFileName = baseFileName + '.nii.gz'
	    corrFileName = baseFileName + '_corrected.nii.gz'
	    fileList = [bvecFileName,bvalFileName,origFileName,corrFileName]

	    
	    fileList.append(baseFileName + '_FA.nii.gz')
	    fileList.append(baseFileName + '_MD.nii.gz')
	    fileList.append(baseFileName + '_L1.nii.gz')
	    fileList.append(baseFileName + '_L2.nii.gz')
	    fileList.append(baseFileName + '_L3.nii.gz')
	    fileList.append(baseFileName + '_V1.nii.gz')
	    fileList.append(baseFileName + '_V2.nii.gz')
	    fileList.append(baseFileName + '_V3.nii.gz')

	    line= ','.join(fileList)


	    if (dirName.find('Control') > 0):
	    	line+=',0\n'
	    else:
	    	line+=',1\n'

	    with open(dataSetFileName,'a') as file:
	        file.write(line)




