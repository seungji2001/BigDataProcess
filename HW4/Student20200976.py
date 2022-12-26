#!/usr/bin/python3
import os
import numpy as np
import sys
import operator


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    return normDataSet, ranges, minVals

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(),
            key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]
	
def labeling(filename, arr):
	dist = np.array(arr,float)
	label = filename.split('/')[1].split('.')[0].split('_')[0]
	
	return dist, label

trainingFolder = sys.argv[1]
testFolder = sys.argv[2]
all_file = (os.listdir(trainingFolder))
trainSetY = []
trainLabel = []
for file in all_file:
	file = '%s/%s' %(trainingFolder, file)
	with open(file) as fp:
		arr = []
		for line in fp.readlines():
			line = str.strip(line)
			arr.extend(line)
		value, label = labeling(file, arr)
		trainSetY.append(value)
		trainLabel.append(label)

trainSetY = np.array(trainSetY)
testSetX = []
testLabel = []
all_file = (os.listdir(testFolder))
for file in all_file:
	file = '%s/%s' %(testFolder, file)
	with open(file) as fp:
		arr = []
		for line in fp.readlines():
			line = str.strip(line)
			arr.extend(line)
		testValue, label = labeling(file, arr)
		testSetX.append(testValue)
		testLabel.append(label)
for k in range(1, 21):
	i = 0
	cnt = 0
	for x in testSetX:
		list = np.array(x)
		predict = classify0(list,trainSetY,trainLabel,k)
		if predict != testLabel[i]:
			cnt+=1
		i+=1
	
	print('%d' %((cnt/len(testSetX))*100))	
