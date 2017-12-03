class Solution:
    # @param A : integer
    # @return a strings
    def findDigitsInBinary(self, A):
        res = []
        if A == 0:
            res.append(str(A))
        while A > 0:
            res.append(str(A % 2))
            A //= 2
        res.reverse()
        ans = "".join(res)
        return ans

Sol = Solution()
print(Sol.findDigitsInBinary(6))