def reverseString(string):
    # What is the base case?
    if(string == ""):
        return ""
    
    # What is the smallest amount of work I can do in each iteration!
    return reverseString(string[1::]) + string[0]
    
    
string = "Hello World!"

print("Reverse of", string, "is", reverseString(string))

def isPalindrome(string)-> bool:
    
    if(len(string) == 0 or len(string) == 1):
        return True
    
    if string[0] == string[-1]:
        return isPalindrome(string[1:-1])
    
    return False

string = "racecar"
print("Is", string, "a palindrome? :", isPalindrome(string))
    
   
# Convert a number (Decimal to Binary)

def findBinary(decimal: int, result = ""):
    
    if(decimal == 0):
        return result
    
    result = str(decimal % 2) + result
    
    return findBinary(decimal // 2, result)

decimal = 100

print(decimal, "in binary format is :", findBinary(decimal))

# Sum of natural numbers

def sumOfNaturalNumbers(number: int) -> int:
    
    if number == 0:
        return number
    
    return number + sumOfNaturalNumbers(number-1)

num = 10
print("Sum of", num, "natural numbers is :", sumOfNaturalNumbers(num))

# Printing Triable with given number of rows (INVERTED RIGHT ANGLED TRIANGLE)
# ****
# ***
# **
# *

def invertedRightTriangle(row: int, column: int = 0):
    
    # Exit Condition
    if(row == 0):
        return
    
    if column < row:
        print("*", end="")
        invertedRightTriangle(row, column+1)
    else:
        print()
        invertedRightTriangle(row-1, 0)
 
height = 5       
print("Inverted Right Triangle with height", height, ":")
invertedRightTriangle(height)


# Printing Triable with given number of rows (Normal Right Angled TRIANGLE)
# *
# **
# ***
# ****

def rightTriangle(rows: int, current_row: int = 1):
    # Base condition to end recursion
    if rows < current_row:
        return

    # Print stars for the current row
    print('*' * current_row)

    # Recursive call for the next row
    rightTriangle(rows, current_row + 1)

height = 5
print("Right Triangle with height", height, ":")
rightTriangle(height)
