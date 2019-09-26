class DFS:
    def minimumTotal(self, triangle):
        if triangle == []:
            return 0
        
        self.sumup = None
        self.tri = triangle
        self.height = len(self.tri)
        self.recur(0, 0, self.tri[0][0])
        
        return self.sumup
        
    def recur(self, height, pos, sumup):
        if height == self.height - 1:
            if self.sumup is None:
                self.sumup = sumup
            else:
                self.sumup = min(self.sumup, sumup)
        else:
            self.recur(height+1, pos, sumup + self.tri[height+1][pos])
            self.recur(height+1, pos+1, sumup + self.tri[height+1][pos+1])


class Solution:
    '''DP with constant extra space'''
    def minimumTotal(self, triangle):
        if triangle == []:
            return 0
        
        for row in range(1, len(triangle)):
            for col in range(len(triangle[row])):
                first = triangle[row-1][col-1] if col-1 >=0 else None
                second = triangle[row-1][col] if col < len(triangle[row]) - 1 else None
                last_row = [first, second]
                min_val = min([i for i in last_row if i is not None])
                triangle[row][col] += min_val
        
        return min(triangle[-1])
        