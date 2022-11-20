"""
def SelectionSort(array,size):
    for i in range(size):
        mindex=i
        for j in range(i + 1, size):
            if array[j] < array[mindex]:
                mindex = j
        (array[i], array[mindex]) = (array[mindex], array[i])
 
arr = [3,5,2,1,0,9]
size = len(arr)
SelectionSort(arr, size)
print('Dizinin siralanmis hali')
print(arr)
"""
"""
def İnsertionSort(arr):
    for i in range(1, len(arr)):
 
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
 
arr = [10,16,18,9,0,3]
İnsertionSort(arr)
print(arr)
"""
"""
def BubbleSort(arr):
    n=len(arr)
    swap=False
    for i in range (n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                swap=True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swap:
            return
"""
"""
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    i = 0    
    j = 0     
    k = l     
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
  
def MergeSort(arr, l, r):
    if l < r: 
        m = l+(r-l)//2

        MergeSort(arr, l, m)
        MergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 
arr = [1,2,3,6,5,9,0]
n = len(arr) 
MergeSort(arr, 0, n-1)
print("Siralanmis hali")
for i in range(n):
    print("%d" % arr[i],end=" ")

"""
"""
def partition(array, low, high):

	pivot = array[high]
	i = low - 1
	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])
	(array[i + 1], array[high]) = (array[high], array[i + 1])
	return i + 1

def QuickSort(array, low, high):
	if low < high:
		pi = partition(array, low, high)
		QuickSort(array, low, pi - 1)
		QuickSort(array, pi + 1, high)


arr = [1,6,7,0,8,5,4,6,3]
size = len(arr)

QuickSort(arr, 0, size - 1)

print('Listelenmis hali:')
print(arr)
"""