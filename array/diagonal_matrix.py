class Solution:
    def anti_diagonal(self, A):
        row = len(A)
        col = len(A[0])
        res = []
        for i in range(row):
            k = i
            n = i
            B = []
            if n >= col:
                n = col - 1
            for j in range(0, n + 1, 1):
                # print(A[j][k])
                B.append(A[j][k])
                k -= 1
            res.append(B)
        n = col - 1
        l = 1
        start = 0
        while l <= n:
            k = row - 1
            B = []
            for j in range(start + 1, col, 1):
                # print(A[j][k])
                B.append(A[j][k])
                k -= 1
            res.append(B)
            start += 1
            l += 1
        return res



sol = Solution()
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
c = [[1,2,3,4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
b = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
q = (sol.anti_diagonal(c))
print("start q"+str(q))
