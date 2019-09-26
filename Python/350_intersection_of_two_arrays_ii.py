class Solution:
    def intersect(self, nums1, nums2):
        dict1 = {}
        dict2 = {}
        output = []
        
        for i in nums1:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        
        for i in nums2:
            if i not in dict2:
                dict2[i] = 1
            else:
                dict2[i] += 1
                
        for i in dict1:
            if i in dict2:
                times = min(dict1[i], dict2[i])
                for _ in range(times):
                    output.append(i)
                    
        return output


s = Solution()
print(s.intersect([4,9,5], [9, 4, 9, 8, 4]))