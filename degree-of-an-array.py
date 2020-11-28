nums = [1, 2, 2, 3, 1, 4, 2]


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cmap = {}
        min_subarray = inf
        for i, num in enumerate(nums):
            if num not in cmap:
                cmap[num] = [i]
            else:
                cmap[num].append(i)
        degree = max([len(c) for c in cmap.values()])
        for v in cmap.values():
            if len(v) == degree:
                subarray = v[-1]-v[0]
                if subarray < min_subarray:
                    min_subarray = subarray
        return min_subarray+1
