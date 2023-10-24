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
print("************ Converting Linked List to ArrayList ************")
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
print("************ Sum of all Linked List elements ************")
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
print("************ Find an element in Linked List ************")
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
print("************ Getting value of a Linked List element at a certian Index ************")
print_nodes(a)
index = 3
print("Value of node at index ", index, " is: ", get_index_value(a, index))


# Problem 6: 
# Reverese a linked list

# A -> B -> C -> D -> E -> None after reverse E -> D -> C -> B -> A -> None

#Iterative Approach

def reverseLinkedList(head: Node) -> Node:
    
    previous = None  # Initialize previous pointer to None
    current = head   # Start with the head node
    
    while(current is not None):
        
        next = current.next  # Temporarily store the next node
        
        current.next = previous  # Reverse the current node's pointer
        
        previous = current  # Move the previous pointer forward
        current = next      # Move the current pointer forward
    
    # At the end, previous points to the new head of the reversed list
    return previous

    # Time: O(n)
    # Space: O(1)


# Recursion Approach

# def reverseLinkedList(current: Node, previous=None) -> Node:
    
#     # Base case: If we've reached the end of the list, return the last node
#     if current is None:
#         return previous
    
#     # Save the next node before overwriting current's next pointer
#     next = current.next
    
#     # Reverse the current node's pointer
#     current.next = previous
    
#     # Recursive call with the next node and the current node as the new "previous"
#     return reverseLinkedList(next, current)

#     # Time: O(n)
#     # Space: O(n)

    
    

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')

a.next = b
b.next = c
c.next = d
d.next = e
    
print()
print("************ Reversing a Linked List ************")
print("Given Linked list: ")
print_nodes(a)
reversed_head = reverseLinkedList(a)
print("Reversed Linked list: ")
print_nodes(reversed_head)

# Problem 7 (Zipper)

#Given two linked lists, insert nodes of second list into first list at alternate positions of first list. 


# For example, if first list is 5->7->17->13->11 and second is 12->10->2->4->6, the first list should become 5->12->7->10->17->2->13->4->11->6 and second list should become empty. 
# The nodes of second list should only be inserted when there are positions available. 
# For example, if the first list is 1->2->3 and second list is 4->5->6->7->8, then first list should become 1->4->2->5->3->6 and second list to 7->8.

def zipper_linked_list(head1: Node, head2: Node) -> Node:
    
    tail = head1
    current1 = head1.next
    current2 = head2
    counter = 0
    
    # Loop until one of the linked lists ends
    while(current1 is not None and current2 is not None):
        
        if(counter % 2 == 0): 
            # Append node from the second list
            tail.next = current2
            current2 = current2.next
        else:
            # Append node from the first list
            tail.next = current1
            current1 = current1.next
        
        # Update the tail reference and counter
        tail = tail.next
        counter += 1
            
    # Attach remaining nodes, if any
    if(current1 is not None): tail.next = current1
    if(current2 is not None): tail.next = current2
        
    return head1

    # Time: O(n)
    # Space: O(1)

            
            
        
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')

a.next = b
b.next = c
c.next = d
d.next = e


p = Node('1')
q = Node('2')
r = Node('3')
s = Node('4')
t = Node('5')
u = Node('6')
v = Node('7')

p.next = q
q.next = r
r.next = s
s.next = t
t.next = u
u.next = v
    
print()
print("************ Zipping Two Lists ************")
print("Given Linked list1: ")
print_nodes(a)

print()
print("Given Linked list2: ")
print_nodes(p)

print()
print("Zipping two list: ")
print_nodes(zipper_linked_list(a, p))


        
        
# problem 8: (Slow and Fast pointer method)
# Find Middle of the Linked List / split the linked list in two halves


# Note: Distanc covered by fast pointer = 2 * Distance covered by slow pointer

def mid_finder(head: Node):
    
    slow = head
    fast = head
    
    while(fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next 
        
    return slow.value

    # Time: O(n)
    # Space: O(1)


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

print()
print("************ Mid Element of Linked List ************")
print("Given List: ")
print_nodes(a)

print()
print("Mid of this Linked List is: ", mid_finder(a))

# Problem 9: 
# Divide the Linked list in two halves

def divideLinkedList(head: Node):
    
    slow = head
    fast = head
    
    previous = head
    
    while fast is not None and fast.next is not None:
        previous = slow
        slow = slow.next
        fast = fast.next.next 
        
    previous.next = None
    
    newHead = slow
    
    return head, newHead

    # Time: O(n)
    # Space: O(1)


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
g = Node('G')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

print()
print("************ Split Linked List in two halves ************")
print("Given List: ")
print_nodes(a)

print()
x,y = divideLinkedList(a)
print("First half of Linked List is: ")
print_nodes(x)
print("Second half of Linked List is: ")
print_nodes(y)


# Problem 10: 
# Reordering (https://leetcode.com/problems/reorder-list/submissions/)
# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed

# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Solution i can use my previously built functions 
# step 1 -> split the linked list into 2 equal halves
# reverse second half 
# apply zipper list function on first and second linked list

def reordering_linked_list(head: Node) -> Node:
    
    # Step 1 -> Split the linked list into two equal halves
    
    first_list_head, second_list_head = divideLinkedList(head)
    
    # step 2 ->  reversing the second linked list
    second_list_head = reverseLinkedList(second_list_head)
    
    # step 3 -> apply zipper list function on first and second list
    zipperHead = zipper_linked_list(first_list_head, second_list_head)
    
    return zipperHead

    # Time: O(n)
    # Space: O(1)
    


a = Node('1')
b = Node('2')
c = Node('3')
d = Node('4')
e = Node('5')
# f = Node('F')
# g = Node('G')

a.next = b
b.next = c
c.next = d
d.next = e
# e.next = f
# f.next = g

print()
print("************ Reordering Linked List ************")
print("Given List: ")
print_nodes(a)

print()
reordered_head = reordering_linked_list(a)
print("Reordered Linked List is: ")
print_nodes(reordered_head)
    
    
# Problem 11
# Remove Linked List Elements (LeetCode: https://leetcode.com/problems/remove-linked-list-elements/description/)

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

def removeElements(head: Node, value: int):

    # Handle the case where the head needs to be removed
    while head and head.value == value:
        head = head.next

    # Initialize current and previous pointers
    current = head
    previous = None



    while(current is not None): 
            
        if(current.value == value):
                #logic to remove
            previous.next = current.next
        else:
                # Only update previous if no node was removed
            previous = current
            
        current = current.next

    return head

    
a = Node('1')
b = Node('2')
c = Node('3')
d = Node('3')
e = Node('5')
# f = Node('F')
# g = Node('G')

a.next = b
b.next = c
c.next = d
d.next = e
# e.next = f
# f.next = g

print()
print("************ Removing Element from Linked List ************")
print("Given List: ")
print_nodes(a)
toRemove = '3'
print("Element to remove - ", toRemove)

print()
new_list_head = removeElements(a, toRemove)
print("New Linked List is: ")
print_nodes(new_list_head)