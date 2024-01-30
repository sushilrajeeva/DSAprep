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
        
    
    