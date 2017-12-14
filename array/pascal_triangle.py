class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        res = []
        for i in range(A):
            row = []
            for j in range(0, i+1, 1):
                row.append(self.nCr(i, j))
            res.append(row)
        return res

    def nCr(self, n, r):
        res = 1
        if r > n // 2:
            r = n - r
        for i in range(1, r+1):
            res *= n - i + 1
            res //= i
        return res


sol = Solution()
# print(sol.nCr(5,2))
print(sol.generate(5))