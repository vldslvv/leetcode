from typing import List, Dict


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        sums = {}
        max_n = nums[0]
        for n in nums:
            if n > max_n:
                max_n = n
            if n in sums:
                sums[n] += n
            else:
                sums[n] = n

        m = {}

        return self.dp(max_n, m, sums)


    def dp(self, i: int, m: Dict[int, int], sums: Dict[int, int]) -> int:
        if i < 0:
            return 0
        if i == 0:
            return 0

        if i in m:
            return m[i]

        i_score = sums[i] if i in sums else 0
        take_i_score = i_score + self.dp(i - 2, m, sums)
        skip_i_score = self.dp(i - 1, m, sums)

        score = max(take_i_score, skip_i_score)
        m[i] = score

        return score


s = Solution()
# a = [1, 2, 2, 5]
# a = [3, 3, 3, 2, 2, 1, 1, 1, 10]
# a = [1,1,1,2,4,5,5,5,6]
a = [1,4,5,5,5,6]
res = s.deleteAndEarn(a)
print(res)