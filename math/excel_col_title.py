class Solution:
    # @param A : integer
    # @return a strings
    def __init__(self):
        self.list = []
    def convertToTitle1(self, A):
        if A == 0:
            return
        if A%26 == 0:
            self.list.append(self.int_to_char(26))
            self.convertToTitle1(A // 26 - 1)
        else:
            self.list.append(self.int_to_char((A % 26)))
            self.convertToTitle1(A // 26)

    def int_to_char(self,n):
        return chr(64 + n)

    def convertToTitle(self, A):
        self.convertToTitle1(A)
        sstr = ''.join(reversed(self.list))
        return sstr

sol = Solution()
sol.convertToTitle1(95568)
sstr = ''.join(reversed(sol.list))
print(sstr)