class Solution:
    def isValidSudoku(self, board):
        row_check = [[] for _ in range(9)]
        col_check = [[] for _ in range(9)]
        square_check = [[] for _ in range(9)]
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != '.':
                    row_check[row].append(board[row][col])
                    col_check[col].append(board[row][col])
                    square_check[3*(row//3)+(col//3)].append(board[row][col])

        output = True
        for check in row_check:
            if len(set(check)) != len(check):
                return False
        for check in col_check:
            if len(set(check)) != len(check):
                return False
        for check in square_check:
            if len(set(check)) != len(check):
                return False
                
        return output

s = Solution()
row_check, col_check, square_check = s.isValidSudoku(
    [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
)
