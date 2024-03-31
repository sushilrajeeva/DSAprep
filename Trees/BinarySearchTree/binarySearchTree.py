from typing import *

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
            
    def getBST(self, root: Node):
        # Inorder gives bst in sorted order [ascending] -> LEFT -> ROOT -> RIGHT
        result = []

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
print("Printing the binary Tree")
print(bst.getBST(bst.root))
value = 30
print(f"Value {value} in BST :", bst.isPresent(value))



    
