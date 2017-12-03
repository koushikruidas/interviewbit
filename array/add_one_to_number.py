class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        A.insert(0, 0)
        n = len(A) - 1
        carry = 1
        for i in range(n, -1, -1):
            sum = (A[i] + carry)
            A[i] = sum%10
            carry = sum // 10
        i = 0
        while A[i] == 0:
            if A[i] == 0:
                A.remove(0)
        return A




A = [8,9,9]
sol = Solution()
print(sol.plusOne(A))