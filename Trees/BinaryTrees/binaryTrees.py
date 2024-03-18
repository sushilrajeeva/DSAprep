from typing import *
from collections import *

class Queue:

    def __init__(self):
        self.queue = deque()

    def isEmpty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False
    
    def enqueue(self, data) -> None:
        self.queue.append(data) # This adds to the right

    def dequeue(self) -> int:
        if self.isEmpty():
            raise IndexError("Queue is Empty")
        return self.queue.popleft()
    
    def peek(self) -> int:
        if self.isEmpty():
            print("Empty Queue")
            return None
        return self.queue[0]



class BinaryTree:

    def __init__(self, data: int = 0, left: Optional['BinaryTree'] = None ,right: Optional['BinaryTree'] = None):
        self.data = data
        self.left = left
        self.right = right


# Create the nodes
root = BinaryTree(1)
node2 = BinaryTree(2)
node3 = BinaryTree(3)
node4 = BinaryTree(4)
node5 = BinaryTree(5)
node6 = BinaryTree(6)
node7 = BinaryTree(7)
# Link the nodes to form the tree
root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

# Travelling techniques
# There are two types - BFS and DFS 
# In DFS we have - 1. Inorder Treversal, 2. Preorder Treversal, 3. Postorder Traversal
# Inorder Traversal means go to extreme left and then recurse -> Left Root Right
# Pre-Order Treaversal means go to the root and apply recursively -> Root Left Right
# Post-Order Traversal means go to extreme left and apply recursively -> Left Right Root

# Level order traversal is BFS

def in_order_traversal(node: Optional['BinaryTree']) -> None:

    if node:
        in_order_traversal(node.left)
        print(node.data)
        in_order_traversal(node.right)

def pre_order_traversal(node: Optional['BinaryTree']) -> None:

    if node:
        print(node.data)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

def post_order_traversal(node: Optional['BinaryTree']) -> None:

    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.data)
        
        

print("Printing the given binary tree in Inorder")
in_order_traversal(root)
print("Printing the given binary tree in Pre-Order")
pre_order_traversal(root)
print("Printing the given binary tree in Post-Order")
post_order_traversal(root)

# BFS

def levelOrder(root: Optional['BinaryTree']) -> None:
    
    queue = Queue()
    queue.enqueue(root)
    queue.enqueue(None)

    while not queue.isEmpty():
        curNode: BinaryTree = queue.dequeue()

        if curNode is None:
            print()
            if queue.isEmpty():
                break
            else:
                queue.enqueue(None)
        else:
            print(curNode.data, end= " ")
            
            if curNode.left is not None:
                queue.enqueue(curNode.left)
            
            if curNode.right is not None:
                queue.enqueue(curNode.right)

print(f"Print the level order of the following tree")
levelOrder(root)

def countNodes(root: Optional['BinaryTree']) -> int:

    if root is None:
        return 0

    leftCount = countNodes(root.left)
    rightCount = countNodes(root.right)

    return leftCount + rightCount + 1

print("number of nodes in given binary tree :", countNodes(root))

def sumOfNodes(root: Optional['BinaryTree']) -> int:

    if root is None:
        return 0


    leftSubSum = sumOfNodes(root.left)
    rightSubSum = sumOfNodes(root.right)

    return leftSubSum + rightSubSum + root.data

print("sum of all the nodes of the given binary tree is :", sumOfNodes(root))

def heightOfTree(root: Optional['BinaryTree']) -> int:

    if root is None:
        return 0


    leftHeight = heightOfTree(root.left)
    rightHeight = heightOfTree(root.right)

    return max(leftHeight, rightHeight) + 1

print("Height of the given binary tree is :", heightOfTree(root))


