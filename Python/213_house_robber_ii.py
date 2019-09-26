class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        
        list1 = [None] * len(nums)
        list2 = [None] * len(nums)
        
        list1[0] = nums[0]
        list1[1] = nums[0]
        for i in range(2, len(nums)-1):
            list1[i] = max(list1[i-1], list1[i-2] + nums[i])
        list1[-1] = list1[-2]
        
        list2[0] = 0
        list2[1] = nums[1]
        for i in range(2, len(nums)):
            list2[i] = max(list2[i-1], list2[i-2] + nums[i])
        
        return max(list1[-1], list2[-1])


s = Solution()
print(s.rob([1,2,3,1]))