class Node:
    #A node structure contains a constructor
    #Constructor takes a value
    #by default when a node is created, it's value is set and the next pointer is set to None;
       
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next
    
    
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

    # Creating a dummy node and pointing it to the head of my given linked list
    dummy: Node = Node(next=head)
    
    # Assigning previous to my dummy
    previous: Node = dummy
    # Assigning current to my head of linked list
    current: Node = head
    
    while current is not None:
        
        # Storing the next node in a next variable
        next = current.next
        
        # delete the node if it has the value we want to delete
        if(current.value == value):
            previous.next = next
        else:
            previous = current
            
        current = next
    
    return dummy.next

    # Time: O(n)
    # Space: O(1)
    

    
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


# Problem 12: Palindrome

# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Input: head = [1,2,2,1]
# Output: true

# Follow up: Could you do it in O(n) time and O(1) space?

def isPalindrome(head: Node) -> bool:
    
    #First i will break this problem into multiple parts 
    # 1. Getting the mid point
    # 2. Reverse the linked list from mid point
    # 3. Itterate from the second half (right side) reversed till it reaches null and compare it with the first half (left side)
    # 4. return true or false depending on if it is same throughout or not
    
    # Getting mid point (using two pointer)
    
    slow:Node = head
    fast:Node = head
    
    
    while(fast is not None and fast.next is not None):
        
        slow = slow.next 
        fast = fast.next.next 
        
    
    mid = slow
    
    # Reversing the linked list from mid
    
    previous = None
    current = mid
    
    
    while(current is not None):
        next = current.next 
        current.next = previous
        previous = current
        current = next 
        
    
    #This will contain the head of the second half i.e last element of original linked list
    right = previous
    left = head 
    
    #Checking palindrome
    
    while(right is not None):
        if left.value != right.value:
            return False
        left = left.next 
        right = right.next
        
    return True


a = Node('1')
b = Node('2')
c = Node('3')
d = Node('2')
e = Node('1')


a.next = b
b.next = c
c.next = d
d.next = e


print()
print("************ Checking Palindrome from Linked List ************")
print("Given List: ")
print_nodes(a)

print()
value = "is a" if isPalindrome(a) else "not a"
print("The given linked list",value, "Palindrome" )

#Problem 13: 
# Merging two sorted list

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

def mergeTwoLists(list1: Node, list2: Node) -> Node:
    
    #I will create a starting point of my result node that will contain the merger of two lists
    dummy = Node()
    #Tail to keep track of the end of the linked list
    tail = dummy
    
    # now let's itterate over both lists and check which is having lower value that will be added to the dummy linked liat tail
    
    while(list1 is not None and list2 is not None):
        
        if(list1.value < list2.value):
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
            
        tail = tail.next
        
    # one of the list will have remaining elements so we have to append it to the end of the dummy list
    
    if(list1 is not None):
        tail.next = list1
    else:
        tail.next = list2
        
    return dummy.next

    # Time: O(n)
    # Space: O(1)
    
    
a = Node('1')
b = Node('2')
c = Node('3')



a.next = b
b.next = c


x = Node('1')
y = Node('1')
z = Node('4')



x.next = y
y.next = z


print()
print("************ Merging two Linked List ************")
print("Given List A: ")
print_nodes(a)
print("Given List B: ")
print_nodes(x)
print()
print("Merged Linked List: ")
print_nodes(mergeTwoLists(a,x))



# Problem 14
# Merge k Sorted Lists
# Leetcode link -> https://leetcode.com/problems/merge-k-sorted-lists/

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6


def mergeKLists(lists: list[Node]) -> Node:
    
    # edge cases
    
    # edge case 1: when given list is empty it should return none
    if not lists or len(lists) == 0:
        return None
    
    # do this logic till my lists array has only one element
    while len(lists) > 1:
        
        # storing the output of two merged sorted list
        mergedLists = []
        
        # Iterrate the loop in step of 2
        for i in range(0, len(lists), 2):
            
            list1 = lists[i]
            # Edge Case 2: while looping if the array is of odd length then we might encounter array out of bound when trying to get i+1 element
            list2 = lists[i+1] if (i+1) < len(lists) else None
            
            # Now i have to merge these two linked lists to one linked lists
            mergedLists.append(mergeTwoLists(list1, list2))
            
            
            
        # now replace this merged linked lists (size of it is half of original list) with the original lists
        
        lists = mergedLists
        
    # after the while loop executes only one element will be present in the list, and that is the k merged linked lists in sorted order
    return lists[0]

    # Time: O(n*log(k))
    # space: O(n)
    
    
    
