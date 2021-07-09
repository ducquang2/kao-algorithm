class Solution:
    def isPalindrome(self, x):
        
        outstring = str(abs(x))[::-1] #change to string and reverse it
        
        if int(outstring) > (2)**31: #check if |x| <= (2^31)-1
            outstring = '0'
        
        elif x < 0: # check if x negative or not
            #outstring = '-' + outstring
            return False

        y = int(outstring)

        if x == y:
            return True
        else:
            return False

Solution.isPalindrome(Solution, -121)
        