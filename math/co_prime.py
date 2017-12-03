class Solution:
    """takes two integer as input
    returns 1 if those two are co-prime else returns 0"""
    def gcd(self, x , y):
        c = 1
        if x < 0:
            return y
        if y < 0:
            return x
        if x < y:
            temp = y
            y = x
            x = temp
        while c > 0:
            c = x % y
            x = y
            y = c
        return x

    def co_prime(self, x, y):
        k = self.gcd(x, y)
        if k == 1:
            return 1
        return 0

    def cpFact(self, A, B):
        k = self.gcd(A,B)
        if k == 1:
            return A
        y = A // k
        while(y > 0):
            z = self.gcd(y, B)
            if z == 1:
                return y
            y = y // z
        return 1



sol = Solution()
print(sol.cpFact(74,22))