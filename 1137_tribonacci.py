class Solution:
    def tribonacci(self, n: int) -> int:
        vals = [-1] * n + 1
        if n > 0:
            vals[0] = 0
        if n > 1:
            vals[1] = 1
        if n > 2:
            vals[2] = 2

        for i in range(3, n):
            vals[i] = vals[i-1] + vals[i-2] + vals[i-3]

        return vals[-1]