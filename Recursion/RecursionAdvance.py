from typing import *

# Get all the stair paths given a number - valid steps are 1 , 2 and 3 only

def stair_path(n: int) -> List[str]:
    
    # Positive Base case: if n reach 0 steps then add "" and return
    if n == 0:
        return [""]
    
    # Negative base case: if n reach less than 0 then add empty array
    if n < 0:
        return [] 
    
    
    # Faith
    # path one will give me all the paths array after taking 1 step to destination
    paths1 = stair_path(n-1)
    paths2 = stair_path(n-2)
    paths3 = stair_path(n-3)
    paths = []
    
    # Expectation
    # I will add each paths to path but to its respective i will add 1, 2 or 3 corresponding to it before adding to path
    
    for path in paths1:
        paths.append("1" + path)
        
    for path in paths2:
        paths.append("2" + path)
        
    for path in paths3:
        paths.append("3" + path)
        
    return paths
        
n = 4   
print(f"All the possible valid paths for given number {n}")
print(stair_path(n))


# Count total paths in maze to move from (0, 0) to (n, m)

def count_maze(n: int, m: int) -> None:
    
    def recursive(i: int = 0, j: int = 0) -> int:
        
        # Base Condition
        if i == n or j == m:
            return 0
        
        if i == n - 1 and j == m - 1:
            return 1
        
        
        # Faith
        # Move down
        downPaths = recursive(i+1, j)
        
        # Move right
        rightPaths = recursive(i, j+1)
        
        return downPaths + rightPaths
    
    result = recursive()
    print(result)

n, m = 3, 3
print(f"Count total paths in maze to move from (0, 0) to ({n}, {m})")

count_maze(n, m)


# Get all the paths to the maze

def get_maze_paths(n: int, m: int, i: int = 0, j: int = 0) -> List[str]:
    
    # Base Condition
    if i == n or j == m:
        return []
    
    if i == n - 1 and j == m - 1:
        return [""]
    
    
    
    # Faith
    rightPaths = get_maze_paths(n, m, i, j + 1)
    downPaths = get_maze_paths(n, m, i + 1, j)
    
    paths = []
    
    for path in rightPaths:
        paths.append("R" + path)
        
    for path in downPaths:
        paths.append("D" + path)
        
    return paths

n, m = 3, 3
print("Get all the paths to the maze of dimension {n} x {m}")
print(get_maze_paths(n, m))





    
        
        