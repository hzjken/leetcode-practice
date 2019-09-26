class Solution:
    def singleNumber(self, nums):
        bit = [0] * 32
        negative = 0
        for i in nums:
            if i < 0:
                negative += 1
            string = bin(abs(i))[2:]
            for index, j in enumerate(string[::-1]):
                bit[len(bit) - index - 1] += int(j)
        
        bit = [str(i % 3) for i in bit]
        output = int(''.join(bit),2)
        if negative % 3 == 0:
            return output
        else:
            return -1 * output


s = Solution()
print(s.singleNumber([0,1,0,1,0,1,99]))