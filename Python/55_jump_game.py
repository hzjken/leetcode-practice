class Solution:
    def canJump(self, nums):
        if nums == []:
            return False
        if len(nums) == 1:
            return True
        
        reached = [0]
        max_point = 0
        
        while reached != []:
            point = reached.pop(0)
            if point + nums[point] <= max_point:
                pass
            else:
                new_max_point = min(point + nums[point], len(nums)-1)
                reached += list(range(max_point+1, new_max_point+1))
                max_point = new_max_point
                
            if max_point == len(nums) - 1:
                return True
        
        return False


s = Solution()
print(s.canJump([2,3,1,1,4]))