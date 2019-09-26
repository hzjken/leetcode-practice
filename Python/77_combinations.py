class Solution:
    def combine(self, n, k):
        output = []
        queue = [([], k)]
        while queue != []:
            comb, k = queue.pop(0)
            if k == 0:
                output.append(comb)
            if k > 0:
                if comb == []:
                    for i in range(1, n+1):
                        new_comb = comb.copy()
                        new_comb.append(i)
                        new_k = k - 1
                        queue.append((new_comb, new_k))
                else:
                    for i in range(comb[-1]+1, n+1):
                        new_comb = comb.copy()
                        new_comb.append(i)
                        new_k = k - 1
                        queue.append((new_comb, new_k))
        
        return output


s = Solution()
print(s.combine(5,3))