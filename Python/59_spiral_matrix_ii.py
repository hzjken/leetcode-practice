class Solution:
    def generateMatrix(self, n):
        if n == 1:
            return [[1]]
        
        matrix = [[None] * n for _ in range(n)]
        direction = [(0,1), (1,0), (0, -1), (-1, 0)]
        non_visited = set()
        for row in range(n):
            for col in range(n):
                non_visited.add((row, col))
                
        row = 0
        col = 0
        matrix[row][col] = 1
        non_visited.remove((row, col))
        pos = 0
        i = 2
        
        while len(non_visited) != 0:
            
            row_change, col_change = direction[pos % 4]
            
            if (row + row_change, col + col_change) in non_visited:
                row += row_change
                col += col_change
                matrix[row][col] = i
                non_visited.remove((row, col))
                i += 1
            else:
                pos += 1
        
        return matrix


s = Solution()
print(s.generateMatrix(3))