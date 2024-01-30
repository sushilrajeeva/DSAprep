from typing import *

class Node:
    
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next
        

# 1.  Convert Array to Linked List
def arr_to_LL(arr: list) -> Node:
    
    if not arr:
        return None
    
    head = Node(arr[0])
    current = head
    for i in range(1, len(arr)):
        temp = Node(arr[i])
        current.next = temp
        current = current.next
        
    return head

# 2. Print all elements of linkedlist -> traversal
def print_linkedList(head: Node):
    
    current = head
    
    nodes = ""
    while current != None:
        nodes += str(current.value)
        
        if current.next != None:
            nodes += "->"
        current = current.next
            
    return nodes

# Printing result
arr = [1, 2, 3, 4]
head = arr_to_LL(arr)
print(print_linkedList(head))

# 3. Length of a linked list

def len_linked_list(head: Node):
    
    if head is None:
        return 0
    
    length = 0
    current = head
    
    while current is not None:
        length += 1
        current = current.next
        
    return length

print("Length of the above linked list is: ",len_linked_list(head))