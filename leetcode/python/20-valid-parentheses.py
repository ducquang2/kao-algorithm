# Another solution with Java: https://github.com/ducquang2/Java-Basic-Skill/blob/master/Braces.java
class Solution:
    def isValid(self, s):
        dic = {'(': 1 , ')': 2 , '[': 3 , ']': 6 , '{': 5 , '}': 10}  # open brace is odd and muptile by 2 is the close brace will make them easier too track
        res = []
        for one in s:
            temp = dic[one]
            if(temp % 2):
                res.append(temp)
            else:
                if(len(res) and res[-1] == temp // 2): # check if close brace in order or not
                    del res[-1]
                else:
                    return False

        return res == []

print(Solution.isValid(Solution, "[{()}[]()]"))