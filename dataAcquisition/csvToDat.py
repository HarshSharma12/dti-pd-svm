import pandas as pd
import numpy as np

# csvFiles = ['fix_data_train_lin.csv', 'fix_fa_data_train_lin.csv', 'fix_md_data_train_lin.csv', 'fix_data_test_lin.csv', 'fix_fa_data_test_lin.csv', 'fix_md_data_test_lin.csv']

# for csvFile in csvFiles:
# 	fName = csvFile.split('.')[0]
# 	print ("In Progress: ", fName)
# 	input_pd = pd.read_csv(csvFile)
# 	input_pd.to_csv(fName+'.dat')


faTrainFile = 'fix_fa_data_train_lin.csv'
faTrainFileDat = 'fix_fa_data_train_lin.dat'

mdTrainFile = 'fix_md_data_train_lin.csv'
mdTrainFileDat = 'fix_md_data_train_lin.dat'

faTestFile = 'fix_fa_data_test_lin.csv'
faTestFileDat = 'fix_fa_data_test_lin.dat'

mdTestFile = 'fix_md_data_test_lin.csv'
mdTestFileDat = 'fix_md_data_test_lin.dat'

with open (faTrainFile, 'r') as fid:
	fidFAData = fid.readlines()

with open (mdTrainFile, 'r') as fid:
	fidMDData = fid.readlines()

with open (faTestFile, 'r') as fid:
	fidFADataTest = fid.readlines()

with open (mdTestFile, 'r') as fid:
	fidMDDataTest = fid.readlines()

faDatFile = open(faTrainFileDat, 'w')
mdDatFile = open(mdTrainFileDat, 'w')
faDatFileT = open(faTestFileDat, 'w')
mdDatFileT = open(mdTestFileDat, 'w')

idx = 0
for line1, line2, in zip(fidFAData,fidMDData):
	if (idx == 0):
		# print (line)
		newLine1 = '# '+line1
		newLine2 = '# '+line2
		# print (newLine)
	else:
		# print (line)
		fa, cat1 = line1.split(',')
		md, cat2 = line2.split(',')

		fa1 = np.float32(fa.split(' '))
		md1 = np.float32(md.split(' '))

		if ("HC" in cat1):
			newLine1 = '1 '
			newLine2 = '1 '
		else:
			newLine1 = '-1 '			
			newLine2 = '-1 '

		arrIdx = 0
		for f,m in zip(fa1,md1):
			arrIdx += 1
			if (f != 0):
				newLine1 += ' '+str(arrIdx)+':'+str(f)
			if (m != 0):
				newLine2 += ' '+str(arrIdx)+':'+str(m)

	faDatFile.write(newLine1+'\n')
	mdDatFile.write(newLine2+'\n')
	idx+=1
	print ("Lines Processed: ", idx)

print ("Lines Processed: ", idx)
print ('--------------------------------------')
faDatFile.close()
mdDatFile.close()
idx = 0
for line1, line2, in zip(fidFADataTest,fidMDDataTest):
	if (idx == 0):
		# print (line)
		newLine1 = '# '+line1
		newLine2 = '# '+line2
		# print (newLine)
	else:
		# print (line)
		fa, cat1 = line1.split(',')
		md, cat2 = line2.split(',')
		if ("HC" in cat1):
			newLine1 = '1'
			newLine2 = '1'
		else:
			newLine1 = '-1'
			newLine2 = '-1'


		fa1 = np.float32(fa.split(' '))
		md1 = np.float32(md.split(' '))

		arrIdx = 0
		for f,m in zip(fa1,md1):
			arrIdx += 1
			if (f != 0):
				newLine1 += ' '+str(arrIdx)+':'+str(f)
			if (m != 0):
				newLine2 += ' '+str(arrIdx)+':'+str(m)

	faDatFileT.write(newLine1+'\n')
	mdDatFileT.write(newLine2+'\n')	
	idx+=1
	print ("Lines Processed: ", idx)


print ("Lines Processed: ", idx)
faDatFileT.close()
mdDatFileT.close()
