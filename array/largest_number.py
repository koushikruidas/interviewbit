class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        B = list(A)
        C = sorted(B, cmp = self.my_compare, reverse=True)
        for i in range(len(C)):
            if C[i] != 0:
                break
        C = C[i:]

        D = [str(x) for x in C]
        D = "".join(D)
        return D

    def my_compare(self,i, j):
        first = j
        first_k = 1
        if j == 0:
            first_k = 10
        while first > 0:
            first //= 10
            first_k *= 10
        xy = i*first_k +j
        second = i
        second_k = 1
        if i == 0:
            second_k = 10
        while second > 0:
            second //= 10
            second_k *= 10
        yx = j*second_k + i
        if yx > xy:
            return -1
        elif xy > yx:
            return 1
        else:
            return 0



sol = Solution()
a = [8, 89]
print(sol.largestNumber(a))
