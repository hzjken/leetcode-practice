class Solution:
    def spiralOrder(self, matrix):
        if matrix == [] or matrix == [[]]:
            return matrix
        
        move_direction = [(0,1), (1,0), (0,-1), (-1,0)]
        output = []
        
        non_visited = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                non_visited.add((row, col))
        
        pos = 0
        row = 0
        col = 0
        while len(non_visited) != 0:
            if (row, col) in non_visited:
                output.append(matrix[row][col])
                non_visited.remove((row, col))
            row_change, col_change = move_direction[pos % 4]
            
            if (row + row_change, col + col_change) in non_visited:
                row += row_change
                col += col_change
            else:
                pos += 1

        return output


s = Solution()
print(s.spiralOrder(
    [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
))