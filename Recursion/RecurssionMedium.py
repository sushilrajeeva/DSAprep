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

# Print all the unique subsequence of a given string

def print_unique_subsequence(string: str) -> None:
    
    index = 0
    unique = set()
    newString = ""
    
    def recursive(string: str, index: int, newString: str, unique: set) -> None:
        
        # Base Condition
        if index == len(string):
            unique.add(newString)
            return
        
        
        # Faith
        
        currentElement = string[index]
        
        # To Include
        recursive(string, index + 1, newString + currentElement, unique)
        
        # Not to include
        recursive(string, index + 1, newString, unique)
        
    recursive(string, index, newString, unique)
    
    print(unique)
    
print("Print all the unique subsequence of a given string")
string = "aaa"
print_unique_subsequence(string)

# Given an array create a new array that contains all the indexes of the element that is in given in given array

def all_indices(arr: list, key: int, index: int = 0, count: int = 0) -> list:
    
    if index == len(arr):
        return [0] * count
    
    
    if arr[index] == key:
        result = all_indices(arr, key, index + 1, count + 1)
        result[count] = index
        return result
        
    else:
        result = all_indices(arr, key, index + 1, count)
        return result
    
print("Given an array create a new array that contains all the indexes of the element that is in given in given array")
arr = [1, 2, 3, 3, 2, 2, 5, 6]
print(all_indices(arr, 2))





# Print all permutation of a given string

def string_permutation(string: str) -> None:
    
    permutationList = []
    
    def recursive(string, permutation: str = "") -> None:
        
        # Base Condition
        if len(string) == 0:
            permutationList.append(permutation)
            return
        
        # Work
        for i in range(len(string)):
            
            currentChar = string[i]
            newString = string[:i] + string[i+1:]
            recursive(newString, permutation + currentChar)
    recursive(string, "")
    
    print(permutationList)
            
            
print("Print all permutation of a given string")
string = "abc"
string_permutation(string)

            
        
# Print keypad combination with memory

def get_keypad_combinaiton(digits: str) -> list:
    
    if not digits:
        return []
    
    keypad = [".", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tu", "vwx", "yz"]
    result = []
    
    def recursive(index: int = 0, subString: str = "") -> None:
        
        if index == len(digits):
            if subString:
                result.append(subString)
            return
        
        
        # Work
        key = digits[index]
        keyword = keypad[int(key)]
        for char in keyword:
            recursive(index + 1, subString + char)
            
            
    recursive()
    return result
    
print("Print keypad combination")
string = "23"
print(get_keypad_combinaiton(string))


# Print keypad combination without storing in memory

def print_keypad_combinaiton(digits: str) -> list:
    
    if not digits:
        return []
    
    keypad = [".", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tu", "vwx", "yz"]
    
    def recursive(index: int = 0, subString: str = "") -> None:
        
        if index == len(digits):
            if subString:
                print(subString)
            return
        
        
        # Work
        key = digits[index]
        keyword = keypad[int(key)]
        for char in keyword:
            recursive(index + 1, subString + char)
            
            
    recursive()
    
print("Print keypad combination")
string = "23"
print_keypad_combinaiton(string)     
        