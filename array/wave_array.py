import random

class Solution:
    def quick_sort(self, A, start, end):
        if start < end:
            mid = self.randomized_partition(A, start, end)
            self.quick_sort(A, start, mid-1)
            self.quick_sort(A, mid+1, end)
        return A

    def randomized_partition(self, A, start, end):
        i = random.randint(start, end)
        self.swap(A, i, end)
        return self.partition(A, start, end)

    def partition(self, A, start, end):
        x = A[end]
        j = start -1
        for i in range(start, len(A)):
            if A[i] < x:
                j += 1
                self.swap(A, i, j)
        self.swap(A, j+1, end)
        return j+1

    def swap(self, A, i, j):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp

    def wave_array(self, A):
        self.quick_sort(A, 0, len(A) -1)
        i = 0
        while(i < len(A) -1):
            self.swap(A, i, i+1)
            i += 2
        return A

    def wave(self, A):
        n = len(A)
        self.quick_sort(A, 0, n - 1)
        for i in range(0, n, 2):
            if i > 0 and A[i - 1] > A[i] :
                self.swap(A, i-1, i)
            if i < n -1 and A[i + 1] > A[i]:
                self.swap(A, i+1, i)
        return A


A = [8, 7, 9, 5, 3, 1, 4, 2, 6, 0]
B = [10, 90, 49, 2, 1, 5, 23]
C = [11, 8, 7, 9, 2, 10, 2]
D = [ 95, 19, 54, 23, 89, 60, 5, 26, 23, 6, 13, 70, 38, 94, 20, 44, 66, 34, 26, 94, 63, 38, 44, 90, 50, 59, 23, 47, 85, 17, 72, 39, 47, 85, 96, 85, 23, 20, 44, 68, 35, 15, 25, 34, 42, 11, 79, 52, 44 ]

sol = Solution()
print(sol.wave(D))