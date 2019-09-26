# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def sortList(self, head):
        if not head:
            return None

        return self.recur(head)

    def recur(self, head):
        if not head:
            return None
        if not head.next:
            return head

        pointer1 = head
        pointer2 = head
        prev = None

        while pointer2:
            pointer2 = pointer2.next
            if pointer2:
                pointer2 = pointer2.next
            prev = pointer1
            pointer1 = pointer1.next
        prev.next = None

        first = self.recur(head)
        second = self.recur(pointer1)

        start = first
        prev = None

        while first or second:
            if first and second and first.val <= second.val:
                prev = first
                first = first.next
            elif first and second and first.val > second.val:
                point = second
                second = second.next
                point.next = None

                if prev:
                    prev.next = point
                    point.next = first
                    prev = prev.next
                else:
                    point.next = first
                    start = point
                    prev = point
            elif first:
                break
            else:
                prev.next = second
                break

        return start
                    
                