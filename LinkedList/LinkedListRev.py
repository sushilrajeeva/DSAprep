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

# 4. Search in a linked list

def element_in_linked_list(head: Node, search: int) -> bool:
    
    if not head:
        return False
    if search == "":
        return True
    
    current = head
    
    while current is not None:
        
        if current.value == search:
            return True
        
        current = current.next
        
    return False

search = 4

arr = [1, 4, 5, 7, 3, 5]

head = arr_to_LL(arr)

print(element_in_linked_list(head, search))

# 5. Delete head of linked list

def del_head(head: Node):
    
    if not head or not head.next:
        return None
    
    head.value = head.next.value
    head.next = head.next.next 
    
    return head

arr = [1, 4, 5, 7, 2]

head = arr_to_LL(arr)
print("Linked List before Deletion of head", print_linkedList(head))
print("Linked List after Deletion of head",print_linkedList(del_head(head)))