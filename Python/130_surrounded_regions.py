class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if board == [] or board == [[]]:
            pass
        else:
            non_visited = set()
            queue = []
            for row in range(len(board)):
                for col in range(len(board[0])):
                    non_visited.add((row, col))
                    if (row == 0 or col == 0 or row == len(board)-1 or col == len(board[0])-1) and board[row][col] == 'O':
                        queue.append((row,col))
            
            while queue != []:
                row, col = queue.pop(0)
                if (row, col) in non_visited:
                    non_visited.remove((row, col))
                    self.helper(row-1, col, queue, board)
                    self.helper(row+1, col, queue, board)
                    self.helper(row, col-1, queue, board)
                    self.helper(row, col+1, queue, board)
            
            while len(non_visited) != 0:
                row, col = non_visited.pop()
                if board[row][col] == 'O':
                    board[row][col] = 'X'
        
        return board
                
    
    def helper(self, row, col, queue, board):
        if 0 <= row < len(board) and 0 <= col < len(board[0]):
            if board[row][col] == 'O':
                queue.append((row, col))


s = Solution()
print(s.solve(
    [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
))