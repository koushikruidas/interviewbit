class Solution:
    def diagonal(self, A):
        n = len(A[0])
        res = []
        row = []
        # k = 0
        # m = len(A)
        row.append(A[0][0])
        res.append(row)
        for k in range(1,n):
            row = []
            for i in range(k, -1, -1):
                for j in range(i, -1, -1):
                    if i + j == k:
                        if i == j:
                            row.append(A[i][j])
                        else:
                            row.append(A[j][i])
                            row.append(A[i][j])
            res.append(row)
        return res





a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
sol = Solution()
print(sol.diagonal(a))