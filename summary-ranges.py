class Solution:
    def summaryRanges(self, nums):
        if len(nums) == 1:
            return [str(nums[0])]
        else:
            temp = []
            curr = 0
            new = 1
            while new < len(nums):
                if nums[new - 1] + 1 == nums[new]:
                    if new == len(nums) - 1:
                        temp.append(f"{nums[curr]}->{nums[new]}")

