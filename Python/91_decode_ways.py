class Solution:
    def numDecodings(self, s):
        '''BFS'''
        if s == '':
            return 0
        
        output = 0
        queue = [0]
        
        while queue != []:
            index = queue.pop(0)
            if index == len(s):
                output += 1
            for i in [2,1]:
                val = s[index: index+i]
                if val != '' and val[0] != '0' and 0 < int(val) <= 26:
                    queue.append(index+i)
        
        return output


class Solution2:
    def numDecodings(self, s):
        '''DP'''
        if s == '':
            return 0
        
        self.dp = {0: 1}
        self.s = s
        if s[0] != '0':
            self.dp[1] = 1
        else:
            self.dp[1] = 0
            
        return self.recur(len(s))
        
    def recur(self, length):
        if length in self.dp:
            return self.dp[length]
        if length < 0:
            return 0
        else:
            first_s = self.s[length-1: length]
            second_s = self.s[length-2: length]
            if first_s != '' and first_s[0] != '0' and 0 < int(first_s) <= 26:  
                first = self.recur(length - 1) 
            else:
                first = 0
            if second_s != '' and second_s[0] != '0' and 0 < int(second_s) <= 26:  
                second = self.recur(length - 2)
            else:
                second = 0
            self.dp[length] = first + second
            return self.dp[length]


s = Solution()
s2 = Solution2()
print(s.numDecodings('12351331'))
print(s2.numDecodings('12351331'))