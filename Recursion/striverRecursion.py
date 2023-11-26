# Summation of N natural numbers

# Parameterized way

def summationParam(number: int, sum: int = 0) -> int:
    
    # Base Condition
    if(number < 1):
        return sum
    
    # Minimum work
    return summationParam(number=number-1, sum=sum+number)

number = 5
print("Param - Summation of", number, "natural numbers is :", summationParam(number))

def summationFunc(number: int) -> int:
    
    # Base Condition
    if(number == 0):
        return 0
    
    # Minimum work
    return number + summationFunc(number-1)
    

print("Func - Summation of", number, "natural numbers is :", summationFunc(number))


# Factorial of N

def fac(number: int) -> int:
    
    if(number == 1 or number == 0):
        return 1
    
    return number * fac(number-1)


num = 5

print("Factorial of", num, "is :", fac(num))

# Reverse an Array using recursion

# Input -> [1, 2, 3, 4]
# Output -> [4, 3, 2, 1]


def reverseArray(input: list, itr: int = 0) -> list:
    
    # Base Condition
    if(len(input)//2 == itr):
        return input
    
    # Minimum work
    complement = len(input) - itr - 1
    input[itr], input[complement] = input[complement], input[itr] # Swap
    return reverseArray(input, itr+1)

array = [1, 2, 3]
print("Given Array is :", array)
print("Reverse of Array is :", reverseArray(array))

# Palindrome using recursion

def isPalindrome(string: str, itr: int = 0) -> bool:
    
    if(len(string)//2 == itr):
        return True
    
    if(string[itr] != string[len(string) - itr - 1]): return False
    
    return isPalindrome(string, itr=itr+1)

string = "Hello"
print("Is", string, "a palindrome :", isPalindrome(string))