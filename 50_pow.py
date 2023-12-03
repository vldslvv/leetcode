class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, n * -1)

        if n == 1:
            return x

        if n == 0:
            return 1
        
        m = n // 2
        if n % 2 == 1:
            return x * self.myPow(x * x, m)

        return self.myPow(x * x, m)


    def myPow_iter(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n *= -1

        # Current x ^ ni
        res = x
        ni = n
        while ni != 0:
            if ni % 2 == 1:
                res == res * x
                ni -= 1

            res *= res

            ni = ni // 2

        return res


s = Solution()
res = s.myPow_iter(2, 10)
print(res)
