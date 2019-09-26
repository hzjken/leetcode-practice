class Solution:
    def evalRPN(self, tokens):
        output = []
        operator = {'+', '-', '*', '/'}
        
        for i in tokens:
            if i not in operator:
                output.append(int(i))
            else:
                latter = output.pop()
                former = output.pop()
                if i == '+':
                    result = former + latter
                elif i == '-':
                    result = former - latter
                elif i == '*':
                    result = former * latter
                else:
                    result = int(former / latter)
                output.append(result)
        
        return output[-1]


s = Solution()
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
