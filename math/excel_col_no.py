import math

class Solution:
    # @param A : string
    # @return an integer
    def char_to_value(self,char):
        return ord(char) - ord("A") + 1

    def titleToNumber(self, A):
        n = len(A)
        y = 0
        for i in range(0,n):
            x = self.char_to_value(A[n-1-i])
            y += x*self.power(26,i)
        return y

    def power(self, x, y):
        if y == 0:
            return 1
        z = 0 if y == -1 else y // 2
        temp = self.power(x, z)
        if y % 2 == 0:
            return temp * temp
        else:
            if y > 0:
                return x * temp * temp
            else:
                return (temp * temp) / x

sol = Solution()
print(sol.titleToNumber("EKIR"))