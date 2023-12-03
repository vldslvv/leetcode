from typing import List, Dict, Tuple


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = {}
        return self.dp(i=0, s=0, e=len(nums) - 1, m=m, nums=nums, multipliers=multipliers)

    # i -- current operation
    # s -- start index
    # e -- end index
    # m -- memoized scores with tuple as key: m(s, e)
    # representing max score
    def dp(self, i: int, s: int, e: int, m: Dict[Tuple[int, int], int], nums: List[int], multipliers: List[int]) -> int:
        if (s, e) in m:
            return m[(s, e)]

        mult = multipliers[i]
        # Last case, leaf of recursion tree
        if i == len(multipliers) - 1:
            m[(s, e)] = max(mult * nums[s], mult * nums[e])
            return m[(s, e)]

        # if i == 0:
        #     m[(s, e-1)] = mult * nums[e]
        #     m[(s+1, e)] = mult * nums[s]
        #     m[(s, e)] = max()
        #     return max(m[(s, e-1)], m[(s+1, e)])

        take_start = self.dp(i+1, s+1, e, m, nums, multipliers) + (mult * nums[s])
        take_end = self.dp(i+1, s, e-1, m, nums, multipliers) + (mult * nums[e])
        m[(s, e)] = max(take_start, take_end)
        return m[(s, e)]


s = Solution()
nums = [1,2,3]
mult = [3,2,1]

nums = [-5,-3,-3,-2,7,1]
mult = [-10,-5,3,4,6]
res = s.maximumScore(nums, mult)
print(res)