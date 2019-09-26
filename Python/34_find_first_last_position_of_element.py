class Solution:
    def searchRange(self, nums, target):
        if nums == []:
            return [-1, -1]
        elif len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        left_point = mid + 1 if nums[mid] != target else mid
        left = left_point
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
                
        right_point = mid - 1 if nums[mid] != target else mid
        
        if left_point > right_point:
            return [-1, -1]
        elif left_point == right_point:
            if nums[left_point] == target:
                return [left_point, right_point]
            else:
                return [-1, -1]
        else:
            return [left_point, right_point]
                