class Solution:
    # def climbStairs(self, n: int) -> int:
    #     m = {}

    #     def dp(i) -> int:
    #         if i == 1:
    #             return 1
    #         if i == 2:
    #             return 2

    #         if i in m:
    #             return m[i]

    #         sum = dp(i-1) + dp(i-2)
    #         m[i] = sum
    #         return sum

    #     return dp(n)

    # bottom-up approach
    # Space size -- O(N)
    def climbStairs(self, n: int) -> int:
        dp = [-1] * n
        dp[0] = 1
        if n > 1:
            dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]

    # Space size -- O(1)
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        prevprev = 1
        prev = 2
        for _ in range(2, n):
            temp = prevprev + prev
            prevprev = prev
            prev = temp

        return prev
