class Solution:
    def search(self, nums, target):
        if nums == []:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            else:
                if nums[left] < nums[mid]:
                    if nums[left] == target:
                        return left
                    elif nums[left] < target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if nums[right] == target:
                        return right
                    elif nums[mid] < target < nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
        
        return -1