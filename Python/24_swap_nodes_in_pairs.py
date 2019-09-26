class Solution:
    def swapPairs(self, head):
        if not head:
            return None
        
        current = head
        prev = None
        connection = None
        start = None
        n = 0
        
        while current:
            if n % 2 == 1:
                if connection:
                    connection.next = current
                else:
                    start = current
                next_point = current.next
                current.next = prev
                current = next_point
                connection = prev
            elif n % 2 == 0:
                prev = current
                current = current.next
            n += 1
            
        if n % 2 == 0:
            connection.next = None
        elif n == 1:
            return head
        else:
            connection.next = prev
        
        return start