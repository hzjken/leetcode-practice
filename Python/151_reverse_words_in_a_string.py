class Solution:
    def reverseWords(self, s):
        output = []
        word = ''
        for i in s:
            if i == ' ':
                if word != '':
                    output.append(word)
                word = ''
            else:
                word += i
                
        if word != '':
            output.append(word)
        
        return ' '.join(reversed(output))


class Solution2:
    def reverseWords(self, s):
        if s == '':
            return s
        
        s = [i for i in s]
        s.append(' ')
        start = 0
        move = 0
        
        while start + move < len(s):
            if s[start + move] == ' ':
                if move == 0:
                    s.pop(start)
                else:
                    new_start = start + move + 1
                    stop = start + move - 1
                    while start < stop:
                        s[start], s[stop] = s[stop], s[start]
                        start += 1
                        stop -= 1

                    start = new_start
                    move = 0
                
            else:
                move += 1
        
        if len(s) != 0:
            s.pop()
        return ''.join(s[::-1])


s = Solution()
s2 = Solution2()
print(s.reverseWords("the sky is blue"))
print(s2.reverseWords("the sky is blue"))

