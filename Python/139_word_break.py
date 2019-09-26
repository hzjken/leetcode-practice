class Solution:
    def wordBreak(self, s, wordDict):
        if s == '' or wordDict == []:
            return False
        
        len_list = [len(i) for i in wordDict]
        min_len = min(len_list)
        max_len = max(len_list)
        wordDict = set(wordDict)
        output = [True] + [False] * len(s)
        
        for i in range(1, len(s)+1):
            ok = False
            for span in range(min_len, max_len+1):
                if i - span >= 0:
                    ok = output[i-span] and s[i-span:i] in wordDict
                    if ok:
                        output[i] = ok
                        break
        
        return output[-1]


s = Solution()
print(s.wordBreak('leetcode', ['leet', 'code']))
        