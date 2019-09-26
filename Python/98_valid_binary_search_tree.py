# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        if not root:
            return True
        
        self.output = True
        self.prev = None
        self.in_order_traverse(root)
        return self.output
    
    def in_order_traverse(self, root):
        if root:
            self.in_order_traverse(root.left)
            
            if self.prev is None:
                pass
            else:
                if self.prev >= root.val:
                    self.output = False
            self.prev = root.val
            
            self.in_order_traverse(root.right)
    

s = Solution()