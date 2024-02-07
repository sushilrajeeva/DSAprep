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
        
        