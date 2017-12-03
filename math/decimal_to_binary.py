import math

class Solution:
    # Takes an Integer number A
    # Returns a list
    def __init__(self):
        self.list = []

    def int_to_binary(self, A):
        if A == 0:
            return
        self.list.append(str((A % 2)))
        self.int_to_binary(A // 2)



sol = Solution()
sol.int_to_binary(9)
sstr = ''.join(reversed(sol.list))
print(sstr)