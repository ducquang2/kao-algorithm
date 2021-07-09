class Solution:
    def isPalindrome(self, x):
        # Solution 1        
        # outstring = str(abs(x))[::-1] #change to string and reverse it
        
        # if int(outstring) > (2)**31: #check if |x| <= (2^31)-1
        #     outstring = '0'
        
        # elif x < 0: # check if x negative or not
        #     #outstring = '-' + outstring
        #     return False

        # y = int(outstring)

        # if x == y:
        #     return True
        # else:
        #     return False

        # Solution 2
        if x < 0 :
            return False
        
        reverse = 0
        origin = x

        while x > 0:
            reverse = reverse * 10 + x % 10
            x = x // 10

        return reverse == origin
Solution.isPalindrome(Solution, 121)
        