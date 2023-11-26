#Recursion:
# When a function calls itself until a specific condition is met is called Recursion

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


# Reversing a linked list

class Node:
    
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
        
# printing linkedlist using recursion

def print_nodes(head: Node):
    
    # Exit condition
    if(head.next is None):
        print(head.value)
        return 
    
    # Minimum work
    print(head.value, "-> ", end="")
    return print_nodes(head.next)
        

def reverseLinkedList(current: Node, previous: Node = None) -> Node:
    
    #Exit Condition
    if(current is None):
        return previous
    
    # saving the next node
    next = current.next
    
    current.next = previous
    
    return reverseLinkedList(next, current)


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')

a.next = b
b.next = c
c.next = d
d.next = e
    
print()
print("************ Reversing a Linked List ************")
print("Given Linked list: ")
print_nodes(a)
reversed_head = reverseLinkedList(a)
print("Reversed Linked list: ")
print_nodes(reversed_head)

# Merging two sorted Linked Lists

def mergeSortedList(A: Node, B: Node) -> Node:
    
    # Exit Condition
    if(A is None): return B
    if(B is None): return A
    
    # Minimum work
    if(A.value <= B.value):
        A.next = mergeSortedList(A.next, B)
        return A
    else:
        B.next = mergeSortedList(A, B.next)
        return B
        
    
    

        
a = Node(1)
b = Node(1)
c = Node(2)
d = Node(3)
e = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e      


x = Node(2)
y = Node(2)
z = Node(4)

x.next = y
y.next = z



print()
print("************ Merging two sorted Linked Lists ************")
print("Linked list A: ")
print_nodes(a)
print()
print("************ Merging two sorted Linked Lists ************")
print("Linked list B: ")
print_nodes(x)
print()
print("Sorted Linked List: ")
print_nodes(mergeSortedList(a,x))


# Print N to 1 using backtracking

def backTrack(n1: int, n2: int):
    
    if(n1 > n2):
        return
    
    backTrack(n1+1, n2)
    
    print(n1)
    
    
print("Printing N to 1 using Backtracking")
backTrack(1, 5)
    
