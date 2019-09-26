class Solution:
    def detectCapitalUse(self, word):
        if len(word) <= 1:
            return True
        
        start_cap = word[0].isupper()
        all_cap = word[1].isupper()
        
        if not start_cap:
            for i in range(len(word)):
                if word[i].isupper():
                    return False
        else:
            if not all_cap:
                for i in range(1, len(word)):
                    if word[i].isupper():
                        return False
            else:
                for i in range(1, len(word)):
                    if not word[i].isupper():
                        return False
        
        return True


s = Solution()
print(s.detectCapitalUse("FlaG"))