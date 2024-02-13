from typing import *

# Get all the stair paths given a number - valid steps are 1 , 2 and 3 only

def get_stair_path(n: int) -> List[str]:
    
    # Positive Base case: if n reach 0 steps then add "" and return
    if n == 0:
        return [""]
    
    # Negative base case: if n reach less than 0 then add empty array
    if n < 0:
        return [] 
    
    
    # Faith
    # path one will give me all the paths array after taking 1 step to destination
    paths1 = get_stair_path(n-1)
    paths2 = get_stair_path(n-2)
    paths3 = get_stair_path(n-3)
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
print(get_stair_path(n))


# Print all the stair paths given a number - valid steps are 1 , 2 and 3 only without storing it
def print_stair_path(n: int, path: str = "") -> List[str]:
    
    # Positive Base case: if n reach 0 steps then add "" and return
    if n == 0:
        print(path)
        return
    
    # Negative base case: if n reach less than 0 then add empty array
    if n < 0:
        return
    
    
    # Faith
    # path one will give me all the paths array after taking 1 step to destination, similarly i will do for 2 and 3.
    print_stair_path(n-1, path + "1")
    print_stair_path(n-2, path + "2")
    print_stair_path(n-3, path + "3")
        
n = 4   
print(f"Print all the possible valid paths for given number {n} without using space")
print_stair_path(n)


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


# Get all the paths to the maze with jump

def get_maze_paths_jump(n: int, m: int, i: int = 0, j: int = 0) -> List[str]:
    
    # Base Condition
    if i == n or j == m:
        return []
    
    if i == n - 1 and j == m - 1:
        return [""]
    
    paths = []
    # Right Moves
    for r in range(1, m - j + 1):
        rightPaths = get_maze_paths_jump(n, m , i, j + r)
        for path in rightPaths:
            paths.append("R" + str(r) + path)
    
    # Down Moves
    for d in range(1, n - i + 1):
        downPaths = get_maze_paths_jump(n, m, i + d, j)
        for path in downPaths:
            paths.append("D" + str(d) + path)
            
    return paths


n, m = 3, 3
print("Get all the paths to the maze with jump of dimension {n} x {m}")
print(get_maze_paths_jump(n, m))

# Without storing just print all the subsequence

def print_subsequence(string: str)-> None:
    
    index = 0
    newString = ""
    
    def recursive(string: str, index: int, newString: str) -> list:
        
        if index == len(string):
            #subsequence.append(newString)
            print(newString)
            return
        
        
        # Faith
        currentElement = string[index]
        
        # to be included
        recursive(string, index + 1,newString + currentElement)
        
        # not to be included
        recursive(string, index + 1, newString)
        
    recursive(string, index, newString)
    
print("Print all the sub sequence of a given string")
string = "abc"
print_subsequence(string)


# Flood Fill ()
        
# You are only allowed to go top down left and right and if there is a 1 (obstacle) you can't go there if there is 0 you can go there
# so traverse through a n*m matrix


def floodFill(maze: List[List[int]], row: int, col: int, path: str, visited: List[List[bool]]):
    
    # Exit Condition
    if row < 0 or col < 0 or row == len(maze) or col == len(maze[0]) or maze[row][col] == 1 or visited[row][col] == True:
        return
    
    # Print condition
    if row == len(maze) - 1 and col == len(maze[0]) - 1:
        print(path)
        return
    
    visited[row][col] = True
    # Top
    floodFill(maze, row - 1, col, path + "T", visited)
    # Left
    floodFill(maze, row, col - 1, path + "L", visited)
    # Right
    floodFill(maze, row, col + 1, path + "R", visited)
    # Down
    floodFill(maze, row + 1, col, path + "D", visited)
    
    #Reset visited
    visited[row][col] = False
    
    
n = 4
m = 3
visited = [[False for _ in range(m)] for _ in range(n)]
maze = [
    [0, 1, 1],
    [0, 0, 1],
    [1, 0, 0],
    [0, 1, 0]
]
print(f" Flood Fill of matrix {n}x{m} = {maze}")
floodFill(maze, 0, 0, "", visited)

    
        
        