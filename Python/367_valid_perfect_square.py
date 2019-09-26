class Solution:
    def isPerfectSquare(self, num):
        x0 = num
        
        while True:
            x0 -= (x0**2 - num)/(2*x0)
            int_num = int(x0)
            
            if int_num ** 2 == num:
                return True
            elif int_num ** 2 > num:
                x0 = int_num
            else:
                return False


s = Solution()
print(s.isPerfectSquare(81))
print(s.isPerfectSquare(80))