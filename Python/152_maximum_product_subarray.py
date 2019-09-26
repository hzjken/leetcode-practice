class Solution:
    def maxProduct(self, nums):
        if nums == []:
            return None
        
        output = None
        max_val = None
        min_val = None
        
        for i in nums:
            if max_val is None and min_val is None:
                min_val = i
                max_val = i
            else:
                min_temp = min(i, min_val*i, max_val*i)
                max_temp = max(i, min_val*i, max_val*i)
                min_val = min_temp
                max_val = max_temp
            
            if output:
                output = max(output, max_val)
            else:
                output = max_val
                
        return output


s = Solution()
s.maxProduct([-2, 0, -1])