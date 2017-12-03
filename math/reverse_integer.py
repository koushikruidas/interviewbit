class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        if A < 0:
            a = abs(A)
            c = 0
            while (a > 0):
                c =c*10 + a % 10
                a = a // 10
            if c > 2147483647:
                return 0
            else:
                return c*-1

        else:
            c = 0
            while (A > 0):
                c =c*10 + A % 10
                A = A // 10
        if c > 2147483647:
            return 0
        else:
            return c

sol = Solution()
print(sol.reverse(1111111112))