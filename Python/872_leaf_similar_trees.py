# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        output1 = self.generate_leaf_seq(root1)
        output2 = self.generate_leaf_seq(root2)
        
        return output1 == output2
        
    def generate_leaf_seq(self, root):
        self.output = []
        self.pre_order_traverse(root)
        
        return self.output.copy()
    
    def pre_order_traverse(self, node):
        if node:
            if not node.left and not node.right:
                self.output.append(node.val)
            self.pre_order_traverse(node.left)
            self.pre_order_traverse(node.right)