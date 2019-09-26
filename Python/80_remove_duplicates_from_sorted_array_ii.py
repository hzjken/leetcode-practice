class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)
        
        prev = 0
        pointer = 0
        
        while pointer < len(nums):
            if nums[pointer] == nums[prev]:
                if pointer - prev > 1:
                    nums.pop(pointer)
                else:
                    pointer += 1
            else:
                prev = pointer
                pointer += 1
        
        return nums


s = Solution()
print(s.removeDuplicates([1,1,1,2,3,4,4,4,4,5,5,5,5,5,6,7]))