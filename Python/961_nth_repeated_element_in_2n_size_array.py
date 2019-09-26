class Solution:
    def repeatedNTimes(self, A):
        num_set = set(A)
        for i in A:
            if i in num_set:
                num_set.remove(i)
            else:
                return i