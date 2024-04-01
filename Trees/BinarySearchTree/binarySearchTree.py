from typing import *
from collections import deque

def printSegue():
    print("***************************************************************************************")

class Node:
    def __init__(self, value=None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value: int):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, cur_node: Node, value: int):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                self._insert_recursive(cur_node.left, value)
        else:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                self._insert_recursive(cur_node.right, value)
            
    def sortBST(self, root: Node = None):
        # Inorder gives bst in sorted order [ascending] -> LEFT -> ROOT -> RIGHT
        result = []
        if root is None:
            if self.root is None:
                return []
            root = self.root

        def _inorder_recursive(root: Node, result: List[int]):

            if root is None:
                return
            
            _inorder_recursive(root.left, result)
            result.append(root.value)
            _inorder_recursive(root.right, result)

        _inorder_recursive(root, result)

        return result
    
    def _isPresent_recursive(self, cur_node: Node, value) -> bool:
        if not cur_node:
            return False
        if cur_node.value == value:
            return True
        elif value < cur_node.value:
            return self._isPresent_recursive(cur_node.left, value)
        else: return self._isPresent_recursive(cur_node.right, value)
    
    def isPresent(self, value: int) -> bool:
        if not self.root:
            return False
        else: return self._isPresent_recursive(self.root, value)

    def printLevelOrderBST(self):
        if not self.root:
            return "The tree is empty"
        
        queue = deque([self.root])
        
        while queue:
            level_size = len(queue)  # Number of elements in the current level
            
            for _ in range(level_size):
                current_node = queue.popleft()
                if current_node.value:
                    print(current_node.value, end=' ')
                
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            
            print()  # New line after each level


    def getInorderSuccessor(self, root: Node) -> Node:
        # Getting the left most from root
        while root.left:
            root = root.left
        return root

    

    def _delete(self, root: Node, value: int) -> Node:

        # Delete a Node in BST
        # Case 1 - When the node to be deleted has no child, i.e the node is a leaf node - directly delete
        # Case 2 - When the node has a single child - attach the parent of the current node with the child of the current node
        # Case 3 - When the node has 2 child - replace the current node with its inorder successor

        if root is None:
            return root
        
        if value < root.value:
            root.left = self._delete(root.left, value)
        elif value > root.value:
            root.right = self._delete(root.right, value)
        else:
            # root.value == value
            # Case when root has 0 or 1 child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # Case when the Node has two children: Get the inorder successor (smallest in the right subtree)
            # Find inorder successor - left most node in our right subtree
            inorderSuccessor = self.getInorderSuccessor(root.right)
            root.value = inorderSuccessor.value
            root.right = self._delete(root.right, inorderSuccessor.value)

        return root


    def deleteNode(self, value: int):
        if self.root:
            self._delete(self.root, value)

    def printInRange(self, x: int, y: int):
        if self.root:
            self._printInRange(self.root, x, y)
        else: print("BST is empty")

    def _printInRange(self, root: Node, x: int, y: int):
        if not root:
            return
        if x <= root.value <= y:
            self._printInRange(root.left, x, y)
            print(root.value, end=" ")
            self._printInRange(root.right, x, y)
        elif y <= root.value:
            self._printInRange(root.left, x, y)
        else:
            self._printInRange(root.right, x, y)



# Example Usage
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

# Print in-order traversal of the BST
print("Printing the binary Tree in level order")
bst.printLevelOrderBST()

printSegue()

print("bst values in sorted order :", bst.sortBST())

printSegue()

value = 80
print(f"Value {value} in BST :", bst.isPresent(value))
printSegue()

value = 50
print(f"deleting {value} from BST")
bst.deleteNode(value)
print("Level order after deletion")
bst.printLevelOrderBST()
print("sorted after deletion :", bst.sortBST())
printSegue()

x = 0
y = 70
print(f"Printing the BST Nodes whose values are in range {x} to {y}")
bst.printInRange(x, y)

# Print in range
# X = 30, Y = 70 (INCLUSIVE)







  


        
