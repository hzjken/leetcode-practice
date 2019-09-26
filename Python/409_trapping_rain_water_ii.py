import copy

class Solution:
    def trapRainWater(self, heightMap):
        if heightMap == [[]]:
            return 0
        
        output = 0
        water_height = copy.deepcopy(heightMap)
        for row in range(len(heightMap)):
            leftmax = heightMap[row][0]
            rightmax = heightMap[row][-1]
            for col in range(len(heightMap[0])):
                water_height[row][col] = leftmax
                leftmax = max(leftmax, heightMap[row][col])

            for col in reversed(range(len(heightMap[0]))):
                water_height[row][col] = min(water_height[row][col], rightmax)
                rightmax = max(rightmax, heightMap[row][col])
        print(water_height)

        for col in range(len(heightMap[0])):
            upmax = heightMap[0][col]
            downmax = heightMap[-1][col]
            for row in range(len(heightMap)):
                water_height[row][col] = min(water_height[row][col], upmax)
                upmax = max(upmax, heightMap[row][col])


            for row in reversed(range(len(heightMap))):
                water_height[row][col] = min(water_height[row][col], downmax)
                downmax = max(downmax, heightMap[row][col])

                
        for row in range(len(heightMap)):
            for col in range(len(heightMap[0])):
                output += max(0, water_height[row][col] - heightMap[row][col])
        
        return output

s = Solution()
a = s.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]])

print(a)