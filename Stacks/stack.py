# Stack -> Last In First Out [LIFO]

# Stack using Linked List
from typing import *

class Node:

    def __init__(self, value: int = 0, next: Optional['Node'] = None):
        self.value = value
        self.next = next

class Stack:

    # By default head is Null
    def __init__(self):
        self.head = None

    # Check if the stack is empty or not
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    
    # Method to add data to stack 
    # Adds to the start of the stack
    def push(self, data):

        if self.head is None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
        
    # Remove element that is the current ehad (top of the stack)
    def pop(self):
        if self.isEmpty():
            return None
        
        # Remove the head and makes the precediing one as the new head
        poppedNode = self.head
        self.head = self.head.next

        # Removing the connection of popped node
        poppedNode.next = None
        return poppedNode.value
    
    # Return the head node data
    def peek(self):

        if self.isEmpty():
            return None
        return self.head.value
    
    # Prints out the stack
    def display(self):
        current = self.head
        if self.isEmpty():
            print("Stack Underflow")
            return
        
        while current:
            print(current.value, end="")
            current = current.next
            if current:
                print("->", end="")
        return

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

# Push at bottom 

def pushAtBottom(data: int, stack: Stack) -> None:

    if stack.isEmpty():
        stack.push(data)
        return

    top = stack.pop()
    pushAtBottom(data, stack)
    stack.push(top)

print("Add 100 at the bottom of the given stack: ", end="")
stack.display()
print("After adding 100 at the bottom, new stack is :", end="")
pushAtBottom(100, stack)
stack.display()
print()

# Reversing a Stack

def reverseStack(stack: Stack) -> None:

    if stack.isEmpty():
        return
    top = stack.pop()
    reverseStack(stack)
    pushAtBottom(top, stack)

print("Current Stack :", end="")
stack.display()
print()
print("Stack after reversing: ", end="")
reverseStack(stack)
stack.display()
print()


        
    


