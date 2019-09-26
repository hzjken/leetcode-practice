# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution1:
    def copyRandomList(self, head):
        if not head:
            return None
        
        visited = {}
        root = None
        current = head
        prev = None
        
        while current:
            if current.val not in visited:
                node = Node(current.val, None, None)
                if not root:
                    root = node
                visited[current.val] = node
            else:
                node = visited[current.val]
                
            if prev:
                visited[prev.val].next = node
            if current.random:
                if current.random.val not in visited:
                    random = Node(current.random.val, None, None)
                    visited[random.val] = random
                    node.random = random
                else:
                    node.random = visited[current.random.val]
          
            prev = current
            current = current.next
        
        return root


class Solution2:
    '''Time Limit Exceed'''
    def copyRandomList(self, head):
        if not head:
            return None
        
        visited = {}
        queue = [(head, None, 'next')]
        start = None
        
        while queue != []:
            current, from_node, source = queue.pop(0)
            if current:
                if current.val not in visited:
                    copy = Node(current.val, None, None)
                    visited[current.val] = copy
                    if not start:
                        start = copy

                    queue.append((current.next, copy, 'next'))
                    queue.append((current.random, copy, 'random'))
                    
                if from_node:
                    if source == 'next':
                        from_node.next = copy
                    else:
                        from_node.random = copy
        
        return start