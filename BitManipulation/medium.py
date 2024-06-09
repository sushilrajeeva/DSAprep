from typing import *

counter = 0
def new_block(message: str) -> None:
    global counter
    counter += 1
    print()
    print(f"********************** {counter}. {message} **********************")

# Minimum Bits to convert to a number
new_block("Minimum Bits to convert to a number")

def minimum_bit_flip(start: int, goal: int) -> int:
    
    # Step 1: XOR the start and goal to set all the bits that needs to be changed, bits that don't have to be changed will be 0

    compute = start ^ goal

    # Step 2: Write logic to count all the set bits:

    def count_set_bits(num: int) -> int:
        
        count = 0
        while num:
            # add the 0th bit in every itteration
            count += num & 1
            num = num >> 1 # right shifting to remove the 0th bit
        return count
    
    res = count_set_bits(compute)
    return res

start = 7
goal = 4
print(f"Given start: {start} and goal: {goal}")
print("Number of bits required to flip:", minimum_bit_flip(start, goal))

# Find the number that appears odd number of time
new_block("Find the number that appears odd number of time")

def getOddRepeatNum(arr: List[int]) -> int:

    xor = 0

    for ele in arr:
        xor ^= ele

    return xor

arr = [4, 1, 3, 1, 3]
print(f"Given arr: {arr}")
print("result ->", getOddRepeatNum(arr))

# Print all the subsets of an array of numbers
# Note number of subsets  = 2^n => (1 << n)
new_block("Print all the subsets of an array of numbers")

def powerSet(arr: List[int]) -> List[List[int]]:

    # no of columns/elements in arr
    n = len(arr)
    # no of rows / number of subsets [2^n]
    rows = 1 << n

    ans = []

    for row in range(rows):
        temp = []
        for col in range(n):
            if row & (1<<col):
                temp.append(arr[col])
        
        ans.append(temp)

    return ans

arr = [1, 2, 3]
print(f"Given arr: {arr}")
print("Subsets:", powerSet(arr))

# Xor of numbers in range left to right
# You are given two integers L and R, your task is to find the XOR of elements of the range [L, R].

new_block("Xor of numbers in range left to right")

def xorRange(left: int, right: int) -> int:

    # Step 1: logic to get xor or 1 to n
    # Pattern to notice is below, every 4 number have same pattern
    def xor_n(num: int) -> int:
        if num%4 == 0:
            return num
        elif num%4 == 1:
            return 1
        elif num%4 == 2:
            return num+1
        else: return 0

    # step 2: xor of 1 to left-1 result and xor of 1 to right result when we xor these both we will get xor of left to right

    return xor_n(left-1) ^ xor_n(right)

left, right = 4, 8
print(f"Given left: {left} and right: {right}")
print(f"Xor of numbers from {left} to {right} =", xorRange(left, right))

    
