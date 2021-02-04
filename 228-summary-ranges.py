class Solution:
    def summaryRanges(self, nums):
        if len(nums) == 1:
            return [str(nums[0])]
        else:
            result = []
            start = 0
            stop = 1

            while stop < len(nums):
                if nums[stop - 1] + 1 != nums[stop]:
                    if stop - 1 == start:
                        result.append(str(nums[start]))
                    else:
                        result.append(f"{nums[start]}->{nums[stop-1]}")
                    if stop == len(nums)-1:
                        result.append(f"{nums[stop]}")
                    start = stop 
                    stop += 1
                else:
                    if stop == len(nums) - 1:
                        result.append(f"{nums[start]}->{nums[stop]}")
                    stop += 1
            return result

Solution.summaryRanges(Solution,[0,2,3,4,6,8,9])