class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        rect_down = max(B, F)
        rect_up = min(H, D)
        rect_left = max(A, E)
        rect_right = min(C, G)
        
        if rect_up > rect_down and rect_right > rect_left:
            overlap = (rect_up - rect_down) * (rect_right - rect_left)
        else:
            overlap = 0
            
        rect1_area = (D-B) * (C-A)
        rect2_area = (H-F) * (G-E)
        
        return rect1_area + rect2_area - overlap


s = Solution()
print(s.computeArea(A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2))