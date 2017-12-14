class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        hash = {}
        for i in range(len(A)):
            if A[i] in hash:
                return A[i]
            hash[A[i]] = 1
        return -1


sol = Solution()
A = [3,4,1,4,1]
print(sol.repeatedNumber(A))