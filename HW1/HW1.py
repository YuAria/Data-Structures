import numpy as np
from timeit import default_timer as timer

# Parameters
ARRAYS_SORTED = 10
START_ARRAY_SIZE = 10 # Size: 2**START_ARRAY_SIZE
END_ARRAY_SIZE = 30 # Size: 2**END_ARRAY_SIZE

# Sorting Algorithms here
def InsertionSort(array):
    for index in range(1, len(array)):

        currentValue = array[index]
        position = index

        while position>0 and array[position-1]>currentValue:
            array[position]=array[position-1]
            position = position-1

        array[position]=currentValue

    return array
    
def MergeSort(array):
    if len(array) <=1:
        return array
    else:
        mid = len(array)//2
        left = array[:mid].copy()
        right = array[mid:].copy()

        MergeSort(left)
        MergeSort(right)

        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k]=left[i]
                i=i+1
            else:
                array[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            array[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            array[k]=right[j]
            j=j+1
            k=k+1

    return array

def RandomizedQuickSort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = np.random.choice(array, size = 1)[0]
        lower = []
        equal = []
        higher = []
        for num in array:
            if num < pivot:
                lower.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                higher.append(num)
        return RandomizedQuickSort(lower) + equal + RandomizedQuickSort(higher)

def CountingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * (max(array)+1)

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, (max(array)+1)):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]
        
    return array 

# Used for TimSort
def merge(arr, l, m, r): 
   
    # original array is broken in two parts  
    # left and right array  
    len1, len2 =  m - l + 1, r - m  
    left, right = [], []  
    for i in range(0, len1):  
        left.append(arr[l + i])  
    for i in range(0, len2):  
        right.append(arr[m + 1 + i])  
    
    i, j, k = 0, 0, l 
    # after comparing, we merge those two array  
    # in larger sub array  
    while i < len1 and j < len2:  
       
        if left[i] <= right[j]:  
            arr[k] = left[i]  
            i += 1 
           
        else: 
            arr[k] = right[j]  
            j += 1 
           
        k += 1
       
    # copy remaining elements of left, if any  
    while i < len1:  
       
        arr[k] = left[i]  
        k += 1 
        i += 1
    
    # copy remaining element of right, if any  
    while j < len2:  
        arr[k] = right[j]  
        k += 1
        j += 1
    
    return arr
      
# iterative Timsort function to sort the  
# array[0...n-1] (similar to merge sort)  
def TimSort(array):  

    n = len(array)
    # Sort individual subarrays of size 32 
    for i in range(0, n, 32):  
        InsertionSort(array[i:min((i+32, n))])
    
    # start merging from size RUN (or 32). It will merge  
    # to form size 64, then 128, 256 and so on ....  
    size = 32 
    while size < n:  
       
        # pick starting point of left sub array. We  
        # are going to merge arr[left..left+size-1]  
        # and arr[left+size, left+2*size-1]  
        # After every merge, we increase left by 2*size  
        for left in range(0, n, 2*size):  
           
            # find ending point of left sub array  
            # mid+1 is starting point of right sub array  
            mid = left + size - 1 
            right = min((left + 2*size - 1), (n-1))  
    
            # merge sub array arr[left.....mid] &  
            # arr[mid+1....right]  
            merge(array, left, mid, right)

          
        size = 2*size
    
    return array
    
# Uniformly Random Array
def UniformlyRandomArray(size):
    np.random.seed(0) #Set seed to return the same unsorted array each time
    return np.random.randint(1, 1001, size = (ARRAYS_SORTED, size))

# Almost Sorted Array
def AlmostSortedArray(size):
    np.random.seed(0) #Set seed to return the same unsorted array each time
    arr = np.empty((ARRAYS_SORTED, size), dtype='int') # Found that an int array is necessary for Counting Sort
    for i in range(ARRAYS_SORTED):
        arr[i] = np.arange(1, size+1)
        randomize = np.random.randint(0, size, 100)
        for index in randomize:
            arr[i][index] = np.random.randint(1, 1001)
    return arr

if __name__ == "__main__":
    for n in range(START_ARRAY_SIZE, END_ARRAY_SIZE+1):
        # Create Array
        unsortedArray = UniformlyRandomArray(2**n)
        # Sort Array
        start = timer()
        for i in range(ARRAYS_SORTED):
            array = InsertionSort(unsortedArray[i])
        end = timer()
        print(f"Sorted array w/ 2^{n} numbers")
        print(f"Time taken: {round(end-start, 2)} seconds ({int((end-start)/60)}m {round((end-start)%60)}s)")
        print(f"Average time taken: {round((end-start)/ARRAYS_SORTED, 2)} seconds")
