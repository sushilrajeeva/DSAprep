from typing import *

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