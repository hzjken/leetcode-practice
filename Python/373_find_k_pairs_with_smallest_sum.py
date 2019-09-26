class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        '''direct heap'''
        if k == 0:
            return []
        if nums1 == [] or nums2 == []:
            return []
        
        import heapq
        output = []
        
        for row in range(len(nums1)):
            for col in range(len(nums2)):
                heapq.heappush(output, (-(nums1[row] + nums2[col]), [nums1[row], nums2[col]]))
                if len(output) > k:
                    heapq.heappop(output)
                
        return [i[1] for i in output]
                    

class Solution2:
    def kSmallestPairs(self, nums1, nums2, k):
        '''BFS with heap'''
        if k == 0:
            return []
        if nums1 == [] or nums2 == []:
            return []
        
        import heapq
        queue = [(nums1[0] + nums2[0], (0, 0))]
        output = []
        visited = set()
        
        while len(output) < k and queue != []:
            _, result = heapq.heappop(queue)
            if result not in visited:
                visited.add(result)
                row, col = result
                output.append([nums1[row], nums2[col]])
                if row + 1 < len(nums1):
                    heapq.heappush(queue, (nums1[row+1]+nums2[col], (row+1, col)))
                if col + 1 < len(nums2):
                    heapq.heappush(queue, (nums1[row]+nums2[col+1], (row, col+1)))
        
        return output
                
s = Solution()
s2 = Solution2()
print(s.kSmallestPairs([1,7,11],[2,4,6],3))
print(s2.kSmallestPairs([1,7,11],[2,4,6],3))