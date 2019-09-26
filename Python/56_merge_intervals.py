class Solution:
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals
        
        intervals = sorted(intervals, key= lambda x:x[1])
        
        output = []
        while intervals != []:
            start, end = intervals.pop(0)
            if output == []:
                output.append([start, end])
            else:
                while output != [] and start <= output[-1][1]:
                    start = min(start, output[-1][0])
                    output.pop()
                output.append([start, end])
                
        return output
        

s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))