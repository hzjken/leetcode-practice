class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == []:
            return []

        start = -1
        for i in reversed(range(1, len(nums))):
            if nums[i] > nums[i - 1]:
                start = i - 1
                break

        if start == -1:
            pass
        else:
            for i in reversed(range(start + 1, len(nums))):
                if nums[start] < nums[i]:
                    nums[start], nums[i] = nums[i], nums[start]
                    break

        left = start + 1
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums


s = Solution()
print(s.nextPermutation([1,3,2]))