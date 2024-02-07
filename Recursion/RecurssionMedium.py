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

# Move all 'x' to the end of the string

def move_all_key_to_end(string: str, key: string) -> str:
    
    newString = ""
    index, count = 0, 0
    
    def recursive(string: str, key: str, index: int, count: int, newString: str) -> str:
        
        # Base Condition
        if len(string) == index:
            return newString + key*count
        
        # Faith
        if string[index] == key:
            count += 1
        else:
            newString += string[index]
        
        return recursive(string, key, index + 1, count, newString)
    
    return recursive(string, key, index, count, newString)

print("Move all key char to the end of the string")
string = "axbcxxd"
key = "x"
print(move_all_key_to_end(string, key))


# Remove duplicates from the string

def remove_duplicates(string: str) -> str:
    
    freqArr = [0] * 26
    index = 0
    newString = ""
    
    def recursive(string: str, index: int, freqArr: list, newString: str) -> str:
        
        if len(string) == index:
            return newString
        
        # Faith
        freqArr[ord(string[index]) - 97] += 1
        if freqArr[ord(string[index]) - 97] == 1:
            newString += string[index]
            
        return recursive(string, index + 1, freqArr, newString)
    
    return recursive(string, index, freqArr, newString)

print("Remove duplicates in a given string")
string = "abbccda"

print(remove_duplicates(string))

# Print all the subsequences of a given string

def print_subsequence(string: str)-> None:
    
    index = 0
    subsequence = []
    newString = ""
    
    def recursive(string: str, index: int, subsequence: list, newString: str) -> list:
        
        if index == len(string):
            subsequence.append(newString)
            return
        
        
        # Faith
        currentElement = string[index]
        
        # to be included
        recursive(string, index + 1, subsequence, newString + currentElement)
        
        # not to be included
        recursive(string, index + 1, subsequence, newString)
        
    recursive(string, index, subsequence, newString)
        
    print(subsequence)
    
print("Print all the sub sequence of a given string")
string = "abc"
print_subsequence(string)
            
        