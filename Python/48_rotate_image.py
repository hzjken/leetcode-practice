class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix == [] or matrix == [[]]:
            return matrix
        
        n = len(matrix)
        non_visited = set()
        for row in range(n):
            for col in range(n):
                non_visited.add((row, col))
                
        while len(non_visited) != 0:
            row, col = non_visited.pop()
            non_visited.add((row, col))
            temp1 = matrix[row][col]
            while True:
                new_row = col
                new_col = n - row - 1
                if (new_row, new_col) in non_visited:
                    non_visited.remove((new_row, new_col))
                else:
                    break
                
                temp2 = matrix[new_row][new_col]  
                matrix[new_row][new_col] = temp1
                temp1 = temp2
                row = new_row
                col = new_col
                
        return matrix
                

s = Solution()
print(
    s.rotate(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    )
)