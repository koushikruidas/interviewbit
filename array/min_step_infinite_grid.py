class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        min_step = 0
        for i in range(len(A) - 1):
            x1 = A[i]
            y1 = B[i]
            i += 1
            x2 = A[i]
            y2 = B[i]
            dlta_x = abs(x1 - x2)
            dlta_y = abs(y1 - y2)
            z = dlta_x if dlta_x < dlta_y else dlta_y
            min_step += z + abs(dlta_x - dlta_y)
        return min_step


A = [0, 2, 3, 4]
B = [0, 2, 2, 3 ]
sol = Solution()
print(sol.coverPoints(A, B))