# Assumptions for performing binary search on a given array
# Our array should be sorted only then we can perform binary search
# No duplicates

# This is kind of a extension of two pointer as it keeps 3 pointers to keep track of low, mid and high
from typing import *

def binary_search(arr: List, target: int) -> int:
    
    n = len(arr)
    
    low = 0
    high = n - 1
    
    # important condition , we should run the loop until low is lower than or equal to high, and not just lower than
    while low <= high:
        
        mid = (low + high)//2
        
        # Condition 1 - if target == arr[mid]
        if target == arr[mid]:
            return mid
        
        # Condition 2 - if target < arr[mid]
        elif target < arr[mid]:
            high = mid - 1
        
        # Condition 3 - if target > arr[mid]
        else:
            low = mid + 1
            
        
    return -1
        
        
arr = [1, 4, 6, 24, 53, 66, 89]
target = 53

print(binary_search(arr, target))
    
    
    