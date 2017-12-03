class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        sum = 0
        for i in range(1, A):
            z = self.power(5,i )
            if A // z is not 0:
                sum += A//z
        return sum

    def power(self, x, y):
        if y == 0:
            return 1
        z = 0 if y == -1 else y//2
        temp = self.power(x,z)
        if y % 2 == 0:
            return temp*temp
        else:
            if y > 0:
                return x*temp*temp
            else:
                return (temp*temp)/x



sol = Solution()
print(sol.trailingZeroes(2))