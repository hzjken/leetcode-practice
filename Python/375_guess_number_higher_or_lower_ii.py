class Solution:
    def getMoneyAmount(self, n):
        self.dp = [[None] * n for i in range(n)]
        for i in range(n):
            self.dp[i][i] = 0
            if i < n - 1:
                self.dp[i][i+1] = i+1
        
        return self.recur(0, n-1)
    
    def recur(self, start, end):
        if start > end:
            return 0
        elif self.dp[start][end] is not None:
            return self.dp[start][end]
        else:
            min_val = None
            for i in range(start, end+1):
                first_half = self.recur(start, i-1)
                second_half = self.recur(i+1, end)
                output = i+1 + max(first_half, second_half)
                
                if min_val is None:
                    min_val = output
                else:
                    min_val = min(min_val, output)
            
            self.dp[start][end] = min_val
            return self.dp[start][end]


s = Solution()
print(s.getMoneyAmount(10))