array = [13, 46, 24, 52, 20, 9]

def insertionSort(array: list) -> list:
    
    for i in range(1,len(array)):
        
        j = i
        while j>0 and array[j] < array[j-1]:
                # swap
            array[j], array[j-1] = array[j-1], array[j]
            j-=1
        
    return array

    # Time: O(n*n)
    # Space: O(1)


print("Given Unsorted Array: ", array)
print()
print("After applying Insertion Sort: ", insertionSort(array))    