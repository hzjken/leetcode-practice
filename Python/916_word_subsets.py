class Solution:
    def solve(self, a_list, b_list):
        if a_list == [] or b_list == []:
            return []

        output = []

        max_dict = self.max_dict(b_list)
        for word in a_list:
            count_dict = {}
            select = True

            for i in word:
                if i not in count_dict:
                    count_dict[i] = 1
                else:
                    count_dict[i] += 1
            
            for key in max_dict:
                if key not in count_dict or count_dict[key] < max_dict[key]:
                    select = False
                    break
            
            if select:
                output.append(word)
        
        return output

    def max_dict(self, b_list):
        output = {}
        for word in b_list:
            temp_dict = {}
            for i in word:
                if i not in temp_dict:
                    temp_dict[i] = 1
                else:
                    temp_dict[i] += 1
            
            for j in temp_dict:
                if j not in output:
                    output[j] = temp_dict[j]
                else:
                    output[j] = max(output[j], temp_dict[j])
        
        return output    

s = Solution()
A = ['amazon', 'apple', 'facebook', 'google', 'leetcode']
B = ['e', 'o']
print(s.solve(A, B))
A = ['amazon', 'apple', 'facebook', 'google', 'leetcode']
B = ['l', 'e']
print(s.solve(A, B))
A = ['amazon', 'apple', 'facebook', 'google', 'leetcode']
B = ['e', 'oo']
print(s.solve(A, B))
A = ['amazon', 'apple', 'facebook', 'google', 'leetcode']
B = ['lo', 'eo']
print(s.solve(A, B))
A = ['amazon', 'apple', 'facebook', 'google', 'leetcode']
B = ['ec', 'oc', 'ceo']
print(s.solve(A, B))