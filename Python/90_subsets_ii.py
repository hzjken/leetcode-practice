class Solution:
    def subsetsWithDup(self, nums):
        if nums == []:
            return [[]]
        
        nums = sorted(nums)
        prev = None
        queue = [([], -1)]
        output = [[]]
        
        while queue != []:
            subset, index = queue.pop(0)
            for i in range(index+1, len(nums)):
                if not prev or prev != nums[i]:
                    new_set = subset.copy()
                    new_set.append(nums[i])
                    output.append(new_set)
                    queue.append((new_set, i))
                    prev = nums[i]
            prev = None
            
        return output
                