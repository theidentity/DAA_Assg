def bubbleSort(array):
	for i in range(0,len(array)):
		for j in range(i+1,len(array)):
			if(array[i]>array[j]):
				array[i],array[j]=array[j],array[i]
	return array;

def selectionSort(array):
   for fillslot in range(len(array)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if array[location]>array[positionOfMax]:
               positionOfMax = location

       array[fillslot],array[positionOfMax] = array[positionOfMax],array[fillslot]

def shellSort(array):
    sublistcount = len(array)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(array,startposition,sublistcount)

      sublistcount = sublistcount // 2

def gapInsertionSort(array,start,gap):
    for i in range(start+gap,len(array),gap):

        currentvalue = array[i]
        position = i

        while position>=gap and array[position-gap]>currentvalue:
            array[position]=array[position-gap]
            position = position-gap

        array[position]=currentvalue