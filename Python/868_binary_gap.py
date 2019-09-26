class Solution:
    def binaryGap(self, N):
        string = bin(N)[2:]
        
        dist = 0
        prev = None
        for i in range(len(string)):
            if string[i] == '1':
                if prev is None:
                    prev = i
                else:
                    dist = max(dist, i-prev)
                    prev = i
        
        return dist


s = Solution()
print(s.binaryGap(22))