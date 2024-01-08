# Assumptions for performing binary search on a given array
# Our array should be sorted only then we can perform binary search
# No duplicates

# This is kind of a extension of two pointer as it keeps 3 pointers to keep track of low, mid and high

# Binary Search is not just limited to arrays, we can use the same concept/algorithm to solve problems in data structure like dictionary, answers ... etc
from typing import *

def binary_search(arr: List, target: int) -> int:
    
    n = len(arr)
    
    low = 0
    high = n - 1
    
    # important condition , we should run the loop until low is lower than or equal to high, and not just lower than
    while low <= high:
        
        # mid = (low + high) // 2
        # To avoid overflow
        mid = int(low + (high - low) // 2)
        
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
        
        # mid = (low + high) // 2
        # To avoid overflow
        mid = int(low + (high - low) // 2)
        
        if arr[mid] == target:
            return mid
      
        elif target < arr[mid]:
            high = mid - 1
            
        else:
            low = mid + 1
            
        
        return bs_recursion(arr, target, low, high)
        
        
    
    return bs_recursion(arr, target, low, high)
        
        
        
        
arr = [1, 4, 6, 24, 53, 66, 89]
target = 53

# print(binary_search(arr, target))
print(binary_search_using_recursion(arr, target))

# Lower Bound
# Problem statement
# You are given an array 'arr' sorted in non-decreasing order and a number 'x'.



# You must return the index of lower bound of 'x'.



# Note:
# For a sorted array 'arr', 'lower_bound' of a number 'x' is defined as the smallest index 'idx' such that the value 'arr[idx]' is not less than 'x'

# If all numbers are smaller than 'x', then 'n' should be the 'lower_bound' of 'x', where 'n' is the size of array.

# Consider 0-based indexing.


# Example:
# Input: ‘arr’ = [1, 2, 2, 3] and 'x' = 0

# Output: 0

# Explanation: Index '0' is the smallest index such that 'arr[0]' is not less than 'x'.

def lower_bound(arr: [int], x: int) -> int:
    
    n = len(arr)
    
    # Initializing my pointers
    low, high = 0, n - 1
    
    # Initializing answer to size of the array
    answer = n
    
    while low <= high:
        
        mid = int(low + (high - low) // 2)
        
        if x <= arr[mid]:
            high = mid - 1
            answer = mid
            
            
        else:
            low = mid + 1
    
            
    return answer

n = 76
arr = [366, 482, 727, 813, 1133, 1219, 1257, 1640, 2084, 2110, 2363, 2559, 2706, 2763, 3471, 4213, 5300, 5365, 5433, 5517, 6227, 6506, 8384, 8438, 8687, 8847, 8873, 9963, 10696, 11582, 12221, 12344, 12791, 14072, 14079, 14239, 14387, 14949, 15244, 16945, 17516, 19637, 20011, 20504, 20687, 20959, 21252, 21570, 21620, 21651, 22922, 23369, 24141, 24852, 25012, 25192, 25496, 25694, 25843, 27359, 27368, 27523, 28123, 28339, 28568, 29072, 29560, 30259, 30321, 30388, 30918, 31410, 31748, 32370, 32512, 32647]
x = 17111

print(lower_bound(arr, x))

# Upper Bound
# Problem statement
# You are given a sorted array ‘arr’ containing ‘n’ integers and an integer ‘x’.



# Implement the ‘upperBound’ function to find the index of the upper bound of 'x' in the array.



# Note:
# The upper bound in a sorted array is the index of the first value that is greater than a given value. 
# If the greater value does not exist then the answer is 'n', Where 'n' is the size of the array.
# We are using 0-based indexing.
# Try to write a solution that runs in log(n) time complexity.


# Example:

# Input : ‘arr’ = {2,4,6,7} and ‘x’ = 5,

# Output: 2

# Explanation: The upper bound of 5 is 6 in the given array, which is at index 2 (0-indexed).

def upper_bound(arr: [int], x: int) -> int:
    n = len(arr)
    
    # Initializing my pointers
    low, high = 0, n - 1
    
    # Initializing answer to size of the array
    answer = n
    
    while low <= high:
        
        mid = int(low + (high - low) // 2)
        
        if x < arr[mid]:
            high = mid - 1
            answer = mid
            
            
        else:
            low = mid + 1
    
            
    return answer


x = 42
arr = [1, 2, 13, 16, 19, 23, 25, 29, 36, 37, 42, 44]

print(upper_bound(arr, x)) 


# Search Insert Postion
# This is same as finding the lower bound to insert the element

# Problem Descripion
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

def search_insert(nums: List[int], target: int) -> int:
    
    return lower_bound(nums, target)


target = 28
arr = [4, 23, 33, 37, 40]

print(search_insert(arr, target)) 

    
    