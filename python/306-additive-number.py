class Solution:
    def isAdditiveNumber(self, num):
        length = len(num)
        for i in range(1, int(length/2 + 1)):
            for j in range(1, int((length-i)/2 + 1)):
                first, second, others = num[:i], num[i:i+j], num[i+j:]
                if self.isValid(self ,first = first, second = second, others = others):
                    return True
        return False

    def isValid(self, first, second, others):
        if ((len(first) > 1 and first[0] == "0") or (len(second) > 1 and second[0] == "0")):
            return False
        sum_str = str(int(first) + int(second))
        if sum_str == others:
            return True
        elif others.startswith(sum_str):
            return self.isValid(self, first = second, second = sum_str, others = others[len(sum_str):])
        else:
            return False

print(Solution.isAdditiveNumber(Solution, "112358"))