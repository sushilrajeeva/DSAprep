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

# Doing the same but with recursion

def binary_search_using_recursion(arr: List, target: int) -> int:
    
    
    n = len(arr)
    low, high = 0, n - 1
    
    # defining a function to perform recursion
    def bs_recursion(arr: List, target: int, low: int, high: int) -> int:
        
        # Exit Condition
        if low > high:
            return -1
        
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
      
        elif target < arr[mid]:
            high = mid - 1
            
        else:
            low = mid + 1
            
        
        return bs_recursion(arr, target, low, high)
        
        
    
    return bs_recursion(arr, target, low, high)
        
        
        
        
arr = [1, 4, 6, 24, 53, 66, 89]
target = 24

# print(binary_search(arr, target))
print(binary_search_using_recursion(arr, target))
    
    
    