#Input: lists = [[1,4,5],[1,3,4],[2,6]]
    
lists = []

a = Node(1)
b = Node(4)
c = Node(5)

a.next = b
b.next = c


lists.append(a)

l = Node(1)
m = Node(3)
n = Node(4)

l.next = m
m.next = n

lists.append(l)

x = Node(2)
y = Node(6)

x.next = y

lists.append(x)



print()
print("************ Merging K sorted Linked List ************")
print("Given List 1: ")
print_nodes(lists[0])
print("Given List 2: ")
print_nodes(lists[1])
print("Given List 3: ")
print_nodes(lists[2])
print()
print("Merged K Linked List: ")
print_nodes(mergeKLists(lists))


            
# Problem 15:
# Add Two Numbers
# Medium

# LeetCode link -> https://leetcode.com/problems/add-two-numbers/description/

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.       

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

def addTwoNumbers(node1: Node, node2: Node) -> Node:
    
    dummy = Node()
    current = dummy
    carry = 0
    
    while node1 is not None or node2 is not None or carry:
        
        # Taking care of condition when one of them is empty like very large number plus small -> 100000 + 3 , so it is actually 100000 + 000003
        v1 = node1.value if node1 else 0
        v2 = node2.value if node2 else 0
        
        value = v1 + v2 + carry
        
        # compute carry and value if it over flows
        carry = value // 10
        value = value % 10
        
        current.next = Node(value)
        
        current = current.next
        node1 = node1.next if node1 else None
        node2 = node2.next if node2 else None
        
    return dummy.next

    # Time: O(max(m,n))
    # Space: O(max(m,n))

        


a = Node(2)
b = Node(4)
c = Node(3)

a.next = b
b.next = c


l = Node(5)
m = Node(6)
n = Node(4)

l.next = m
m.next = n



print()
print("************ Adding two Linked List numbers ************")
print("Given List A: ")
print_nodes(a)
print("Given List B: ")
print_nodes(l)
print()

print("Addition of two linked list numbers is: ")
print_nodes(addTwoNumbers(a, l))


# Problem 16: 

# 19. Remove Nth Node From End of List
# Medium
# LeetCode Link -> https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

def removeNthFromEnd(head: Node, n: int) -> Node:
    
    # creating a dummy node and linking it to the head
    dummy = Node(next = head)
    
    # setting left pointer to the dummy and right pointer to the nth distance from head
    
    left = dummy
    right = head
    
    # Logic to set right at nth distance from head initially
    while n > 0 and right is not None:
        right = right.next
        n-=1
        
    # Now keep itterating till right is None, when this happens then left will be the node we want to delete's position's left 
    
    while right is not None:
        left = left.next
        right = right.next
        
    # logic to delete the nth node from end
    left.next = left.next.next
    
    # return from head
    return dummy.next

    # Time: O(n)
    # Space: O(1)

# Input: head = [1,2,3,4,5], n = 2
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)


a.next = b
b.next = c
c.next = d
d.next = e



print()
print("************ Remove Nth Node From End of List ************")
print("Given List A: ")
print_nodes(a)
print()
n = 2
print("After deleting", n, "position from end, new Linked list:")
print_nodes(removeNthFromEnd(a, n))

# Problem 17

# 24. Swap Nodes in Pairs
# Medium
# Given a linked list, swap every two adjacent nodes and return its head. 
# You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

def swapPairs(head: Node) -> Node:
    
    if not head or not head.next:
        return head
    
    dummy = Node(next=head)
    previous = dummy
    
    while head and head.next:
        
        first: Node = head
        second: Node = head.next
        
        #swapping
        
        previous.next = second
        first.next = second.next
        second.next = first
        
        #updating the pointers
        previous = first
        head = first.next
        
    return dummy.next

    # Time: O(n)
    # Space: O(1)
    
    
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
    
a.next = b
b.next = c
c.next = d

print()
print("************ Swap Nodes in Pairs ************")
print("Given List A: ")
print_nodes(a)
print()
print("Swapped Linked List:")
print_nodes(swapPairs(a))