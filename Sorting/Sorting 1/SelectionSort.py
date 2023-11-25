# Code for selection sort on a list

array = [13, 46, 24, 52, 20, 9]

def selectionSort(array) -> list:
    
    n = len(array)
    for i in range(0, n-1):
        
        min_index = i
        for j in range(i+1, n):
            if(array[j] < array[min_index]):
                min_index = j
        
        # swap (python shorthand)
        array[i], array[min_index] = array[min_index], array[i]
        
    return array

print("Given Unsorted Array: ", array)
print()
print("After applying Selection Sort: ", selectionSort(array))

# Selection sort is a simple and efficient sorting algorithm 
# it works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list. 
# it does n-2 passes

# Time: O(n*n)
# Space: O(1)

def selectionSortRecursion(array: list, start: int = 0):
    
    n = len(array)
    
    # Exit Condition (itterate till len of array -1 times)
    if start >= n-1:
        return
    
    min_index = start
    
    # itterate through the array from second position to end
    for i in range(start+1, n):
        # Swap if required
        if(array[i]< array[min_index]):
            min_index = i
    array[start], array[min_index] = array[min_index], array[start]
    
    # Recursive call
    selectionSortRecursion(array, start+1)
    
array = [13, 46, 24, 52, 20, 9]
print("Given Unsorted Array:", array)
selectionSortRecursion(array)
print("After applying Selection Sort using Recursion:", array)
    
