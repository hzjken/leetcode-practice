# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None
        
        self.array = []
        current = head
        
        while current:
            self.array.append(current.val)
            current = current.next
            
        left = 0
        right = len(self.array) - 1
        return self.recur(left, right)
        
    def recur(self, left, right):
        if left <= right:
            mid = (left + right) // 2
            node = TreeNode(self.array[mid])
            if mid != left:
                node.left = self.recur(left, mid-1)
            if mid != right:
                node.right = self.recur(mid+1, right)
            return node
        else:
            return None