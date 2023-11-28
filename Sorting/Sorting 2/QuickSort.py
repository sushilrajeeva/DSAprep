def quickSort(inputArr: list, low: int, high: int):
    
    # Base condition
    if low > high:
        return 
    
    # Minimum Work
    
    partitionIndex = getPartitionIndex(inputArr, low, high)
    # sort left
    quickSort(inputArr, low, partitionIndex-1)
    # sort right
    quickSort(inputArr, partitionIndex+1, high)
        
    
def getPartitionIndex(inputArr: list, low: int, high: int):
    
    pivot = inputArr[low]
    i = low
    j = high
    
    
    while i < j:
        # In Left : Find out the first guy that is greater than pivot
        while (inputArr[i] <= pivot) and (i<= high):
            i+=1
            
        # In Right: Find out the first guy that is less than pivot
        while(inputArr[j] > pivot) and (j>= low):
            j-=1
    
        # after doing left and right if i is still less than j then swap
        if(i<j):
            inputArr[i], inputArr[j] = inputArr[j], inputArr[i]
    
    # after the above while executes, j'th index is the pivot location
    
    inputArr[low], inputArr[j] = inputArr[j], inputArr[low]
    return j


inputArr = [5, 6, 3, 1, 8]
print("Given Array :", inputArr)

quickSort(inputArr, 0, len(inputArr) -1)  

print("After Quick Sort :", inputArr)