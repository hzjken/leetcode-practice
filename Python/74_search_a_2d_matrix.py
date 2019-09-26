class Solution:
    def searchMatrix(self, matrix, target):
        '''binary search'''
        if matrix == [] or matrix == [[]]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        left = 0
        right = m*n-1
        
        while left <= right:
            mid = (left + right) // 2
            mid_row = mid // n
            mid_col = mid % n
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False

    def searchMatrix2(self, matrix, target):
        '''binary search separately on row and column'''
        if matrix == [] or matrix == [[]]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        left = 0
        right = m-1
        
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        if matrix[mid][0] < target:
            row = mid
        else:
            if mid > 0:
                row = mid - 1
            else:
                return False
        
        left = 0
        right = n-1
        
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return False


s = Solution()
print(s.searchMatrix(
    [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], target = 3
))
print(s.searchMatrix2(
    [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], target = 3
))