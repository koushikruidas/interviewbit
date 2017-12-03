class Solution:
    """A, B : 2 array of integer
       Return the list of the summation """
    def __init__(self):
        self.li = []

    def add_two_number(self, A, B):
        i = len(A) - 1
        j = len(B) - 1
        carry = 0
        if j > i:
            B.insert(0, 0)
            temp = i
            i = j + 1
            j = temp
            while i != -1:
                if j == -1:
                    carry += B[i]
                    self.li.append(carry % 10)
                    carry //= 10
                    i -= 1
                else:
                    carry += B[i] + A[j]
                    self.li.append(carry % 10)
                    carry //= 10
                    i -= 1
                    j -= 1
        else:
            A.insert(0, 0)
            i += 1
            while i != -1:
                if j == -1:
                    carry += A[i]
                    self.li.append(carry % 10)
                    carry //= 10
                    i -= 1
                else:
                    carry += A[i] + B[j]
                    self.li.append(carry % 10)
                    carry //= 10
                    i -= 1
                    j -= 1
        self.li.reverse()
        if self.li[0] == 0:
            self.li.remove(0)
        return self.li

    def add_two_number_ext(self, A, B):
        i = len(A) - 1
        j = len(B) - 1
        carry = 0
        while i != -1 and j != -1:
            carry += A[i] + B[j]
            self.li.append(carry %10)
            carry //= 10
            i -= 1
            j -= 1
        while i != -1:
            carry += A[i]
            self.li.append(carry % 10)
            carry //= 10
            i -= 1
        while j != -1:
            carry += B[j]
            self.li.append(carry % 10)
            carry //= 10
            j -= 1
        if carry != 0:
            self.li.append(carry)
        self.li.reverse()
        if self.li[0] == 0:
            self.li.remove(0)
        return self.li

    def add_two_num_ext1(self, A, B):
        A.insert(0, 0)
        B.insert(0, 0)
        i = len(A) - 1
        j = len(B) - 1
        carry = 0
        while i > 0 or j > 0:
            carry += A[i] + B[j]
            self.li.append(carry % 10)
            carry //= 10
            if i > 0:
                i -= 1
            if j > 0:
                j -= 1
        if carry > 0:
            self.li.append(carry)
        self.li.reverse()
        return self.li

    def add_two_hex_num(self, A, B):
        A = Solution.char_to_int(A)
        B = Solution.char_to_int(B)
        A.insert(0, 0)
        B.insert(0, 0)
        i = len(A) - 1
        j = len(B) - 1
        carry = 0
        while i > 0 or j > 0:
            carry += A[i] + B[j]
            ch = Solution.int_to_char(carry % 16)
            self.li.insert(0, ch)
            carry //= 16
            if i > 0:
                i -= 1
            if j > 0:
                j -= 1
        if carry > 0:
            self.li.insert(0, carry)
        return self.li

    @staticmethod
    def int_to_char(n):
        if n > 9:
            return chr(55 + n)
        else:
            return n

    @staticmethod
    def char_to_int(p):
        n = len(p)
        for i in range(n):
            if ord(str(p[i])) <= 57:
                continue
            else:
                p[i] = ord(p[i]) - 54
        return p

A = ['E', 1, 4]
B = [9, 9, 9, 9]
sol = Solution()
print(sol.add_two_hex_num(A, B))