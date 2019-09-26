class Solution:
    def groupAnagrams(self, strs):
        ana_dict = {}
        for word in strs:
            letter_dict = {}
            for i in word:
                if i not in letter_dict:
                    letter_dict[i] = 1
                else:
                    letter_dict[i] += 1
            
            letter_list = [(key,str(val)) for key, val in letter_dict.items()]
            letter_list = sorted(letter_list, key= lambda x:x[0])
            letter_str = ''.join([''.join(i) for i in letter_list])
            
            if word not in ana_dict:
                ana_dict[word] = (letter_str, 1)
            else:
                ana_dict[word] = (ana_dict[word][0], ana_dict[word][1]+1)
        
        output_dict = {}
        for key, val in ana_dict.items():
            if val[0] not in output_dict:
                output_dict[val[0]] = [key] * val[1]
            else:
                output_dict[val[0]] += [key] * val[1]
        
        return list(output_dict.values())


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))