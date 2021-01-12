class Solution:
    def isAdditiveNumber(self, num: str):
        length = len(num)
        for i in range(1, length/2+1):
            for j in range(1, (length-i)/2 + 1):
                first, second, others = num[:i], num[i:i+j], num[i+j:]
                if self.isValid(first, second, others):
                    return True
        return False
        
    def isValid(self, first, second, others):
        if ((len(first) > 1 and first[0] == "0") or (len(second) > 1 and second[0] == "0")):
            return False
        