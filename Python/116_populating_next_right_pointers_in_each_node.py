"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root):
        if not root:
            return None
        
        queue = [(root, 0)]
        while queue != []:
            node, level = queue.pop(0)
            if node:
                if queue == [] or level != queue[0][1]:
                    node.next = None
                else:
                    node.next = queue[0][0]

                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
        
        return root