class Solution:
    def canPartition(self, nums):
        if nums == []:
            return False
        
        sumup = sum(nums)
        if sumup % 2 == 1:
            return False
        
        max_row = len(nums) + 1
        max_col = sumup // 2 + 1
        dp = [[None] * max_col for _ in range(max_row)]
        
        for row in range(max_row):
            dp[row][0] = True
        for col in range(max_col):
            dp[0][col] = False

        for row in range(1, max_row):
            for col in range(1, max_col):
                first = dp[row-1][col]
                second = dp[row-1][col - nums[row-1]] if col - nums[row-1] >= 0 else False
                dp[row][col] = first or second
        
        return dp[max_row-1][max_col-1]

s = Solution()
print(s.canPartition([1, 2, 5]))
print(s.canPartition([1, 5, 11, 5]))


class Solution1:
    def minDiffPartition(self, nums):
        if nums == []:
            return [[], []]
        
        half_sum = sum(nums) // 2

        
        max_row = len(nums) + 1
        max_col = half_sum + 1
        dp = [[None] * max_col for _ in range(max_row)]
        
        for row in range(max_row):
            dp[row][0] = True
        for col in range(max_col):
            dp[0][col] = False

        for row in range(1, max_row):
            for col in range(1, max_col):
                first = dp[row-1][col]
                second = dp[row-1][col - nums[row-1]] if col - nums[row-1] >= 0 else False
                dp[row][col] = first or second
        
        for min_diff_sum in reversed(range(half_sum+1)):
            if dp[max_row-1][min_diff_sum] == 1:
                break
        
        first_part = []
        for i in reversed(range(1, max_row)):
            if dp[i-1][min_diff_sum-nums[i-1]]:
                first_part.append(nums[i-1])
                min_diff_sum -= nums[i-1]
            else:
                pass
        
        second_part = nums.copy()
        for i in first_part:
            second_part.remove(i)
        
        return [first_part, second_part]


s = Solution1()
print(s.minDiffPartition([3,5,11,5,1]))