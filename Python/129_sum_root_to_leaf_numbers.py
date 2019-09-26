# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        if not root:
            return 0
        
        self.stack = []
        self.output = 0
        
        self.recur(root)
        return self.output
    
    def recur(self, node):
        if node:
            self.stack.append(str(node.val))
            if not node.left and not node.right:
                val = int(''.join(self.stack))
                self.output += val
            else:
                if node.left:
                    self.recur(node.left)
                if node.right:
                    self.recur(node.right)
            self.stack.pop()
    