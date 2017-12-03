class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        ar = []
        for i in range(1,A+1):
            if i % 15 == 0:
                ar.append("FizzBuzz")
            elif i % 3 == 0:
                ar.append("Fizz")
            elif i % 5 == 0:
                ar.append("Buzz")
            else:
                ar.append(i)
        return ar


sol = Solution()
print(sol.fizzBuzz(25))