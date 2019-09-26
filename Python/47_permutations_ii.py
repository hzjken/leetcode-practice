class Solution:
    def permuteUnique(self, nums):
        if nums == []:
            return []
        
        non_visited = {}
        for i in nums:
            if i not in non_visited:
                non_visited[i] = 1
            else:
                non_visited[i] += 1
                
        queue = [([], non_visited)]
        output = []
        
        while queue != []:
            perm, non_visited = queue.pop(0)
            sum_zero = True
            for key, val in non_visited.items():
                if val != 0:
                    sum_zero = False
                    new_perm = perm.copy()
                    new_perm.append(key)
                    new_non_visited = non_visited.copy()
                    new_non_visited[key] = val - 1
                    queue.append((new_perm, new_non_visited))
            
            if sum_zero:
                output.append(perm)
                
        return output
        

s = Solution()
print(s.permuteUnique([1,1,2]))