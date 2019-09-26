class Solution:
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if mid-1 >= 0 and mid+1 < len(nums):
                if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                    return mid
                elif nums[mid-1] < nums[mid] < nums[mid+1]:
                    left = mid + 1
                elif nums[mid-1] > nums[mid] > nums[mid+1]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif mid-1 >= 0:
                if nums[mid-1] < nums[mid]:
                    return mid
                else:
                    right = mid - 1
            else:
                if nums[mid+1] < nums[mid]:
                    return mid
                else:
                    left = mid + 1


s = Solution()
print(s.findPeakElement([1,2,3,1]))