# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        self.output = []
        self.preorder(root)
        prev = None
        
        while self.output != []:
            node = self.output.pop(0)
            node.left = None
            if not prev:
                pass
            else:
                prev.right = node
            prev = node
                
    def preorder(self, node):
        if node:
            self.output.append(node)
            self.preorder(node.left)
            self.preorder(node.right)


class Solution2:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        self.prev = None
        self.recur(root, 'first')
    
    def recur(self, node, pattern):
        if node:
            if pattern == 'second':
                self.prev.right = node
            
            node.left, node.right = node.right, node.left
            self.recur(node.right, 'first')
            next_point = node.left
            node.left = None
            if not node.left and not node.right:
                self.prev = node
            self.recur(next_point, 'second')