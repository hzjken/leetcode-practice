# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def partition(self, head, x):
        if not head:
            return head
        
        less = None
        greater = None
        less_start = None
        greater_start = None
        start = None
        current = head
        
        while current:
            if current.val < x:
                if not less_start:
                    less_start = current
                    less = current
                else:
                    less.next = current
                    less = current
            else:
                if not greater_start:
                    greater_start = current
                    greater = current
                else:
                    greater.next = current
                    greater = current
                    
            current = current.next
        
        if greater_start:
            greater.next = None
        else:
            less.next = None
        
        if less_start:
            start = less_start
            less.next = greater_start
        else:
            start = greater_start
            
        return start
            