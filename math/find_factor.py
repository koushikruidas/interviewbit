import math


class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        x = math.floor(math.sqrt(A))
        res = []
        for i in range(1, x + 1):
            if A % i == 0:
                res.append(i)
                if i <= x:
                    res.append(A//i)
        # res.append(A)
        res.sort()
        return res

Solution = Solution()
print(Solution.allFactors(38808))