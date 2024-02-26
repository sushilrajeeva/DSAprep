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

n = 6
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