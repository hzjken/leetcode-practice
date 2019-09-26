class Solution:
    def divide(self, dividend, divisor):
        if dividend == 0:
            return 0
        
        same_sign = False
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            same_sign = True
            
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        output = 0
        while True:
            move = 0
            while dividend >= (divisor << move):
                move += 1
            
            if move > 0:
                dividend -= (divisor << (move-1))
                output += (1 << (move - 1))
            else:
                break
            
        if not same_sign:
            output = -(output)
        
        if output >= (1 << 31) or output < -(1 << 31):
            output = (1 << 31) - 1
        
        return output


s = Solution()
print(s.divide(2147483648, 1))