class Solution:
    def findShortestSubArray(self, nums):
        cmap = {}
        min_subarray = 10
        for locate, num in enumerate(nums):
            if num not in cmap:
                cmap[num] = [locate]
            else:
                cmap[num].append(locate)
        degree = max([len(c) for c in cmap.values()])
        for v in cmap.values():
            if len(v) == degree:
                subarray = v[-1]-v[0]
                if subarray < min_subarray:
                    min_subarray = subarray
        return min_subarray+1


Solution.findShortestSubArray(Solution,[1,2,2,3,1])
