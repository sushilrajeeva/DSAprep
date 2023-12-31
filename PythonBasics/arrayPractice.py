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