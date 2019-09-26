class Solution:
    def getPermutation(self, n, k):
        rest = k - 1
        factorial = 1
        new_fact = 1
        component = [0] * n

        while factorial * new_fact <= k - 1:
            factorial *= new_fact
            new_fact += 1
        new_fact -= 1

        while rest > 0:
            if rest >= factorial:
                val = rest // factorial
                component[new_fact] = val
                rest -= val * factorial
            else:
                factorial //= new_fact
                new_fact -= 1

        output = ''
        n_list = list(range(1, n+1))
        for i in reversed(range(n)):
            num = component[i]
            output += str(n_list.pop(num))
        
        return output


s = Solution()
print(s.getPermutation(5,20))