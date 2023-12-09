from typing import List, Dict


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        m = [-1] * amount
        m[0] = 0

        for i in range(1, len(m) + 1):
            # Min steps to find the i-th amount
            min_steps = float('inf')
            min_found = False
            for c in coins:
                if i - c < 0:
                    continue
                prev_steps = m[i-c]
                if prev_steps != -1 and prev_steps < min_steps:
                    min_steps = prev_steps
                    min_found = True

            res = 1 + min_steps if min_found else -1
            if i == len(m):
                return res

            m[i] = res


s = Solution()
res = s.coinChange([5, 3, 2], 11)
print(res)