class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1:
            return False
        
        while n > 1:
            if n % 3 == 0:
                n /= 3
            else:
                return False
        
        return True

s = Solution()
print(s.isPowerOfThree(81))