# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        
        pointer1 = head
        prev = None
        pointer2 = head
        while pointer2:
            pointer2 = pointer2.next
            if pointer2:
                pointer2 = pointer2.next
            prev = pointer1
            pointer1 = pointer1.next
        prev.next = None
        
        current = pointer1
        prev = None
        while current:
            next_point = current.next
            current.next = prev
            prev = current
            current = next_point
            
        pointer1 = head
        pointer2 = prev
        prev = 0
        
        while pointer1 or pointer2:
            point1_next = pointer1.next if pointer1 else None
            point2_next = pointer2.next if pointer2 else None
            
            pointer1.next = pointer2
            if prev:
                prev.next = pointer1
            
            pointer1 = point1_next            
            prev = pointer2
            pointer2 = point2_next
        
        return head