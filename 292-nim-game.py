class Solution:
    def canWinNim(self, n):
        # First way:
        return '1' in bin(n)[-2:]


Solution.canWinNim(Solution, 9)