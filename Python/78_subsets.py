class Solution:
    def subsets(self, nums):
        if nums == []:
            return []
        
        output = []
        queue = [([], 0)]
        while queue != []:
            comb, pos = queue.pop(0)
            output.append(comb)
            for i in range(pos, len(nums)):
                new_comb = comb.copy()
                new_comb.append(nums[i])
                queue.append((new_comb, i+1))
        
        return output
            

s = Solution()
print(s.subsets([1,4,5,3]))