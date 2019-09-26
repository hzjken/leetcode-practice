class Solution:
    def longestPalindrome(self, s):
        letter_dict = {}
        for i in s:
            if i not in letter_dict:
                letter_dict[i] = 1
            else:
                letter_dict[i] += 1
        
        output = 0
        choose_one = False
        for val in letter_dict.values():
            if val > 1:
                output += (val // 2) * 2
            if val % 2 == 1:
                if not choose_one:
                    output += 1
                    choose_one = True
        
        return output
            

s = Solution()
print(s.longestPalindrome("abccccdd"))