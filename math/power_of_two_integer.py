import math


class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        if A == 1:
            return 1
        sqrt_a = math.floor(math.sqrt(A))
        for i in range(1,sqrt_a + 1):
            for j in range (2,sqrt_a+1):
                x = self.power(i,j)
                if x == A:
                    return 1
                elif x > A:
                    break
                else:
                    continue
        return 0


    def power(self,x,y):
        if y == 0:
            return 1
        z = 0 if y == -1 else y//2
        temp = self.power(x,z)
        if y % 2 == 0:
            return temp*temp
        else:
            if y > 0:
                return x*temp*temp
            else:
                return (temp*temp)/x



sol = Solution()
print(sol.isPower(25252554))