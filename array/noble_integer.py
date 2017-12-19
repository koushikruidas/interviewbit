class Solution:
    def solve(self, A):
        A.sort()
        n = len(A)
        for i in range(1,n,1):
            if A[i - 1] == A[i]:
                continue
            if A[i - 1] == n - i:
                return 1
            continue
        if A[n - 1] == 0:
            return 1
        return -1


sol = Solution()
a = [-6, -1, 4]
print(sol.solve(a))