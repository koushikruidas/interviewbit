class Solution:
    # @param A : integer
    # @return a list of list of integers
    def getRow(self, A):
        row = []
        for j in range(0, A+1, 1):
            row.append(self.nCr(A, j))
        return row

    def nCr(self, n, r):
        res = 1
        if r > n // 2:
            r = n - r
        for i in range(1, r+1):
            res *= n - i + 1
            res //= i
        return res


sol = Solution()
print(sol.getRow(5))