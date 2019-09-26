class Solution:
    def validMountainArray(self, A):
        if len(A) < 3:
            return False
        
        output = True
        go_down = False
        for i in range(1, len(A)):
            if not go_down:
                if A[i] > A[i-1]:
                    pass
                elif A[i] == A[i-1]:
                    return False
                else:
                    go_down = True
                    if i == 1:
                        return False
            
            else:
                if A[i] < A[i-1]:
                    pass
                else:
                    return False
        
        return output and go_down


s = Solution()
print(s.validMountainArray([0,3,2,1]))
