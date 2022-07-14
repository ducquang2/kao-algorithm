class Solution:
    def longestCommonPrefix(self, strs):
        common = strs[0]
        
        i = 1

        while i < len(strs):
            if strs[i].startswith(common):
                i += 1
            else:
                common = common[:-1]
        
        print(common)
        return common

Solution.longestCommonPrefix(Solution, ["flower","flow","flight"])
        