class Solution:
    def spiralOrder(self, A):
        row = len(A) - 1
        col = len(A[0]) - 1
        dir = 0
        st_row  = 0
        st_col = 0
        result   = []
        total = (row + 1)*(col +1)
        printed = 0
        while printed < total:
            if dir == 0:
                for i in range(st_col, col + 1, 1):
                    result.append(A[st_row][i])
                    printed += 1
                st_row += 1
                dir = 1
                continue
            if dir == 1:
                for i in range(st_row, row + 1, 1):
                    result.append(A[i][col])
                    printed += 1
                col -= 1
                dir = 2
                continue
            if dir == 2:
                for i in range(col, st_col - 1, -1):
                    result.append(A[row][i])
                    printed += 1
                row -= 1
                dir = 3
                continue
            if dir == 3:
                for i in range(row, st_row - 1, -1):
                    result.append(A[i][st_col])
                    printed += 1
                st_col += 1
                dir = 0
                continue
        return result


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
b = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
c = [[1,2,3,4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
sol = Solution()
print(sol.spiralOrder(a))
