from typing import *

counter = 0
def new_block(message: str) -> None:
    global counter
    counter += 1
    print()
    print(f"********************** {counter}. {message} **********************")


# Convert a given number to binary array
def number_to_binary(n: int) -> List[int]:
    res = []
    while n != 0:
        res.append(n%2)
        n = n//2
    return res[::-1]
n = 11
new_block("Converting number to binary arrary")
print(f"Converting {n} to binary -> ", number_to_binary(n))
arr = number_to_binary(n)
# Convert binary to number
new_block("Converting binary array to number")
def binary_to_number(arr: List[int]) -> int:
    res = 0
    for i, bit in enumerate(arr[::-1]):
        res += bit * (2**i)
    return res

print(f"Converting {arr} to binary -> ", binary_to_number(arr))

# Swap two numbers
def swap_to_numbers(a: int, b: int):
    # a, b = b, a
    # return a, b

    # Using bit manipulation
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

new_block("Swap two numbers")
a = 5
b = 10
print(f"Before swap: a = {a}, b = {b}")
a, b = swap_to_numbers(a, b)
print(f"After swap: a = {a}, b = {b}")

# Check if ith bit is set or not
def is_ith_set(N: int, i: int) -> bool:
    # bit = -1 * i
    # bit -= 1
    # return True if arr[bit] == 1 else False
    # Bit manipulation method
    # First i will move my 1 to i places , this means after shifting this number has all other bits to 0 except the ith bit which is 1
    # now if i and it with the given number, that means all bits will be and with 0 except the ith bit
    # when we and and if any one has 0 then the whole thing is 0 only if both have 1 it is 1
    # so when we and our left shift of i places of 1 with the number, all other bits becomes 0 and the and on ith bits of both 1 left shift i place value and the number ith bit will be either 0 or more 1
    # so end result will be either 0 or a number that is not 0. hence we can just do this operation and if it is not 0 then it is true else false
    # return N & (1 << i) != 0

    # Similarly if we are doing it with right shift then first right shift the number by i places and then and it with 1 and if final result is 1 then it is set else NOT SET
    return (N >> i) & 1 == 1

    # TC: O(1)
    # SC: O(1)



new_block("check if ith bit is set or not")
number = 13
i = 2
print(f"Checking if {i}th bit of number {number} is set:", is_ith_set(number, i))

# Setting the ith bit
new_block("Set ith bit")
def set_ith_bit(N: int, i: int) -> int:
    return N | (1 << i) 
    # If the ith bit is already set then the result is same as number else we get different number

number = 13
i = 2
print(f"setting th {i}th bit of number {number} which results in :", set_ith_bit(number, i))

# Clearing the ith bit
new_block("Clearing ith bit")
def clear_ith_bit(N: int, i: int) -> int:
    return N & (~(1 << i)) 
    # If the ith bit is already set then the result is same as number else we get different number

number = 13
i = 2
print(f"clearing th {i}th bit of number {number} which results in :", clear_ith_bit(number, i))

# Toggling the ith bit
new_block("Clearing ith bit")
def toggle_ith_bit(N: int, i: int) -> int:
    return N ^ (1 << i) 
    # If the ith bit is set then unset it else set it

number = 13
i = 1
print(f"toggling th {i}th bit of number {number} which results in :", toggle_ith_bit(number, i))

# Getting the ith bit
new_block("Getting ith bit")

def get_ith_bit(N: int, i: int) -> int:
    # Shift the bits of N right by i positions, then use AND with 1 to get the i-th bit
    return (N >> i) & 1

# Example usage
number = 13
i = 2
print(f"The {i}th bit of number {number} is: {get_ith_bit(number, i)}")


# Remove the last set bit
new_block("Remove the last set bit")

def remove_last_set_bit(N: int) -> int:
    # The expression N & (N - 1) removes the last set bit from N.
    # When you subtract 1 from a number, all the bits after the last set bit (including the last set bit) are flipped.
    # Performing a bitwise AND with the original number clears the last set bit.
    return N & (N - 1)
    

# Example usage
number = 84
print(f"Removing the last set bit of number {number} results in: {remove_last_set_bit(number)}")

# Check if the number is power of 2 or not
new_block("Check if the number is power of 2 or not")

def check_power_of_2(N: int) -> bool:
    # A number is a power of 2 if it has exactly one bit set in its binary representation.
    # Therefore, N & (N - 1) should be 0 if N is a power of 2.
    # Also, N should be greater than 0.
    return N > 0 and (N & (N - 1)) == 0
    # LOGIC IS IF I REMOVE LAST SET BIT AND IF THE RESULT IS 0 THEN IT IS A POWER OF 2
    

# Example usage
number = 1
print(f"Checking if the number {number} is power of 2: {check_power_of_2(number)}")


# Count number of set bits
new_block("Count number of set bits")

def count_set_bits(N: int) -> bool:
    
    count = 0
    while N:
        count += N & 1
        N = N >> 1 # right shifting by 1 divides the number
    return count
    

# Example usage
number = 84
print(f"number of set bits in {number}:", count_set_bits(number))



