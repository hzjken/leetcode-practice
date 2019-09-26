class Solution:
    def flipLights(self, n, m):
        if m == 0:
            return 1
        elif n == 1:
            return 2
        elif n == 2:
            if m == 1:
                return 3
            if m > 1:
                return 4
        else:
            if m >= 3:
                return 8
            else:
                if m == 1:
                    return 4
                elif m == 2:
                    return 7
                

s = Solution()
print(s.flipLights(8,10))