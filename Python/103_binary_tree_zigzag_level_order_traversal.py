# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        
        stack1 = [(root, 0)]
        stack2 = []
        output = []
        
        while stack1 != [] or stack2 != []:
            while stack1 != []:
                node, level = stack1.pop()
                if node:
                    if level >= len(output):
                        output.append([])
                    output[level].append(node.val)
                    stack2.append((node.left, level+1))
                    stack2.append((node.right, level+1))
            
            while stack2 != []:
                node, level = stack2.pop()
                if node:
                    if level >= len(output):
                        output.append([])
                    output[level].append(node.val)
                    stack1.append((node.right, level+1))
                    stack1.append((node.left, level+1))
                
        return output