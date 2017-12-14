class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        row = A - 1
        col = A - 1
        dir = 0
        st_row = 0
        st_col = 0
        result = [[0 for i in range(A)] for j in range(A)]
        total = (row + 1) * (col + 1)
        printed = 0
        while printed < total:
            if dir == 0:
                for i in range(st_col, col + 1, 1):
                    result[st_row][i] = printed + 1
                    printed += 1
                st_row += 1
                dir = 1
                continue
            if dir == 1:
                for i in range(st_row, row + 1, 1):
                    result[i][col] = printed + 1
                    printed += 1
                col -= 1
                dir = 2
                continue
            if dir == 2:
                for i in range(col, st_col - 1, -1):
                    result[row][i] = printed + 1
                    printed += 1
                row -= 1
                dir = 3
                continue
            if dir == 3:
                for i in range(row, st_row - 1, -1):
                    result[i][st_col] = printed + 1
                    printed += 1
                st_col += 1
                dir = 0
                continue
        return result



sol = Solution()
print(sol.generateMatrix(3))