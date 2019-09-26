class Solution:
    def partition(self, s):
        if s == '':
            return []
        
        self.stack = []
        self.output = []
        self.s = s
        self.recur(0)
        return self.output
    
    def recur(self, start_pos):
        if start_pos == len(self.s):
            self.output.append(self.stack.copy())
        else:
            for i in range(start_pos+1, len(self.s)+1):
                string = self.s[start_pos:i]
                if string == string[::-1]:

                    self.stack.append(string)
                    self.recur(i)
                    self.stack.pop()


s = Solution()
print(s.partition("aab"))