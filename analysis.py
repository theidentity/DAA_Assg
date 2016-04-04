import random
import time
import sort
import json
import matplotlib.pyplot as plt
import numpy
import collections


fig = plt.figure()

xaxis=[]
yaxis=[]

k=0
for i in range (500,10000,1000):
	k=k+1
	if k==10:
		break
	array = random.sample(range(0,10000),i)
	startTime = time.time()
	
	sortedArray = sort.selectionSort(array)
	
	endTime = time.time()
	diff = endTime-startTime

	xaxis.append(i)
	yaxis.append(diff)

plt.plot(xaxis,yaxis,'r')
		

xaxis=[]
yaxis=[]

k=0
for i in range (500,10000,1000):
	k=k+1
	if k==10:
		break
	array = random.sample(range(0,10000),i)
	startTime = time.time()
	
	sortedArray = sort.shellSort(array)
	
	endTime = time.time()
	diff = endTime-startTime

	xaxis.append(i)
	yaxis.append(diff)

plt.plot(xaxis,yaxis,'b')
plt.show()
plt.close('all')


# json_encode = json.dumps(timeArray,indent = 4)
# print(json_encode)