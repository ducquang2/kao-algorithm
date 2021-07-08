class Solution:
    def reverse(self, x):
        
        outstring = str(abs(x))[::-1] #change to string and reverse it
        
        if int(outstring) > (2)**31: #check if |x| <= (2^31)-1
            outstring = '0'
        
        elif x < 0: # check if x negative or not
            outstring = '-' + outstring       
        
        return(int(outstring))

Solution.reverse(Solution, 457)