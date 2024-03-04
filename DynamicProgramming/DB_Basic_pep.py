from typing import *
# This is the stair path problem
# You are at a stair and you have 3 options, either to move one step or two or three
# Count and return all the possible ways you can use to go from n to 0
# Using recursion
def get_stair_path_ways(steps: int, dp: List[int] = None) -> int:
    
    # Base case / Exit Condition
    if dp is None:
        dp = [-1] * (n+1)

    if steps == 0:
        return 1
    elif steps < 0:
        return 0
    
    if dp[steps] != -1:
        return dp[steps]
    
    # Faith - basic work
    n1 = get_stair_path_ways(steps - 1, dp)
    n2 = get_stair_path_ways(steps - 2, dp)
    n3 = get_stair_path_ways(steps - 3, dp)
    number_of_paths = n1 + n2 + n3
    # Saving this in my memory
    dp[steps] = number_of_paths

    return number_of_paths

n = 18
print(f"Number of ways to get from {n} to 0 is:", get_stair_path_ways(n))

# Using tabulation to solve using itration dp
def get_stair_path_ways_tabulation(steps: int) -> int:

    # Step 1: create a dp array of size n+1
    dp = [0] * (steps + 1)
    # Step 2: initialize the first base case value
    dp[0] = 1

    # Step 3: itterate through the steps from 1, to n and then add the previous 3 steps
    for i in range(1, steps + 1):
        if i == 1:
            dp[i] = dp[i - 1]
        elif i == 2:
            dp[i] = dp[i - 1] + dp[i - 2]
        else:
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[-1]
        



n = 6
print(f"Tabulation : Number of ways to get from {n} to 0 is:", get_stair_path_ways_tabulation(n))

# Calculate fibbonaci
# Using memoization
def fib_with_mem(n: int, dp: List[int] = None) -> int:

    if dp is None:
        dp = [-1] * (n + 1)

    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = fib_with_mem(n - 1, dp) + fib_with_mem(n - 2, dp)

    return dp[n]


# Calculate fibbonaci
# Using Tabulation
def fib_with_tab(n: int) -> int:
    
    dp = [-1] * (n + 1)
    
    if n == 0:
        return 0
    
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[-1]


# Calculate fibbonaci
# Using Tabulation Optimized space
# To note i only care about current, and previous and previous's previous variable
def fib_with_tab_optimized(n: int) -> int:
    
    
    if n == 0:
        return 0
    
    if n == 1 or n == 2:
        return 1
    
    previous1 = 1
    previous2 = 0
    

    for i in range(2, n + 1):
        calculation = previous1 + previous2
        previous2 = previous1
        previous1 = calculation

    return previous1

n = 6
print(f"Memoization : Calculate {n}th fibbonaci", fib_with_mem(n))
print(f"Tabulation : Calculate {n}th fibbonaci", fib_with_tab(n))
print(f"Optimized Tabulation : Calculate {n}th fibbonaci", fib_with_tab_optimized(n))

# Maximum sum of non-adjacent elements
# Problem statement
# You are given an array/list of ‘N’ integers. You are supposed to return the maximum sum of the subsequence with the constraint that no two elements are adjacent in the given array/list.

# Note:
# A subsequence of an array/list is obtained by deleting some number of elements (can be zero) from the array/list, leaving the remaining elements in their original order.

# Link: https://www.codingninjas.com/studio/problems/maximum-sum-of-non-adjacent-elements_843261?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

# Using memoization technique
def f_memoization(nums: List[int], n: int = None, dp: List[int] = None) -> int:    
    # Write your code here.
    if dp is None:
        dp = [-1] * (len(nums) + 1)
    if n is None:
        n = len(nums) - 1

    if n == 0: return nums[n]
    if n < 0: return 0

    if dp[n] != -1: return dp[n]

    pick = nums[n] + f_memoization(nums, n-2, dp)
    no_pick = f_memoization(nums, n-1, dp)

    sol = max(pick, no_pick)
    dp[n] = sol
    return dp[n]

# Using Tabulation technique
def f_tab(nums: List[int], dp: List[int] = None) -> int:

    # Initialization
    n = len(nums)
    if dp is None:
        dp = [-1 for _ in range(n)]

    dp[0] = nums[0]

    for i in range(1, n):
        pick = nums[i]
        if i > 1:
            pick += dp[i-2]
        no_pick = dp[i-1]

        dp[i] = max(pick, no_pick)

    return dp[n-1]

# Using optimal tabulization technique
def f_tab_optimal(nums: List[int]) -> int:

    n = len(nums)
    if n == 0: return 0
    if n == 1: return nums[0]
    
    
    prev1 = nums[0]
    prev2 = 0

    for i in range(1, n):
        pick = nums[i]
        if i>1:
            pick += prev2
        no_pick = prev1

        prev2 = prev1
        prev1 = max(pick, no_pick)

    return prev1




    

def maximumNonAdjacentSum(nums) -> int:
    #return f_memoization(nums)
    #return f_tab(nums)
    return f_tab_optimal(nums)

nums = [2, 1, 4, 9]
print(f"Computing the max non adjascent sum for the given Array: {nums}")
print(f"Max nonadjascent sum = {maximumNonAdjacentSum(nums)}")
