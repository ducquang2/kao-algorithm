class Solution:
    def romanToInt(self, s):
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        if len(s) == 0:
            return 0
	    
        num, lastint, total, i = 0, 0, 0, 0

        while (i != len(s)):
            char = s[len(s)-(i+1) : len(s)-i]
            num = roman[char]
            if num < lastint:
                total = total - num
            else:
                total = total + num

            i += 1
            lastint = num


        print(total)
        return total


Solution.romanToInt(Solution, "IV")