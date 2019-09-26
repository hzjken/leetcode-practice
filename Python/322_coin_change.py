class Solution:
    def coinChange(self, coins, amount):
        self.dp = {0:0}
        self.coins = coins
        for i in coins:
            self.dp[i] = 1
        output = self.recur(amount)
        return output if output is not None else -1
        
    def recur(self, amount):
        if amount in self.dp:
            return self.dp[amount]
        elif amount < 0:
            return None
        else:
            amt_list = [amount - i for i in self.coins]
            num_list = [self.recur(i) for i in amt_list]
            num_list = [i for i in num_list if i is not None]
            if num_list == []:
                self.dp[amount] = None
            else:
                self.dp[amount] = min(num_list) + 1
            return self.dp[amount]
                

s = Solution()
print(s.coinChange([1,2,5,10], 57))