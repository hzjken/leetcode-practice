class Solution:
    def solve(self, board, word):
        if word == '':
            return True

        if board == [[]] or board == []:
            return False

        self.board = board
        self.word = word
        self.output = False
        self.stack = []
        self.visited = set()

        self.row_len = len(board)
        self.col_len = len(board[0])

        for row in range(self.row_len):
            for col in range(self.col_len):
                if board[row][col] == word[0]:
                    self.stack.append((row, col))
                    self.visited.add((row, col))
                    self.DFS(1)

        return self.output
                    

    def DFS(self, i):
        if self.word[i:] == '':
            self.output = True
        else:
            letter = self.word[i]
            row, col = self.stack[-1]
            if 0 <= row-1 < self.row_len and (row-1,col) not in self.visited and self.board[row-1][col] == letter:
                self.stack.append((row-1,col))
                self.visited.add((row-1,col))
                self.DFS(i+1)
            if 0 <= row+1 < self.row_len and (row+1,col) not in self.visited and self.board[row+1][col] == letter:
                self.stack.append((row+1,col))
                self.visited.add((row+1,col))
                self.DFS(i+1)
            if 0 <= col-1 < self.col_len and (row,col-1) not in self.visited and self.board[row][col-1] == letter:
                self.stack.append((row,col-1))
                self.visited.add((row,col-1))   
                self.DFS(i+1)
            if 0 <= col+1 < self.col_len and (row,col+1) not in self.visited and self.board[row][col+1] == letter:
                self.stack.append((row,col+1))
                self.visited.add((row,col+1))
                self.DFS(i+1)
            
        pop = self.stack.pop()
        self.visited.remove(pop)

board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

s = Solution()
print(s.solve(board, 'ABCCED'))
print(s.solve(board, 'SEE'))
print(s.solve(board, 'ABCB'))
print(s.solve(board, 'ABCF'))