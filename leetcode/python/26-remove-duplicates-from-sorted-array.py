class Solution:
    def removeDuplicates(self, nums):
        index = 1
        size = len(nums)
        for i in range(1, size):
            if nums[i - 1] != nums[i]:
                nums[index] = nums[i]
                index = index + 1
            
        print("\n" + str(index))
        return index
            

Solution.removeDuplicates(Solution, [1, 2, 2, 3, 4, 5, 5])