# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        if not root:
            return []
        
        self.output = []
        self.stack = []
        self.recur(root, sum)
        
        return self.output
    
    def recur(self, node, val):
        if node:
            self.stack.append(node.val)
            remain = val - node.val
            if not node.left and not node.right:
                if remain == 0:
                    self.output.append(self.stack.copy())
            else:
                self.recur(node.left, remain)
                self.recur(node.right, remain)
            
            self.stack.pop()