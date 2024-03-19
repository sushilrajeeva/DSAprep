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
    
    def size(self) -> int:
        return len(self.queue)



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

def levelOrder(root: Optional['BinaryTree']) -> List[List[int]]:

    res = []

    if not root:
        return res
    
    queue = Queue()
    queue.enqueue(root)

    while not queue.isEmpty():
        cur_level = []
        cur_size = queue.size()

        for i in range(cur_size):
            node = queue.dequeue()
            cur_level.append(node.data)

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        res.append(cur_level)

    return res


print(f"Print the level order of the following tree")
level_order = levelOrder(root)
for level in level_order:
    print(level)

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

# Balanced Binary Tree
# A Binary Tree is said to be balanced if the height of the left sub tree - height of the right sub tree <= 1 (abs)

def isBalancedBinaryTree(root: Optional['BinaryTree']) -> bool:

    def getBalancedHeight(root: Optional['BinaryTree']) -> int:
        if root is None:
            return 0
        
        leftHeight = getBalancedHeight(root.left)
        rightHeight = getBalancedHeight(root.right)

        if leftHeight == -1 or rightHeight == -1:
            return -1

        if abs(leftHeight - rightHeight) > 1:
            return -1
        
        return max(leftHeight, rightHeight) + 1
    
    return True if getBalancedHeight(root) != -1 else False


print("The Given Binary Tree is Blananced? :", isBalancedBinaryTree(root))

# Diameter of the Binary Tree
# It is the maximum path between two leaf nodes
def getDiameter(root: Optional['BinaryTree']) -> int:

    maximum = [0]

    def findMaxDiameter(root: Optional['BinaryTree']) -> int:

        if root is None:
            return 0
        
        leftDiameter = findMaxDiameter(root.left)
        rightDiameter = findMaxDiameter(root.right)

        maximum[0] = max(maximum[0], leftDiameter + rightDiameter)

        return max(leftDiameter, rightDiameter) + 1
    
    findMaxDiameter(root)

    return maximum[0]

print("The Given Binary Tree has a diameter of :", getDiameter(root))

# Get the maximum sum of any path in the given Binary Tree
def maxPathSum(root: Optional['BinaryTree']) -> int:

    maxPath = [float("-inf")]

    def getHeight(root: Optional['BinaryTree']) -> int:

        if root is None:
            return 0
        
        leftPath = max(getHeight(root.left), 0)
        rightPath = max(getHeight(root.right), 0)

        maxPath[0] = max(maxPath[0], leftPath + rightPath + root.data)

        return max(leftPath, rightPath) + root.data
    
    getHeight(root)
    return maxPath[0]

print("The Given Binary Tree has a Maximum Path sum of :", maxPathSum(root))

# Advanced Level order BFS

# Leetcode 314 : Binary Tree Veritcal order traversal

# Given the root of a binary tree, return the vertical order traversal of its nodes values (i.e, from top to bottom, column by column).
# If two nodes are in the same row and column, the order should be from left to right

def verticalOrder(root: Optional['BinaryTree']) -> List[List[int]]:

    if not root:
        return []
    
    column_items = defaultdict(list)

    queue = Queue()
    queue.enqueue((0, root))

    min_x = float("inf")
    max_x = float("-inf")

    res = []

    # BFS
    while not queue.isEmpty():

        x, node = queue.dequeue()

        column_items[x].append(node.data)

        min_x = min(min_x, x)
        max_x = max(max_x, x)

        if node.left:
            queue.enqueue((x-1, node.left))
        
        if node.right:
            queue.enqueue((x+1, node.right))


    for level in range(min_x, max_x + 1):
        res.append(column_items[level])

    return res

print("The Vertical Order Traversal of the given Binary Tree :", verticalOrder(root))

def topView(root: Optional['BinaryTree']) -> List[int]:

    if not root:
        return []
    
    column_items = dict()

    queue = Queue()
    queue.enqueue((0, root))

    min_x, max_x = float("inf"), float("-inf")

    res = []

    while not queue.isEmpty():

        x, node = queue.dequeue()

        min_x = min(min_x, x)
        max_x = max(max_x, x)

        if column_items.get(x, None) is None:
            column_items[x] = node.data

        if node.left:
            queue.enqueue((x - 1, node.left))
        if node.right:
            queue.enqueue((x+1, node.right))

    for level in range(min_x, max_x + 1):
        res.append(column_items[level])

    return res

print("The Top Order view of the given Binary Tree :", topView(root))

def bottomView(root: Optional['BinaryTree']) -> List[int]:

    if not root:
        return []
    
    min_col, max_col = float("inf"), float("-inf")

    column_items = defaultdict(int)

    queue = Queue()
    queue.enqueue((0, root))

    while not queue.isEmpty():
        col, node = queue.dequeue()

        min_col = min(min_col, col)
        max_col = max(max_col, col)

        column_items[col] = node.data

        if node.left:
            queue.enqueue((col - 1, node.left))
        if node.right:
            queue.enqueue((col + 1, node.right))

    res = []

    for level in range(min_col, max_col + 1):
        res.append(column_items[level])

    return res

print("The Bottom view of the given Binary Tree :", bottomView(root))

# Right View

def left_view(root: Optional['BinaryTree']) -> List[int]:

    res = []

    if not root:
        return res

    queue = Queue()
    queue.enqueue(root)

    while not queue.isEmpty():
        level_left = None
        cur_size = queue.size()

        for i in range(cur_size):
            node = queue.dequeue()
            if level_left is None:
                level_left = node.data

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        res.append(level_left)

    return res

print("The Left view of the given Binary Tree :", left_view(root))

def right_view(root: Optional['BinaryTree']) -> List[int]:

    res = []

    if not root:
        return res

    queue = Queue()
    queue.enqueue(root)

    while not queue.isEmpty():

        level_right = 0
        cur_size = queue.size()

        for i in range(cur_size):

            node = queue.dequeue()
            level_right = node.data

            if node.left:
                queue.enqueue(node.left)

            if node.right:
                queue.enqueue(node.right)

        res.append(level_right)

    return res

print("The Right view of the given Binary Tree :", right_view(root))
        


    

        






