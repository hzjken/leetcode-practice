class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == []:
            return []
        
        left = 0
        right = len(nums) - 1
        
        while 0 <= left < len(nums) and nums[left] == 0:
                left += 1
        while 0 <= right < len(nums) and nums[right] == 2:
            right -= 1

        pointer = left
        while pointer <= right:
            if nums[pointer] == 1:
                pointer += 1
            elif nums[pointer] == 0:
                nums[pointer], nums[left] = nums[left], nums[pointer]
                left += 1
            else:
                nums[pointer], nums[right] = nums[right], nums[pointer]
                right -= 1
                
            pointer = max(left, pointer)
        
        return nums
            

s = Solution()
print(s.sortColors([0,2,1,0,1,1,2,1,0,1,0]))
            
                