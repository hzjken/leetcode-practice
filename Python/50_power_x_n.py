import numpy as np

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        elif n == 0:
            return 1
        
        if n > 0:
            n_positive = True
        else:
            n_positive = False
            n *= -1
        if x > 0:
            x_positive = True
        else:
            x_positive = False
        
        output = 1
        power = 0
        
        multiply = x
        add_power = 1
        
        
        while True:
            if power + add_power == n:
                output = output * multiply
                break
            elif power + add_power < n:
                output *= multiply
                multiply = output
                power += add_power
                add_power = power
            else:
                multiply = np.sqrt(multiply)
                add_power /= 2
        
        if not n_positive:
            output = 1 / output
        
        if not x_positive:
            if n % 2 == 1:
                output *= -1
        
        return output
        
        
s = Solution()
print(s.myPow(2.5, 5))