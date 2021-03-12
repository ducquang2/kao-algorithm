class Solution:
    def twoSum(self, nums, target):
        finding_dict = {}
        for i, num in enumerate(nums):
            remain = target - num

            # first-way
            # if remain not in finding_dict:
            #     finding_dict[num] = i
            # else:
            #     return [finding_dict[remain], i]

            # second-way
            if remain in finding_dict:
                return [finding_dict[remain], i]
            finding_dict[num] = i
        return []


Solution.twoSum(Solution, [1,5,4,4,3], 9)