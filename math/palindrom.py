class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        sum = 0
        B = A
        while A > 0:
            sum = 10*sum + A % 10
            A //= 10
        if sum == B:
            return True
        else:
            return False


sol = Solution()
print(sol.isPalindrome(556))