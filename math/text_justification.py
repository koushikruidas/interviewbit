class Solution:
    def __init__(self):
        self.memo = {}
        self.s = {}

    def cost(self, w, i, col_len):
        sum = 0
        cost = 0
        for j in range(i):
            sum += len(w[j]) + 1
        sum -= 1
        if sum > col_len:
            cost = float('inf')
            return cost
        cost = (col_len - sum)**3
        return cost


    def justification(self, w, col_len):
        n = len(w)
        if n in self.memo:
            return self.memo[n]
        if n == 0:
            self.memo[0] = 0
            return 0
        cost = float('inf')
        for i in range(1, n+1):
            if cost > self.justification(w[i:], col_len) + self.cost(w, i, col_len):
                cost = self.justification(w[i:], col_len) + self.cost(w, i, col_len)
                self.s[n] = i
        self.memo[n] = cost
        return cost

    def pprint(self, w, n):
        while n> 0:
            k = self.s[n]
            for i in range(k):
                print(str(w[i])+" ",end = "")
            print("")
            n -= k
            w = w[i+1:]
        return ""



w = "In mathematics, the Euclidean algorithm[a], or Euclid's algorithm, is an efficient method for computing the greatest common divisor (GCD) of two numbers, the largest number that divides both of them without leaving a remainder. It is named after the ancient Greek mathematician Euclid, who first described it in Euclid's Elements (c. 300 BC). It is an example of an algorithm, a step-by-step procedure for performing a calculation according to well-defined rules, and is one of the oldest algorithms in common use. It can be used to reduce fractions to their simplest form, and is a part of many other number-theoretic and cryptographic calculations."
sol = Solution()
split = w.split(" ")
sol.justification(split, 83)
k = len(split)
print(sol.pprint(split, k))
