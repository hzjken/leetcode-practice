class Solution:
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        
        output = []
        nums = sorted(nums)

        first_set = set()
        for first in range(len(nums)-3):
            if nums[first] not in first_set:
                first_set.add(nums[first])
                sec_set = set()
                for sec in range(first+1, len(nums)-2):
                    if nums[sec] not in sec_set:
                        sec_set.add(nums[sec])

                        check_dict = {}
                        output_already = set()
                        for third in range(sec+1, len(nums)):
                            if nums[third] not in output_already:
                                if nums[third] not in check_dict:
                                    check_dict[target - nums[first] - nums[sec] - nums[third]] = nums[third]
                                else:
                                    output.append([nums[first], nums[sec], nums[third], check_dict[nums[third]]])
                                    output_already |= {nums[third], check_dict[nums[third]]}
        return output


s = Solution()
print(s.fourSum([0, 0, -3, 3 ,-3, 3, 0, 3,-3], 0))