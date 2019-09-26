class Solution:
    def search(self, nums, target):
        if nums == []:
            return False
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] == target:
                return True
            if nums[right] == target:
                return True
            
            if nums[left] < nums[mid]:
                if nums[left] < target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] > nums[mid]:
                if nums[mid] < target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    left += 1
                    right -= 1
            
        return False


s = Solution()
print(s.search([2,5,6,0,0,1,2], 3))