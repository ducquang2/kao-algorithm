class Solution:
    def longestPalindrome(self, s):
        ans = ''
        length = 0

        for i in range(len(s)):
            # Odd length strings e.g. 'a' 'aba'
			left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > length:
                    length = right - left + 1
                    ans = s[left:right+1]

                # Expand left to left, right to right
                left -= 1
                right += 1

            # Even length strings 'aa' 'abba'
			left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > length:
                    length = right - left + 1
                    ans = s[left:right+1]

                left -= 1
                right += 1

        print(ans + ' ' + str(length))

Solution.longestPalindrome(Solution, "ababcc")
