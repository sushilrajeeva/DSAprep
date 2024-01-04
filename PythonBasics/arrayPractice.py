# Count Maximum Consecutive One’s in the array
# Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.

# Examples:

# Example 1:

# Input: prices = {1, 1, 0, 1, 1, 1}

# Output: 3

# Explanation: There are two consecutive 1’s and three consecutive 1’s in the array out of which maximum is 3.

# Input: prices = {1, 0, 1, 1, 0, 1} 

# Output: 2

# Explanation: There are two consecutive 1's in the array. 

input = [1, 1, 0, 1, 1, 1]
input1 = [1, 0, 1, 1, 0, 1]
def max_ones(arr: list):
    
    max_range = 0
    cur_range = 0
    
    for i in range(len(arr)):
        
        if(arr[i] == 0):
            cur_range = 0
        else:
            cur_range += 1
            
        max_range = max(max_range, cur_range)
            
    return max_range

print(max_ones(input))
print(max_ones(input1))

def moveZeros(n: int,  a: list) -> list:
    
    j = -1
    for i in range(n):
        if a[i] == 0:
            j= i 
            break
        
    
    if j == -1:
        return a
    
    for i in range(j+1, n):
        if a[i] != 0:
            a[i], a[j] = a[j], a[i]
            j+=1
            
    return a

input = [0,0,0,1]

print(moveZeros(4, input))


# Rotate array by K elements
# Rotate array by K elements

# Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.

# Examples:

# Example 1:
# Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
# Output: 6 7 1 2 3 4 5
# Explanation: array is rotated to right by 2 position .

# Example 2:
# Input: N = 6, array[] = {3,7,8,9,10,11} , k=3 , left 
# Output: 9 10 11 3 7 8
# Explanation: Array is rotated to right by 3 position.

def rotate_by_k(arr: list, k: int, position: str) -> list:
    
    k = k%len(arr)
    if k == 0:
        return arr
    
    if position == "left":
        temp = [arr[i] for i in range(k)]
        
        for i in range(k, len(arr)):
            arr[i-k] = arr[i]
            
        for i in range(len(temp)):
            # print("arr", arr[len(arr) - k], "temp", temp[i])
            arr[len(arr) - k+i] = temp[i]
       
    if position == "right":
        n = len(arr)
        # Store the last k elements in a temporary array
        temp = arr[n-k:]

        # Shift the rest of the array elements right by k positions
        for i in range(n-k-1, -1, -1):
            arr[i+k] = arr[i]

        # Place the elements from the temporary array at the beginning
        for i in range(k):
            arr[i] = temp[i]
            
            
    
    return arr

input = [1,2,3,4,5,6,7]
k = 3
position = "right"

print(rotate_by_k(input, k, position))


from typing import *

def missingNumber(a : list, N : int) -> int:
    # Write your code here.
    total = int(N * ((N+1)/2))
    print("total",total)
    for i in range(len(a)):
        total = total - a[i]

    return total

print(missingNumber([1,2,3], 4))

def searchMatrix(mat: [[int]], target: int) -> bool:
    # Write your code here.
    
    for row in mat:
        if target < row[0]:
            return False
        
        if target <= row[-1]:
            res = False
            for ele in row:
                if ele == target:
                    res = True 
            return res
        
print(searchMatrix( [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 8))


def sort012(arr, n) :

	# write your code here
    # don't return anything 
    count_zeros = 0
    count_ones = 0
    count_twos = 0

    for i in range(n):

        if arr[i] == 0:
            print(arr[i] , "= 0")
            count_zeros += 1
        elif arr[i] == 1:
            print(arr[i] , "= 1")
            count_ones += 1
        else:
            print(arr[i] , "= 2")
            count_twos += 1
            
    print(count_zeros, count_ones, count_twos)

    for i in range(count_zeros):
        
        arr[i] = 0
    print("0s", arr)

    for i in range(count_zeros, count_zeros + count_ones):
        
        arr[i] = 1
    print("1s", arr)

    for i in range(count_zeros + count_ones, count_zeros + count_ones + count_twos):
        
        arr[i] = 2
    print("02", arr)

    return arr

print(sort012([0, 1, 2, 2, 1, 0], 6))