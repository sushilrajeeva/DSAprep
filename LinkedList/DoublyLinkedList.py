from typing import *

class DoublyLinkedListNode:
    
    def __init__(self, value = 0, previous = None, next = None):
        self.value = value
        self.previous = previous
        self.next = next
        
        
# 1. Convert Array to Doubly Linked List

def arr_to_doubly_linked_list(arr: List[int]) -> DoublyLinkedListNode:
    
    if not arr:
        return None
    
    head = DoublyLinkedListNode(arr[0])
    previous = head
    
    for value in arr[1:]:
        current = DoublyLinkedListNode(value, previous)
        previous.next = current
        
        # Traversing forward
        previous = previous.next
        
    return head

# 2. Print doubly linked list

def print_doubly_linked_list(head: DoublyLinkedListNode) -> str:
    nodes = []
    current = head
    while current:
        nodes.append(str(current.value))
        current = current.next
    return " <--> ".join(nodes)

arr = [1, 2, 3, 4, 5]

head = arr_to_doubly_linked_list(arr)

print("Initial Array:", arr)
print("After converting array to Doubly Linked List:", print_doubly_linked_list(head))


# 3. Delete element at the start/head of doubly linked list

def del_head(head: DoublyLinkedListNode) -> DoublyLinkedListNode:
    
    if not head or not head.next: 
        return None
    
    previous = head
    head = head.next # The second node becomes the new head
    head.previous = None # Disconnect the new head's previous link
    previous.next = None # Clean up the old head's next link
    
    
    return head

arr = [1, 2, 3, 4, 5, 6]
head = arr_to_doubly_linked_list(arr)
print("Doubly Linked List before deleting head:", print_doubly_linked_list(head))
print("Doubly Linked List after deleting head:", print_doubly_linked_list(del_head(head)))


# 4. Delete element at the tail/end of doubly linked list

def del_tail(head: DoublyLinkedListNode) -> DoublyLinkedListNode:
    
    if not head or not head.next: 
        return None
    
    current = head
    
    while current.next is not None:
        # This will make my current point to the last element
        current = current.next
        
    previous = current.previous
    
    previous.next = None
    current.previous = None
    
    return head
        

arr = [1, 2, 3, 4, 5, 6]
head = arr_to_doubly_linked_list(arr)
print("Doubly Linked List before deleting tail:", print_doubly_linked_list(head))
print("Doubly Linked List after deleting tail:", print_doubly_linked_list(del_tail(head)))



        
    
    