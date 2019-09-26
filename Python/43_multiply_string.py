class Solution:
    def multiply(self, num1, num2):
        output = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                multiply = int(num1[i]) * int(num2[j])
                pos = i + j + 1
                output[pos] += multiply
        
        for i in reversed(range(len(output))):
            val = output[i]
            output[i] = val % 10
            output[i-1] += val // 10
        
        s = ''
        start_zero = True
        for i in output:
            if start_zero:
                if i != 0:
                    start_zero = False
                    s += str(i)
            else:
                s += str(i)
        
        return s if s != '' else '0'


s = Solution()
print(s.multiply('392', '184'))