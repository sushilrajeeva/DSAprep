# Divide problem into several smaller sub-problems
# Normally, the sub-problems are smaller to the original

# Conquer the subprobelms by solving them recursively
# Base cae: solve small enough problems by brute force

# Combine the solutions to get a solution to the sub-problems
# and finally a solution to the original problem

# Divide and Conquer algorithms are normally recursive

def binarySearch(array: list,find: int, left: int, right: int ):
    
    # Exit condition
    if(left > right):
        return -1
    
    mid = (left + right) // 2
    
    if(array[mid] == find):
        return mid
    
    # Divide and Conquer
    if(find < array[mid]):
        return binarySearch(array, find, left = left, right = mid-1)
    
    return binarySearch(array, find, left = mid + 1, right = right)

    # Time: O(log n)
    # Space: O(log n)
    
    
    
array = [-1, 0, 1, 2, 3, 4, 7, 9, 10, 20]
find = 10
print("In the given list", array, ",", find, "is found in Index :", binarySearch(array, find, 0, len(array)-1))

# Fibonacci sequence (Un-optimized way)

def fib(number: int) -> int:
    
    # Exit Condition
    if(number == 0 or number == 1):
        return number
    
    return fib(number - 1) + fib(number - 2)

    # Time: O(2^n)
    # Space: O(n)

number = 5
print("Fib of", number, "is :", fib(number))

# Checkout recursion of sorting algorithms inside sorting folder