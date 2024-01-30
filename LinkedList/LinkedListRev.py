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
    