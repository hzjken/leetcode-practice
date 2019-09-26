
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        
        visited = {}
        queue = [(node, None)]
        start = None
        
        while queue != []:
            current, from_node = queue.pop(0)
            if current.val not in visited:
                clone = Node(current.val, [])
                visited[current.val] = clone
                if from_node:
                    from_node.neighbors.append(clone)
                if not start:
                    start = clone
                queue += [(i, clone) for i in current.neighbors]
            else:
                if from_node:
                    from_node.neighbors.append(visited[current.val])
                    
        return start