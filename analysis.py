import random
import time
from bubbleSort import bubbleSort 
import json
import matplotlib.pyplot as plt
import numpy
import collections

timeArray = {}
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

	print (i,diff)
	timeArray[i]=diff
		

timeArray = collections.OrderedDict(sorted(timeArray.items()))
print (timeArray)
plt.bar(range(len(timeArray)), timeArray.values(), align='center')
plt.xticks(range(len(timeArray)), timeArray.keys())

plt.show()

# json_encode = json.dumps(timeArray,indent = 4)
# print(json_encode)