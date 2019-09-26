# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        if not head:
            return None   
        
        n = 0
        current = head
        while current:
            n += 1
            current = current.next
        
        if n == 1 or k % n == 0:
            return head
        
        pointer1 = head
        pointer2 = head
        k = k % n
        
        for _ in range(k):
            pointer1 = pointer1.next
        
        while pointer1.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        
        start = pointer2.next
        pointer2.next = None
        pointer1.next = head
        
        return start