class Solution:
    def change(self, amount, coins):
        if amount == 0:
            return 1
        if coins == []:
            return 0
        
        self.row = len(coins) + 1
        self.col = amount + 1
        self.dp = [[None] * self.col for _ in range(self.row)]
        
        for col in range(self.col):
            self.dp[0][col] = 0
        for row in range(self.row):
            self.dp[row][0] = 1
            
        for row in range(1, self.row):
            for col in range(1, self.col):
                first = self.dp[row-1][col]
                second = self.dp[row][col-coins[row-1]] if col - coins[row-1] >= 0 else 0
                self.dp[row][col] = first + second
        
        return self.dp[len(coins)][amount]


s = Solution()
print(s.change(5, [1,2,5]))