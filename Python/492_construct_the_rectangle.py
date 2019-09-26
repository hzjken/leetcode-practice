import numpy as np

class Solution:
    def constructRectangle(self, area):
        sqrt_num = np.sqrt(area)
        if sqrt_num == int(sqrt_num):
            return [int(sqrt_num), int(sqrt_num)]
        else:
            width = int(sqrt_num)
            length = width + 1
            while length * width != area:
                if length * width > area:
                    width -= 1
                else:
                    length += 1
        
            return [length, width]


s = Solution()
print(s.constructRectangle(20))
        