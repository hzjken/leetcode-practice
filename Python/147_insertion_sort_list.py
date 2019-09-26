# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        if not head:
            return None
        
        start = head
        origin = head.next
        start.next = None
        
        while origin:
            point = origin
            origin = origin.next
            
            new = start
            prev = None
            while new and new.val < point.val:
                prev = new
                new = new.next
            
            if prev:
                prev.next = point
                point.next = new
            else:
                point.next = new
                start = point
                
        return start
