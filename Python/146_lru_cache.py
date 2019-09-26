class Node:
    def __init__(self, key, val, before, after):
        self.key = key
        self.val = val
        self.before = before
        self.after = after

class LRUCache:

    def __init__(self, capacity):
        self.max_size = capacity
        self.node_map = {}
        self.start = None
        self.end = None
        self.size = 0

    def get(self, key):
        if key in self.node_map:
            node = self.node_map[key]
            self.update_node_place(node)
        
            return self.node_map[key].val
        else:
            return -1
        

    def put(self, key, value):
        if key in self.node_map:
            node = self.node_map[key] 
            node.val = value
            self.update_node_place(node)
        else:
            node = Node(key, value, None, None)
            self.node_map[key] = node
            self.update_node_place(node)
            
            if self.size == self.max_size:
                self.node_map.pop(self.end.key)
                self.end = self.end.before
                self.end.after = None
            else:
                self.size += 1
                
    def update_node_place(self, node):
        if self.start:      
            if node.before and node.after:
                node.before.after = node.after
                node.after.before = node.before
            elif node.before:
                node.before.after = None
                self.end = node.before
            elif node.after:
                node.after.before = None
                self.start = node.after
            else:
                pass
            
            if self.start != node:
                self.start.before = node
                node.after = self.start
                self.start = node
                self.start.before = None

        else:
            node.before = None
            node.after = None
            self.start = node
            self.end = node
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)