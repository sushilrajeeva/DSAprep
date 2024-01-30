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

# 5. Delete element at a given position in doubly linked list

def del_kth_element(head: DoublyLinkedListNode, k) -> DoublyLinkedListNode:
    
    if not head or k < 0: 
        return head
    
    current = head
    count = 0
    
    # Case 1: Delete the head
    if k == 0:
        # Case 2: If there is only one element return None
        if not head.next:
            return None
        # Proceed to delete the head
        head = head.next
        head.previous = None
        return head
    
    while current is not None:
        
        if count == k: break
        current = current.next
        count += 1
       
    # Case 5: My k is larger than length of doubly linked list 
    if k > count: 
        return head
        
    previous = current.previous
    next = current.next
    
    # Case 4: you are at the last node, so delete tail
    if next is None:
        # Logic for delete tail
        previous.next = next
        
        current.previous = None
        current.next = None
        return head
    
    # Case 5: my k is in middle
    previous.next = next
    next.previous = previous
    
    current.next = None
    current.previous = None
    
    return head
    

arr = [1, 2, 3, 4, 5, 6]
head = arr_to_doubly_linked_list(arr)
k = 2
print("Doubly Linked List before deleting element at position", k, ":", print_doubly_linked_list(head))
print("Doubly Linked List after deleting element at position", k, ":", print_doubly_linked_list(del_kth_element(head, k)))


# 6. Delete a given node of doubly linked list (never the head)

def del_node(node: DoublyLinkedListNode):
    
    # Case 1: If my node itself is None, then can't delete so just return
    if node is None: return
    
    previous = node.previous
    next = node.next
    
    # Case 2: If my node is the last node 
    if next is None:
        previous.next = None
        node.previous = None
        return
    
    # Case 2: my node is in middle of doubly linked list
    previous.next = next
    next.previous = previous
    
    node.previous = None
    node.next = None
    
    return
     
    

arr = [1, 2, 3, 4, 5, 6]
head = arr_to_doubly_linked_list(arr)
node = head.next.next.next
print("Doubly Linked List before deleting the node", node.value, ":", print_doubly_linked_list(head))
del_node(node)
print("Doubly Linked List after deleting the node", node.value, ":", print_doubly_linked_list(head))


# 7. Insert an element at the head / start of the doubly linked list

def insert_head(head: DoublyLinkedListNode, element: int) -> DoublyLinkedListNode:
    
    newHead = DoublyLinkedListNode(element, None, head)
    
    if head is not None:
        head.previous = newHead
    
    return newHead


        
arr = [1, 2, 3, 4, 5, 6]
head = arr_to_doubly_linked_list(arr)
element = 10
print("Doubly Linked List before inserting", element, "at the head:", print_doubly_linked_list(head))
print("Doubly Linked List after inserting", element, "at the head:", print_doubly_linked_list(insert_head(head, element)))  


# 7. Insert an element at the end / tail of the doubly linked list

def insert_tail(head: DoublyLinkedListNode, element: int) -> DoublyLinkedListNode:
    
    newNode = DoublyLinkedListNode(element)
    if not head:
        return newNode
    
    # Reach the end of the linked list
    
    current = head
    
    while current.next is not None:
        current = current.next
        
    current.next = newNode
    newNode.previous = current
    
    return head


        
arr = [1, 2, 3, 4, 5, 6]
head = arr_to_doubly_linked_list(arr)
element = 10
print("Doubly Linked List before inserting", element, "at the tail:", print_doubly_linked_list(head))
print("Doubly Linked List after inserting", element, "at the tail:", print_doubly_linked_list(insert_tail(head, element)))  


# 8. Insert an element before the end / tail of the doubly linked list

def insert_before_tail(head: DoublyLinkedListNode, element: int) -> DoublyLinkedListNode:
    
    newNode = DoublyLinkedListNode(element)
    if not head or not head.next:
        newNode.next = head
        if head is not None:
            head.previous = newNode
        return newNode
    
    # Reach the end of the linked list
    current = head
    
    while current.next.next is not None:
        current = current.next
        
    temp = current.next
    current.next = newNode
    newNode.previous = current
    newNode.next = temp
    temp.previous = newNode
    
    return head


        
arr = [1, 2, 3, 4, 5, 6]
head = arr_to_doubly_linked_list(arr)
element = 10
print("Doubly Linked List before inserting", element, "before the tail:", print_doubly_linked_list(head))
print("Doubly Linked List after inserting", element, "before the tail:", print_doubly_linked_list(insert_before_tail(head, element)))  



    