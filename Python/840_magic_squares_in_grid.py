class Solution:
    def numMagicSquaresInside(self, grid):
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        
        output = 0
        for start_row in range(len(grid)-2):
            for start_col in range(len(grid[0])-2):
                distinct_set = set()
                col_sum = [0] * 3
                row_sum = [0] * 3
                diag_sum = [0] * 2
                for row in range(start_row, start_row+3):
                    for col in range(start_col, start_col+3):
                        distinct_set.add(grid[row][col])
                        col_sum[col % 3] += grid[row][col]
                        row_sum[row % 3] += grid[row][col]
                        if row - start_row == col - start_col:
                            diag_sum[0] += grid[row][col]
                        if row - start_row + col - start_col == 2:
                            diag_sum[1] += grid[row][col]
                            
                if distinct_set == set(range(1,10)) and all([i == 15 for i in col_sum]) and all([i == 15 for i in row_sum]) and all([i == 15 for i in diag_sum]):
                    output += 1
        
        return output
        

s = Solution()
print(s.numMagicSquaresInside(
    [[4,3,8,4],
    [9,5,1,9],
    [2,7,6,2]]
))