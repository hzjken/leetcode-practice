class Solution:
    def findOrder(self, numCourses, prerequisites):
        self.prereq = {}
        for former, latter in prerequisites:
            if latter not in self.prereq:
                self.prereq[latter] = [former]
            else:
                self.prereq[latter].append(former)
        
        self.non_visited = {i for i in range(numCourses)}
        self.output_stack = []
        self.visit_stack = set()
        self.loop = False
        
        while len(self.non_visited) != 0:
            node = self.non_visited.pop()
            self.non_visited.add(node)
            self.recur(node)
        
        if self.loop:
            return []
        else:
            return self.output_stack[::-1]
        
    def recur(self, node):
        if node in self.non_visited:
            if node in self.visit_stack:
                self.loop = True
            else:
                self.visit_stack.add(node)

                if node not in self.prereq:
                    self.output_stack.append(node)
                else:
                    for target in self.prereq[node]:
                        self.recur(target)
                    self.output_stack.append(node)

                self.visit_stack.remove(node)
                self.non_visited.remove(node)


s = Solution()
print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))