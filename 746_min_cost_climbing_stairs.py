from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        two_behind = cost[0]
        one_behind = cost[1]
        curr = min(one_behind, two_behind)

        for i in range(2, len(cost)):
            curr = cost[i] + min(one_behind, two_behind)
            two_behind = one_behind
            one_behind = curr

        return curr
    
    # TODO solve with recursion top-down
    def minCostClimbingStairs1(self, cost: List[int]) -> int:
        pass


s = Solution()
cost = [10, 15, 20]
# cost = [1,100,1,1,1,100,1,1,100,1]
res = s.minCostClimbingStairs(cost)
print(res)
