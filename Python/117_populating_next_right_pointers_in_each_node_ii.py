"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root):
        if not root:
            return None
        
        self.recur(root)
        return root
    
    def recur(self, node):
        if not node or (not node.left and not node.right):
            pass
        else:
            if node.left and node.right:
                node.left.next = node.right
                son = node.right
            elif not node.left:
                son = node.right
            else:
                son = node.left
                
            next_point = node.next
            while next_point:
                if next_point.left:
                    son.next = next_point.left
                    break
                elif next_point.right:
                    son.next = next_point.right
                    break
                else:
                    pass
                next_point = next_point.next
            
            if node.right:
                self.recur(node.right)
            if node.left:
                self.recur(node.left)