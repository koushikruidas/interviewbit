class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        n = len(A)
        maximum = 0
        max_value = 0
        for i in range(n):
            for j in range(1, n, 1):
                max_value = max(max_value, (abs(A[i] - A[j]) + abs(i - j)))
            maximum = max(maximum, max_value)
        return maximum

    #in O(n) complexit
    def max_arr_ext(self, A):
        n = len(A)
        max1 = max2 = max3 = max4 = ans =  float('-inf')
        for i in range(n):
            max1 = max(max1, A[i] + i)
            max2 = max(max2, -A[i] + i)
            max3 = max(max3, A[i] - i)
            max4 = max(max4, -A[i] - i)

        for i in range(n):
            ans = max(ans, max1 - A[i] - i)
            ans = max(ans, max2 + A[i] - i)
            ans = max(ans, max3 - A[i] + i)
            ans = max(ans, max4 + A[i] + i)

        return ans
sol = Solution()
a = [ 95, 19, 54, 23, 89, 60, 5, 26, 23, 6, 13, 70, 38, 94, 20, 44, 66, 34, 26, 94, 63, 38, 44, 90, 50, 59, 23, 47, 85, 17, 72, 39, 47, 85, 96, 85, 23, 20, 44, 68, 35, 15, 25, 34, 42, 11, 79, 52, 44 ]
b = [5, 1, 3, -1]
print(sol.max_arr_ext(b))