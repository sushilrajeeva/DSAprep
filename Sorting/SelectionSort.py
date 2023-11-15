# Code for selection sort on a list

array = [13, 46, 24, 52, 20, 9]

def SelectionSort(array) -> list:
    
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
print("After applying Selection Sort: ", SelectionSort(array))

# Selection sort is a simple and efficient sorting algorithm 
# it works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list. 
# it does n-2 passes

# Time: O(n*n)
# Space: O(1)


    
