import math

class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        x = [None]*(A+1)
        res = []
        for i in range(2,A+1):
            if x[i] == False:
                continue
            else:
                x[i] = self.isPrime(i)
                if x[i]:
                    j = 2
                    while(j*i < A):
                        x[j*i] = False
                        j = j +1
                    res.append(i)
        return res

    def isPrime(self,i):
        x = math.floor(math.sqrt(i))
        if i == 1:
            return False
        for j in range(2,x+1):
            if i % j == 0:
                return False
        return True

sol = Solution()
print(sol.sieve(167772))