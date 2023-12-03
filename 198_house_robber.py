from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_house_sum = 0
        prevprev_house_sum = 0
        curr_sum = 0
        for house in nums:
            curr_sum = max(prevprev_house_sum + house, prev_house_sum)
            prevprev_house_sum = prev_house_sum
            prev_house_sum = curr_sum

        return max(prev_house_sum, prevprev_house_sum)

s = Solution()
# nums = [1,2,3,1]
# nums = [2,7,9,3,1]
nums = [2,1,1,2]
res = s.rob(nums)
print(res)
