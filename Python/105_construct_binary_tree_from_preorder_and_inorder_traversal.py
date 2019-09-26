# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if preorder == [] and inorder == []:
            return None
        
        self.preorder = preorder
        self.inorder = inorder
        root = TreeNode(preorder[0])
        self.preorder.pop(0)
        
        self.recur(root, inorder)
        return root
        
    def recur(self, node, inorder):
        if node:
            node_pos = inorder.index(node.val)
            left = inorder[:node_pos]
            right = inorder[node_pos+1:]
            if left != []:
                for i in range(len(self.preorder)):
                    if self.preorder[i] in left:
                        node.left = TreeNode(self.preorder[i])
                        self.preorder.pop(i)
                        self.recur(node.left, left)
                        break

            if right != []:
                for i in range(len(self.preorder)):
                    if self.preorder[i] in right:
                        node.right = TreeNode(self.preorder[i])
                        self.preorder.pop(i)
                        self.recur(node.right, right)
                        break
            
