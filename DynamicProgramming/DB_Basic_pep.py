from typing import *
# This is the stair path problem
# You are at a stair and you have 3 options, either to move one step or two or three
# Count and return all the possible ways you can use to go from n to 0
# Using recursion
def get_stair_path_ways(steps: int, dp: List[int] = None) -> int:
    
    # Base case / Exit Condition
    if dp is None:
        dp = [0] * (n+1)

    if steps == 0:
        return 1
    elif steps < 0:
        return 0
    
    if dp[steps] > 0:
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