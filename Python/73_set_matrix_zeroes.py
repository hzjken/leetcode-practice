class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_0 = False
        first_col_0 = False
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row == 0 and col == 0:
                    if matrix[row][col] == 0:
                        first_row_0 = True
                        first_col_0 = True
                elif row == 0 and col != 0:
                    if matrix[row][col] == 0:
                        first_row_0 = True
                elif row != 0 and col == 0:
                    if matrix[row][col] == 0:
                        first_col_0 = True
                else:
                    if matrix[row][col] == 0:
                        matrix[row][0] = 0
                        matrix[0][col] = 0
        
        for row in range(1, len(matrix)):
            if matrix[row][0] == 0:
                for col in range(len(matrix[0])):
                    matrix[row][col] = 0
        
        for col in range(1, len(matrix[0])):
            if matrix[0][col] == 0:
                for row in range(len(matrix)):
                    matrix[row][col] = 0
                    
        if first_row_0:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
        
        if first_col_0:
            for row in range(len(matrix)):
                matrix[row][0] = 0
                
        return matrix
        
        
s = Solution()
print(s.setZeroes(
    [
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ]
))