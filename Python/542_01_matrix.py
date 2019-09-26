class Solution:
    def solve(self, matrix):

        self.matrix = matrix
        self.row_len = len(matrix)
        self.col_len = len(matrix[0])
        self.output = [[None] * self.col_len for i in range(self.row_len)]
        self.queue = []

        for row in range(self.row_len):
            for col in range(self.col_len):
                if self.matrix[row][col] == 0:
                    self.queue.append((row,col))
                    self.output[row][col] = 0
        
        while self.queue != []:
            row, col = self.queue.pop(0)
            self.helper(row-1, col, row, col)
            self.helper(row+1, col, row, col)
            self.helper(row, col-1, row, col)
            self.helper(row, col+1, row, col)

        return self.output

    def helper(self, row, col, prev_row, prev_col):
        if 0 <= row < self.row_len and 0 <= col < self.col_len:
            if self.output[row][col] is None or self.output[row][col] > self.output[prev_row][prev_col]+1:
                self.output[row][col] = self.output[prev_row][prev_col] + 1
                self.queue.append((row, col))
                        
            
s = Solution()
print(
    s.solve(
        [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]
    )
)
