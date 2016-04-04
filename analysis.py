import random
import time
import sort
import matplotlib.pyplot as plt
import collections

fig = plt.figure()

xaxis=[]
yaxis=[]
X=[]
Y=[]

k=0

for n in range (500,10000,1000):
	k=k+1
	if k==4:
		break
	array = random.sample(range(0,10000),n)
	startTime = time.time()

	sortedArray = sort.selectionSort(array)
	
	endTime = time.time()
	diff = endTime-startTime

	xaxis.append(n)
	yaxis.append(diff)

	X.append(xaxis)
	Y.append(yaxis)

plt.plot(X[1],Y[1],'r')
		
# xaxis=[]
# yaxis=[]

# k=0
# for i in range (500,10000,1000):
# 	k=k+1
# 	if k==10:
# 		break
# 	array = random.sample(range(0,10000),i)
# 	startTime = time.time()
	
# 	sortedArray = sort.shellSort(array)
	
# 	endTime = time.time()
# 	diff = endTime-startTime

	# xaxis.append(i)
	# yaxis.append(diff)

# plt.plot(xaxis,yaxis,'b')
plt.show()
plt.close('all')


# json_encode = json.dumps(timeArray,indent = 4)
# print(json_encode)