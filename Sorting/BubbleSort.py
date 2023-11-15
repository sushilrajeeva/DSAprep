# Code for Bubble sort on a list

array = [13, 46, 24, 52, 20, 9]

def bubbleSort(array) -> list:
    
    passes = len(array)
    isSorted: bool
    for i in range(0,passes):
        isSorted = True
        for j in range(1, passes - i):
            
            if(array[j]< array[j-1]):
                array[j], array[j-1] = array[j-1], array[j]
                isSorted = False
        
        if isSorted:
            return array
        
        
    return array

print("Given Unsorted Array: ", array)
print()
print("After applying Bubble Sort: ", bubbleSort(array))

# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.
# This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.

# In this algorithm, 

# traverse from left and compare adjacent elements and the higher one is placed at right side. 
# In this way, the largest element is moved to the rightmost end at first. 
# This process is then continued to find the second largest and place it and so on until the data is sorted.

# Time: O(n*n)
# Space: O(1)