class Solution:
    def canWinNim(self, n):
        # First way:
        # return '1' in bin(n)[-2:]
        # Second way:
        return n%4 != 0

Solution.canWinNim(Solution, 9)