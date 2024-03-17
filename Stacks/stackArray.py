# Stack -> Last In First Out [LIFO]

# Stack using Array List
from typing import *

class Stack:

    def __init__(self):
        self.stack = []

    # Check if the stack is empty or not
    def isEmpty(self):
        return len(self.stack) == 0
    
    # Method to add data to the stack
    def push(self, data):
        self.stack.append(data)

    # Remove and return the top element of the stack
    def pop(self):
        if self.isEmpty():
            return None  # Or raise an exception, depending on your preference
        return self.stack.pop()

    # Return the top element of the stack without removing it
    def peek(self):
        if self.isEmpty():
            return None  # Or raise an exception, depending on your preference
        return self.stack[-1]
    
    # Prints out the stack
    def display(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            for i in range(len(self.stack) - 1, -1, -1):
                print(self.stack[i], end="")
                if i > 0:
                    print("->", end="")
            print()


input = [11, 22, 33, 44]   
print(f"Printing the given input {input} as stack")
stack = Stack()
for ele in input:
    stack.push(ele)
print("Displaying Stack : ", end="")
stack.display()
print()

print("Is Stack empty? :", stack.isEmpty())

print("Top Element of stack :", stack.peek())

print("Deleting top two elements")
stack.pop()
stack.pop()
print("After popping two elements , new stack :", end="")
stack.display()
print()
