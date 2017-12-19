class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        array_len = len(arrive) - 1
        start = 0
        dep = 0
        no_room_available = K
        arrive.sort()
        depart.sort()
        while start < array_len:
            start += 1
            no_room_available -= 1
            if no_room_available == 0:
                if arrive[start] >= depart[dep]:
                    no_room_available += 1
                    dep += 1
                else:
                    no_room_available -= 1
            if no_room_available < 0:
                return 0
        return 1



A = [ 1, 2, 3, 4 ]
B = [ 10, 2, 6, 14 ]

C = [1, 2, 3]
D = [2, 3, 4]
sol = Solution()
print(sol.hotel(C, D, 1))