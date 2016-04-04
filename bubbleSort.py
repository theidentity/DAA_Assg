def bubbleSort(array):
	for i in range(0,len(array)):
		for j in range(i+1,len(array)):
			if(array[i]>array[j]):
				array[i],array[j]=array[j],array[i]
	return array;


