class Solution:
    def findJudge(self, N, trust):
        judges = set(range(1, N+1))
        trustee_dict = {i:0 for i in range(1, N+1)}
        
        for truster, trustee in trust:
            if truster in judges:
                judges.remove(truster)
            trustee_dict[trustee] += 1
        
        trustee_set = set([i for i in trustee_dict if trustee_dict[i] == N-1])
        output = trustee_set & judges
        
        if len(output) == 0:
            return -1
        else:
            return output.pop()


s = Solution()
print(s.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))
