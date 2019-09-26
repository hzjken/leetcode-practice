class Solution:
    def floodFill(self, image, sr, sc, newColor):
        origin_val = image[sr][sc]
        queue = [(sr, sc)]
        unvisited = set()
        for row in range(len(image)):
            for col in range(len(image[0])):
                unvisited.add((row, col))
        
        while queue != []:
            row, col = queue.pop(0)
            if 0 <= row < len(image) and 0 <= col < len(image[0]):
                if (row, col) in unvisited:
                    if image[row][col] == origin_val:
                        image[row][col] = newColor
                        queue.append((row-1, col))
                        queue.append((row+1, col))
                        queue.append((row, col-1))
                        queue.append((row, col+1))
                        unvisited.remove((row, col))
        
        return image
                

s = Solution()
print(s.floodFill(
    [[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2
))