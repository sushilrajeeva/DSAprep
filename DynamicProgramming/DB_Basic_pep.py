from typing import *
# This is the stair path problem
# You are at a stair and you have 3 options, either to move one step or two or three
# Count and return all the possible ways you can use to go from n to 0

def get_stair_path_ways(steps: int, memory: dict = {}) -> int:
    
    # Base case / Exit Condition
    if steps == 0:
        return 1
    elif steps < 0:
        return 0
    
    if memory.get(steps, 0) > 0:
        return memory[steps]
    
    # Faith - basic work
    n1 = get_stair_path_ways(steps - 1, memory)
    n2 = get_stair_path_ways(steps - 2, memory)
    n3 = get_stair_path_ways(steps - 3, memory)
    number_of_paths = n1 + n2 + n3
    # Saving this in my memory
    memory[steps] = number_of_paths

    return number_of_paths

n = 10
print(f"Number of ways to get from {n} to 0 is:", get_stair_path_ways(n))