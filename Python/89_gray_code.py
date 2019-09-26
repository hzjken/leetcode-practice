class Solution:
    def grayCode(self, n):
        if n == 0:
            return [0]
        
        output = [0]
        current = ['0'] * n
        visited = {''.join(current)}
        
        for _ in range(2**n - 1):
            digit = 0
            for _ in range(n):
                new_val = current.copy()
                if new_val[digit] == '0':
                    new_val[digit] = '1'
                else:
                    new_val[digit] = '0'
                if ''.join(new_val) not in visited:
                    output.append(int(''.join(new_val), 2))
                    visited.add(''.join(new_val))
                    current = new_val
                    break
                else:
                    digit += 1
                
        return output

s = Solution()
print(s.grayCode(4))