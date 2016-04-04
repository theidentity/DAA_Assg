import random
import time
from bubbleSort import bubbleSort 
import json
import matplotlib.pyplot as plt
import numpy
import collections

xaxis=[]
yaxis=[]

f=open('timeFile','w')
k=0;

for i in range (500,10000,1000):
	k=k+1
	if k==5:
		break
	array = random.sample(range(0,10000),i)
	startTime = time.time()
	
	sortedArray = bubbleSort(array)
	
	endTime = time.time()
	diff = endTime-startTime

	xaxis.append(i)
	yaxis.append(diff)
	timeArray[i]=diff
		

timeArray = collections.OrderedDict(sorted(timeArray.items()))
plt.plot(xaxis,yaxis)

plt.show()
exit(0)

# json_encode = json.dumps(timeArray,indent = 4)
# print(json_encode)