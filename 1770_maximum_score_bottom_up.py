from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # define memo dimensions
        # for each start value, we can potentially have operation index
        # so, len(nums) x len(multipliers)
        num_ops = len(multipliers)
        m = [[0 for _ in range(num_ops + 1)] for _ in range(num_ops + 1)]

        # s -- start index
        # op -- operation number
        # e -- end index, derived from s and op
        for op in range(num_ops - 1, -1, -1):
            for s in range(op, -1, -1):
                e = len(nums) - 1 - (op - s)
                m[op][s] = max(m[op + 1][s] + multipliers[op] * nums[e],
                               m[op + 1][s + 1] + multipliers[op] * nums[s])
        
        return m[0][0]


s = Solution()
nums = [1,2,3]
mult = [3,2,1]

nums = [-5,-3,-3,-2,7,1]
mult = [-10,-5,3,4,6]
res = s.maximumScore(nums, mult)
print(res)