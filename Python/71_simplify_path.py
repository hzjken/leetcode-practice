class Solution:
    def simplifyPath(self, path):
        
        split = path.split('/')
        stack = []
        for i in split:
            if i == '' or i == '.':
                pass
            elif i == '..':
                if stack != []:
                    stack.pop()
            else:
                stack.append(i)
        
        return '/' + '/'.join(stack)


s = Solution()
print(s.simplifyPath('/a/../../b/../c//.//'))