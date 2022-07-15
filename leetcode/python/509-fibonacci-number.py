class Solution:
    def fib(self, n):
        if n <= 1:
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)

Solution.fib(Solution, 2)