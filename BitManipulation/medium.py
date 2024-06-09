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