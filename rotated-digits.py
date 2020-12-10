class Solution:
    def rotatedDigits(self, N):
        count = 0
        for num in range(1, N + 1):
            s = str(num)
            if '3' in s or '4' in s or '7' in s:
                continue
            if '2' in s or '5' in s or '6' in s or '9' in s:
                count += 1
            
        return count

Solution.rotatedDigits(Solution,1000)