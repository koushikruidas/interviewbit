class Solution:
    def nCr(self, n, r):
        res = 1
        if r > n//2:
            r = n -r
        for i in range(1, r+1):
            res *= n - r + i
            res //= i
        return res
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        a = A - 1
        b = B -1
        c = a + b
        return self.nCr(c, a)
