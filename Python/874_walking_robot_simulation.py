class Solution:
    def robotSim(self, commands, obstacles):
        obs = set([(i[0], i[1]) for i in obstacles])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        current_direct = 0
        current_pos = [0,0]
        output = 0
        
        for cmd in commands:
            if cmd == -2:
                current_direct = (current_direct - 1) % 4
            elif cmd == -1:
                current_direct = (current_direct + 1) % 4
            else:
                for _ in range(cmd):
                    row_dir, col_dir = directions[current_direct]
                    if (current_pos[0]+row_dir, current_pos[1]+col_dir) in obs:
                        break
                    else:
                        current_pos[0] += row_dir
                        current_pos[1] += col_dir
            
            output = max(output, current_pos[0] ** 2 + current_pos[1] ** 2)
        
        return output
        

s = Solution()
print(s.robotSim([4,-1,4,-2,4],[[2,4]]))