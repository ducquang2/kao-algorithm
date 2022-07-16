class Solution:
    def lengthOfLongestSubstring(self, s):
        mapping = {}
        result = 0
        start = 0
        
        for char in range(len(s)):
            if s[char] in mapping:
                start = max(mapping[s[char]] + 1,start)
                
            mapping[s[char]] = char
            result = max(result, char - start + 1)
                
        return result

print(Solution.lengthOfLongestSubstring(Solution, "123123412345"))