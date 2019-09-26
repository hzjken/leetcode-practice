# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        output = self.recur(root)
        return max(output)
        
    def recur(self, node):
        if not node:
            return (0, 0)
        if not node.left and not node.right:
            return (node.val, 0)
        else:
            left_tup = self.recur(node.left)
            right_tup = self.recur(node.right)
            right_val = left_tup[0] + right_tup[0]
            left_val = max(node.val + left_tup[1] + right_tup[1], right_val)
            return (left_val, right_val)
        