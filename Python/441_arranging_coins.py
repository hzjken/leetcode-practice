class Solution:
    def arrangeCoins(self, n):
        x0 = n
        
        while True:
            func = (1+x0)*x0 / 2 - n
            deri = x0 + 0.5
            x0 = x0 - func/deri
            
            int_x0 = int(x0)
            func_val = (1+int_x0) * int_x0 / 2 - n
            if func_val <= 0:
                return int_x0
            else:
                x0 = int_x0


s = Solution()
print(s.arrangeCoins(29))