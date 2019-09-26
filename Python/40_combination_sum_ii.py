class Solution:
    def combinationSum2(self, candidates, target):
        if candidates == []:
            return []
        
        candidates = sorted(candidates)
        
        output = []
        queue = []
        for i, val in enumerate(candidates):
            add = ([val], i, val)
            if queue == [] or queue[-1][0] != add[0]:
                queue.append(add)
        
        while queue != []:
            vals, index, sumup = queue.pop(0)
            if sumup == target:
                output.append(vals)
            elif sumup > target:
                pass
            else:
                for i in range(index+1, len(candidates)):
                    new_vals = vals.copy()
                    new_vals.append(candidates[i])
                    sumup = sum(new_vals)
                    add = (new_vals, i, sumup)
                    if queue == [] or queue[-1][0] != add[0]:
                        queue.append(add)
            
        return output

    
s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))