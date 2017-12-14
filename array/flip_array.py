class Solution:
    def __init__(self):
        self.memo = {}

    def flip(self, A):
        for i in range(len(A)):
            A[i] += 1

        for i in range(len(A)):
            x = A[i]
            if A[A[i] - 1] > len(A) +1:
                y = A[A[i] - 1] // (len(A) +1)
            else:
                y = A[A[i] - 1]
            z = x*(len(A) + 1) + y
            A[i] = z

        for i in range(len(A)):
            A[i] %= (len(A) + 1)

        for i in range(len(A)):
            A[i] -= 1

        return A

D = [ 95, 19, 54, 23, 89, 60, 5, 26, 23, 6, 13, 70, 38, 94, 20, 44, 66, 34, 26, 94, 63, 38, 44, 90, 50, 59, 23, 47, 85, 17, 72, 39, 47, 85, 96, 85, 23, 20, 44, 68, 35, 15, 25, 34, 42, 11, 79, 52, 44 ]
A = [2, 1, 4, 3, 6, 0, 5]
B = [2, 0, 1]
I = [ 2,1,3,0 ]
sol = Solution()
print(sol.flip(I))