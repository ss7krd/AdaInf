import numpy as np
import pandas as pd
import random
import sys
import os

#type = 1 is inference task,  type = 2 is retraining task
class DAGVertex:
	def __init__(self, __type, __degree=None, __isRoot=None, __id=None)
		self.type = __type
		self.degree = __degree
		self.isRoot = __isRoot
		self.id = __id

# allDAGVerticesTypeOneList = []
allDAGVerticesTypeOneDict = {}
allDAGVerticesConnectionDict = {}
fileName = "initial_dag.txt"
with open(fileName, 'r', encoding = 'utf8') as inputFile:
	for line in inputFile:
		lineStrList = line.strip().split()
		firstId = int(listStrList[0])
		secondId = int(listStrList[1])
		if allDAGVerticesTypeOneDict.has_key(firstId):
			dummy = 2
		else:
			newDAGVertex = DAGVertex(1, None, firstId, firstId)
			allDAGVerticesTypeOneDict[firstId] = newDAGVertex
			allDAGVerticesConnectionDict[newDAGVertex] = []
		if allDAGVerticesTypeOneDict.has_key(secondId):
			dummy = 2
		else:
			newDAGVertex1 = DAGVertex(1, None, secondId, secondId)
			allDAGVerticesTypeOneDict[secondId] = newDAGVertex1
		allDAGVerticesConnectionDict[allDAGVerticesTypeOneDict[firstId]].append(allDAGVerticesTypeOneDict[secondId])

root = allDAGVerticesTypeOneDict[firstId]
for vertex in allDAGVerticesTypeOneDict.keys():
	if vertex.type == 1:
		retrainingNeeded = 0
		degree = -1
		if retrainingNeeded == 1:
			newDAGVertex = DAGVertex(2, degree, None, vertex.id)
			allDAGVerticesConnectionDict[newDAGVertex] = []
			allDAGVerticesConnectionDict[newDAGVertex].append(vertex)
			if vertex.isRoot == 1:
				newDAGVertex.isRoot = 1
				root = newDAGVertex
				vertex.isRoot = None