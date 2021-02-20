class Solution:
    def maxCoins(self, nums):
        newnums = []
        for n in nums:
            if n != 0:
                newnums.append(n)
        newnums = [1] + nums + [1]
        n = len(newnums)
        dp = [[0]*(n) for _ in range(n)]
        for left in range(n-3, -1, -1):
            for right in range(left+2, n):
                for i in range(left+1, right):
                    dp[left][right] = max(dp[left][i] + newnums[i] * newnums[left] * newnums[right] + dp[i][right], dp[left][right])
        return dp[0][-1]

Solution.maxCoins(Solution, [1,5])