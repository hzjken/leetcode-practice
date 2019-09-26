# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        if inorder == [] and postorder == []:
            return None
        
        self.post = postorder
        root_val = self.post.pop()
        root = TreeNode(root_val)
        self.recur(root, inorder)
        
        return root
        
    def recur(self, node, inorder):
        if node:
            node_pos = inorder.index(node.val)
            left = inorder[:node_pos]
            right = inorder[node_pos+1:]
            
            if left != []:
                for i in reversed(range(len(self.post))):
                    if self.post[i] in left:
                        val = self.post.pop(i)
                        node.left = TreeNode(val)
                        self.recur(node.left, left)
                        break

            if right != []:
                for i in reversed(range(len(self.post))):
                    if self.post[i] in right:
                        val = self.post.pop(i)
                        node.right = TreeNode(val)
                        self.recur(node.right, right)
                        break
                        