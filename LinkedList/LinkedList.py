class Node:
    #A node structure contains a constructor
    #Constructor takes a value
    #by default when a node is created, it's value is set and the next pointer is set to None;
       
    def __init__(self, value):
        self.value = value
        self.next = None
    
    
#Creating 4 node points        
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

#Connecting each node

# a will be my head and d will be tail
a.next = b
b.next = c
c.next = d

# Now the nodes looks like A -> B -> C -> D -> None 
#when a node points to None that means it is the tail node.

#Writing a function to print linked list (the nodes)

# Problem 1: Print singly linked list elements

# def print_nodes(head: Node):
    
#     #initially my current position of the node should be my head node so i am setting it here
#     current = head
    
#     #I know that the last element points to a None, so until my head is None i have to iterate all the nodes using Node.next
    
#     nodes = ""
    
#     #Note : Use '!=' when you want to determine if two objects have different values.
#     #       Use 'is not' when you want to determine if two variables refer to different objects in memory.
#     while(current is not None):
        
#         nodes += current.value
        
#         if(current.next is not None):
#             nodes += " -> "
    
#         current = current.next
        
#     print(nodes)
 

#Doing the same with recursion 

def print_nodes(node: Node):
    
    #For recursion we have to first start with writing the exit condition
    #In our case exit condition is when node (current node) is None
    
    if(node is None):
        return
    
    #Printing the current node value
    print(node.value, end = '')
    
    #Logic to add '->' at the end
    if(node.next is not None):
        print(" -> ", end = '')
    else:
        print()
    
    # Calling the same function recursively until the end condition is met
    print_nodes(node.next)
    

#Printing the nodes by giving the head node to the print function     
print("Printing the values of the Singly Linked List") 
print_nodes(a)

# Problem 2: Given a singly linked list as input, return a list containing elements of the singly linked list in the same order as they are present in SLL.

# def SinglyLinkedList_To_List(head: Node) -> list:
    
#     LL_list = []
#     current = head
#     # Iterrating over the linked list given the head and appending it to the list
    
#     while(current is not None):
#         LL_list.append(current.value)
#         current = current.next 
        
#     return LL_list

#     # Time: O(n)
#     # Space: O(n)

#Doing it in Recursion

def SinglyLinkedList_To_List(head: Node) -> list:
    
    LL_list = []
    
    fillList(head, LL_list)
    
    return LL_list

    # Time: O(n)
    # Space: O(n)


def fillList(node: Node, values: list):
    
    if(node is None):
        return
    
    values.append(node.value)
    fillList(node.next, values)
    

print()
print("Singly Linked List to List with same order : ")
print(SinglyLinkedList_To_List(a))

#Problem 3: Sum List

#Given a linked list of numbers, itterate through each node and get the sum of all the node values.

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

# Iterative approach
# def getLinkedListSum(head: Node) -> int:
    
#     current = head
#     sum = 0
#     while(current is not None):
#         sum += current.value
#         current = current.next
        
#     return sum

#     # Time: O(n)
#     # Space: O(1)


#Recursion approach
def getLinkedListSum(head: Node) -> int:
    
    #Writing my exit condition
    if(head is None): return 0
    
    return head.value + getLinkedListSum(head.next)
    
    # Time: O(n)
    # Space: O(n)
    
print()
print_nodes(a)
print("Sum of the above Singly Linked List of numbers is: ")
print(getLinkedListSum(a))

#Problem 4: 
# Given a linked list, find if a target value is present or not

target = "K"

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')

a.next = b
b.next = c
c.next = d
d.next = e

#Iterative approach
# def target_found(head: Node, target) -> bool:
    
#     current = head
#     found = False
#     while(current is not None):
#         if current.value == target:
#             return True
#         current = current.next
        
#     return found

#     # Time: O(n)
#     # Space: O(1)

#

#Recursion approach
def target_found(node: Node, target) -> bool:
    
    #Exit Conditions
    if(node is None): return False 
    if(node.value == target): return True
    
    return target_found(node.next, target)


    # Time: O(n)
    #Space: O(n)

print()
print_nodes(a)
print("Target ", target, " is present in Singly Linked List: ", target_found(a, target))


# Problem 5: Getting the value of a singly linked list node value at a perticular index

# Iterative approach
# def get_index_value(head: Node, index: int):
    
#     current = head
#     count = 0
#     while(current is not None):
#         if(count == index): 
#             return current.value

#         current = current.next
#         count+=1
        
#     return "Index out of Bound"

#     # Time: O(n)
#     # Space: O(1)


# Recursion approach
def get_index_value(node: Node, index: int):
    
    if index == 0: return node.value
    if (node is None): return "Index out of bound"
    
    return get_index_value(node.next, index-1)
    
    # Time: O(n)
    # Space: O(n)

print()
print_nodes(a)
index = 3
print("Value of node at index ", index, " is: ", get_index_value(a, index))

