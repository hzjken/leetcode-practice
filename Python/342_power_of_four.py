class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 1:
            return True
        if num < 1:
            return False
        
        binary = bin(num)[2:]
        return binary.count('1') == 1 and binary.count('0') % 2 == 0


s = Solution()
print(s.isPowerOfFour(64))