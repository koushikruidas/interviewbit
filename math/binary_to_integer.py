class Solution:
    # Takes a binary number as input
    # Return an Integer

    def bi_to_int(self, A):
        n = len(A)
        sum = 0
        for i in range(n):
            sum += int(A[n-1 -i])*self.power(2, i)
        return sum

    def power(self, x, y):
        z = 0 if y == -1 else y//2
        if y == 0:
            return 1
        temp = self.power(x, z)
        if y % 2 == 0:
            return temp*temp
        else:
            if y > 0:
                return x*temp*temp
            else:
                return (temp*temp)/x


a = "1101"
sol = Solution()
print(sol.bi_to_int(a))