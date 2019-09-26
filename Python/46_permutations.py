class Solution:
    def permute(self, nums):
        non_visited = set(nums)
        queue = [([], non_visited)]
        output = []

        while queue != []:
            perm, non_visited = queue.pop(0)
            if len(non_visited) == 0:
                output.append(perm)
            else:
                for i in non_visited:
                    new_perm = perm.copy()
                    new_perm.append(i)
                    new_non_visited = non_visited.copy()
                    new_non_visited.remove(i)
                    queue.append((new_perm, new_non_visited))
        
        return output

s = Solution()
print(s.permute([1,2,3]))