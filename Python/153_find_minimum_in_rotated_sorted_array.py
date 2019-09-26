class Solution:
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        left = 0
        right = len(nums) - 1
        
        output = None
        
        while left <= right:
            mid = (left + right) // 2
            
            if output is not None:
                output = min(output, nums[mid])
            else:
                output = nums[mid]
            
            if nums[right] < nums[left] < nums[mid]:
                left = mid + 1
            elif nums[mid] < nums[right] < nums[left]:
                right = mid - 1
            elif nums[left] == nums[mid]:
                left = mid + 1
            else:
                if output is not None:
                    output = min(output, nums[left])
                else:
                    output = nums[left]
                break

        return output


s = Solution()
print(s.findMin([4,5,6,7,0,1,2]))