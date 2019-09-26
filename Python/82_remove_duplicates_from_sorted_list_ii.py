# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        
        current = head
        temp = head
        prev = None
        prev_connect = None
        start = None
        
        while current:
            prev = current
            current = current.next
            
            if current:
                if prev.val != current.val:
                    if temp:
                        if not start:
                            start = temp
                            prev_connect = temp
                        else:
                            prev_connect.next = temp
                            prev_connect = temp
                    temp = current
                else:
                    temp = None
            else:
                if not start:
                    start = temp
                else:
                    prev_connect.next = temp
                
        return start
