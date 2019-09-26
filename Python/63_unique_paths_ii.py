class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        self.dp = {(1,1): 1}
        self.obstacle = obstacleGrid
        self.m = len(self.obstacle)
        self.n = len(self.obstacle[0])
        
        return self.recur(self.m, self.n)
    
    def recur(self, m, n):
        if self.obstacle[self.m - m][self.n - n] == 1:
            self.dp[(m, n)] = 0
        elif (m, n) in self.dp:
            pass
        else:
            if m > 1 and n > 1:
                self.dp[(m, n)] = self.recur(m-1, n) + self.recur(m, n-1)
            elif m == 1:
                self.dp[(m, n)] = self.recur(m, n-1)
            else:
                self.dp[(m, n)] = self.recur(m-1, n)
            
        return self.dp[(m, n)]


s = Solution()
print(s.uniquePathsWithObstacles(
    [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
))