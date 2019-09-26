class Solution:
    def fairCandySwap(self, A, B):
        sum_diff = (sum(A) - sum(B)) // 2
        set_a = set(A)
        set_b = set(B)
        for i in set_a:
            if i - sum_diff in set_b:
                return [i, i - sum_diff]


s = Solution()
print(s.fairCandySwap([1,2,5],[2,4]))