class Solution:
    def minPathSum(self, grid):
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        
        if self.m == 1 and self.n == 1:
            return self.grid[0][0]
        
        self.dp = {(1, 1): self.grid[self.m-1][self.n-1]}
        return self.recur(self.m,self.n)
    
    def recur(self, m, n):
        if (m,n) in self.dp:
            pass
        else:
            first = self.recur(m, n-1) if n > 1 else None
            second = self.recur(m-1, n) if m > 1 else None
            dist_list = [first, second]
            dist_list = [i for i in dist_list if i is not None]
            self.dp[(m, n)] = min(dist_list) + self.grid[self.m - m][self.n - n]
        
        return self.dp[(m, n)]

s = Solution()
print(s.minPathSum(
    [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
))