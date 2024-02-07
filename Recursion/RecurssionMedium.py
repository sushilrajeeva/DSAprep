# Reverse a given string using recursion
def reverse_string(string: str) -> None:
    
    n = len(string)
    
    if n == 0:
        return ""
    
    
    # Faith
    return reverse_string(string[1:]) + string[0]

print("Reverse a string using recursion")
string = "sushil"
print(reverse_string(string))

# Find the first and last occurance of an element in a string
def first_and_last(string: str, key: str) -> list:
    
    first, last, index = -1, -1, 0
    
    def recursive(string: str, key: str, index: int, first: int, last: int) -> list:
        
        if index == len(string) - 1:
            return [first, last]
        
        if string[index] == key:
            if first == -1:
                first = index
            else:
                last = index
        
        return recursive(string, key, index+1, first, last)
    
    return recursive(string, key, index, first, last)

print("Printing first and last occurance of a key in a string")
key = "a"
string = "abaacdaefaah"
print(first_and_last(string, key))

# Check if an array is sorted (strictly increasing)


def isSorted(arr: list) -> bool:
    
    # Base Case
    if len(arr) <= 1:
        return True
    
    # Work
    if not (arr[1] > arr[0]):
        return False
    # Faith
    return isSorted(arr[1:])
        
print("Checking if the array is strictly sorted or not")
arr = [1, 2, 3, 4, 4]
print(isSorted(arr))
                
            
        