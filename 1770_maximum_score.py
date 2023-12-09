from typing import List, Dict, Tuple


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = {}
        return self.dp(i=0, s=0, m=m, nums=nums, multipliers=multipliers)

    # i -- current operation
    # s -- start index
    # m -- memoized scores with tuple as key: m(s, e)
    # representing max score
    def dp(self, i: int, s: int, m: Dict[Tuple[int, int], int], nums: List[int], multipliers: List[int]) -> int:
        # End index
        e = len(nums) - 1 - (i - s)

        if (s, i) in m:
            return m[(s, i)]

        mult = multipliers[i]
        # Last case, leaf of recursion tree
        if i == len(multipliers) - 1:
            m[(s, i)] = max(mult * nums[s], mult * nums[e])
            return m[(s, i)]

        take_start = self.dp(i+1, s+1, m, nums, multipliers) + (mult * nums[s])
        take_end = self.dp(i+1, s, m, nums, multipliers) + (mult * nums[e])
        m[(s, i)] = max(take_start, take_end)
        return m[(s, i)]


s = Solution()
nums = [1,2,3]
mult = [3,2,1]

nums = [-5,-3,-3,-2,7,1]
mult = [-10,-5,3,4,6]
res = s.maximumScore(nums, mult)
print(res)