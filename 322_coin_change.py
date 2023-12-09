from typing import List, Dict


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = min(coins)
        m = {}
        return self.dp(amount, m, coins, min_coins)

    # i -- min steps to find number i
    # min_coins -- helps to track when we are not able to find a solution
    def dp(self, i: int, m: Dict[int, int], coins: List[int], min_coins: int) -> int:
        # Base cases
        if i == 0:
            return 0

        if i < min_coins:
            return -1
        
        if i in m:
            return m[i]

        possible_steps = [self.dp(i - c, m, coins, min_coins) for c in coins if i - c >= 0]
        valid_steps = [s for s in possible_steps if s >= 0]
        if len(valid_steps) > 0:
            min_steps = 1 + min(valid_steps)
            m[i] = min_steps
        else:
            m[i] = -1

        return m[i]

s = Solution()
res = s.coinChange([5, 3, 2], 11)
print(res)