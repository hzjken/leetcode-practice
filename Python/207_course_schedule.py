class Solution:
    def canFinish(self, numCourses, prerequisites):
        self.prereq = {}
        self.stack = set()
        for former, latter in prerequisites:
            if former not in self.prereq:
                self.prereq[former] = [latter]
            else:
                self.prereq[former].append(latter)
        
        self.output = True
        self.non_visited = {i for i in range(numCourses)}
        while len(self.non_visited) != 0:
            node = self.non_visited.pop()
            self.non_visited.add(node)
            self.check_loop(node)
            
        return self.output
    
    def check_loop(self, node):
        if node in self.non_visited:
            if node not in self.stack:
                self.stack.add(node)
                if node in self.prereq:
                    for target in self.prereq[node]:
                        self.check_loop(target)

                self.stack.remove(node)
                self.non_visited.remove(node)
            else:
                self.output = False


s = Solution()
print(s.canFinish(2, [[1,0],[0,1]]))