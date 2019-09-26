class Solution:
    def uniquePaths(self, m, n):
        self.dp = {(1, 1): 1}
        return self.recur(m, n)
    
    def recur(self, m, n):
        if (m, n) in self.dp:
            return self.dp[(m, n)]
        else:
            if m > 1 and n > 1:
                self.dp[(m, n)] = self.recur(m-1, n) + self.recur(m, n-1)
            elif m == 1:
                self.dp[(m, n)] = self.recur(m, n-1)
            else:
                self.dp[(m, n)] = self.recur(m-1, n)
            
            return self.dp[(m, n)]


s = Solution()
print(s.uniquePaths(7,3))