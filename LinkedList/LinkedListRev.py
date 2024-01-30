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
def print_linkedList(head: Node) -> str:
    
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

def len_linked_list(head: Node) -> int:
    
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

def del_head(head: Node) -> Node:
    
    if not head or not head.next:
        return None
    
    head.value = head.next.value
    head.next = head.next.next 
    
    return head

arr = [1, 4, 5, 7, 2]

head = arr_to_LL(arr)
print("Linked List before Deletion of head", print_linkedList(head))
print("Linked List after Deletion of head",print_linkedList(del_head(head)))

# 6. Delete tail of linked list

def del_tail(head: Node) -> Node:
    
    if not head or not head.next:
        return None
    
    current = head
    
    while current.next.next is not None:
        # This logic will make my current point to the second last element of the node after while ends
        current = current.next
    
    # to delete last i have to point my current (second last element) next to None
    current.next = None
    
    return head

arr = [1, 4, 5, 7, 2]

head = arr_to_LL(arr)
print("Linked List before Deletion of tail", print_linkedList(head))
print("Linked List after Deletion of tail",print_linkedList(del_tail(head)))

# 7. Deleting a k'th element/node of the linked list

def del_kth_ele(head: Node, k: int):
    
    # If the list is empty or k is invalid (as k can't be less than 0)
    if not head or k < 0: return head
    
    # If the head needs to be deleted
    if k == 0:
        return head.next
    
    current = head
    
    # for _ in range(1, k):  # Move to the node just before the k'th node
    #     if current.next is None:  # If we reach the end before k, return the head
    #         return head
    #     # This logic will point my current to just one node before the deletion node
    #     current = current.next
            
    # if current.next:
    #     current.next = current.next.next
    
    # return head
    
    # Simple logic
    previous = None
    count = 0
    
    while current is not None:
        
        if count == k:
            previous.next = current.next 
            break
    
        previous = current
        current = current.next
        
        count += 1
            
    return head
            
            
arr = [1, 4, 5, 7, 2]
k = 2
head = arr_to_LL(arr)
print("Linked List before Deletion of", k,"th ele:", print_linkedList(head))
print("Linked List after Deletion of", k,"th ele:", print_linkedList(del_kth_ele(head, k)))

# 8. Delete the node of a linked list given a value

def del_node(head: Node, val: int) -> Node:
    
    if head is None: return head
    
    if head.value == val:
        head = head.next
        return head
    
    previous, current = None, head
    
    while current is not None:
        
        if current.value == val:
            previous.next = current.next
            break
        
        previous = current
        current = current.next
        
    return head
        
arr = [1, 4, 5, 7, 2]
del_val = 4
head = arr_to_LL(arr)
print("Linked List before Deletion of", del_val,":", print_linkedList(head))
print("Linked List after Deletion of", del_val,":", print_linkedList(del_node(head, del_val)))


# 9. Insert an element at the head of the linked list

def insert_head(head: Node, element: int) -> Node:
    
    return Node(element, head)

arr = [1, 4, 5, 7, 2]
ele = 4
head = arr_to_LL(arr)
print("Linked List before Insertion of", ele," in head:", print_linkedList(head))
print("Linked List after Insertion of", ele," in head:", print_linkedList(insert_head(head, ele)))


# 10. Insert an element at the tail of the linked list

def insert_tail(head: Node, element: int) -> Node:
    
    new_node = Node(element)
    
    if head is None: return new_node
    
    current= head
    
    while current.next is not None:
        # This will make my current point to the last Node of the linked list
        current = current.next
      
    current.next = new_node
          
    return head

arr = [1, 4, 5, 7, 2]
ele = 4
head = arr_to_LL(arr)
print("Linked List before Insertion of", ele,"in tail:", print_linkedList(head))
print("Linked List after Insertion of", ele,"in tail:", print_linkedList(insert_tail(head, ele)))