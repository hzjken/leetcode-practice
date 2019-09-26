class Solution:
    def largestTriangleArea(self, points):
        
        output = 0
        for a in range(len(points)-2):
            for b in range(a+1, len(points)-1):
                for c in range(b+1, len(points)):
                    output = max(output, self.cal_area(points[a],points[b],points[c]))
        
        return output
        
    def cal_area(self, a, b, c):
        ab = [b[0]-a[0], b[1]-a[1]]
        ac = [c[0]-a[0], c[1]-a[1]]
        ab_len = (ab[0] ** 2 + ab[1] ** 2) ** 0.5
        ac_len = (ac[0] ** 2 + ac[1] ** 2) ** 0.5
        projection_len = (ab[0]*ac[0]+ab[1]*ac[1]) / ab_len
        height = abs((ac_len ** 2 - projection_len ** 2)) ** 0.5
        area = ab_len * height / 2
        
        return area


s = Solution()
print(s.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))