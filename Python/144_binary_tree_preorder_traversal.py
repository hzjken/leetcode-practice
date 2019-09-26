# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''RECURSIVE'''
    def preorderTraversal(self, root):
        if not root:
            return []
        
        self.output = []
        self.recur(root)
        return self.output
    
    def recur(self, root):
        if root:
            self.output.append(root.val)
            self.recur(root.left)
            self.recur(root.right)


class Solution2:
    '''iterative'''
    def preorderTraversal(self, root):
        if not root:
            return []
        
        output = []
        stack = [[root, False, False]]
        
        while stack != []:
            node, left_checked, right_checked = stack[-1]
            if node:
                if not left_checked:
                    output.append(node.val)
                    stack[-1][1] = True
                    stack.append([node.left, False, False])
                elif not right_checked:
                    stack[-1][2] = True
                    stack.append([node.right, False, False])
                else:
                    stack.pop()
            else:
                stack.pop()
                
        return output