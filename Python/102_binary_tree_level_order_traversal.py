# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        queue = [(root, 0)]
        output = []
        output_len = 0
        
        while queue != []:
            node, level = queue.pop(0)
            if node:
                if level >= output_len:
                    output.append([])
                    output_len += 1
                
                output[level].append(node.val)
                
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))

        return output