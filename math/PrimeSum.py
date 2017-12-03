import math


class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        ar = []
        k = 0
        for i in range(2, A+1):
            if self.isPrime(i):
                ar.append(i)
                if self.isPrime(A - ar[k]):
                    ar.append(A - ar[k])
                    return (ar[k], ar[k+1])
                else:
                    k +=1
                    continue


    def isPrime(self, i):
        x = math.floor(math.sqrt(i))
        if i == 1:
            return False
        for j in range(2, x + 1):
            if i % j == 0:
                return False
        return True



sol = Solution()
print(sol.primesum(1677))