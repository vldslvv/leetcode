from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        for i in range(k, len(nums)):
            heapq.heappush(min_heap, nums[i])
            heapq.heappop(min_heap)

        return heapq.heappop(min_heap)

        
nums = [3,2,1,5,6,4]
k = 2
s = Solution()
res = s.findKthLargest(nums, k)
print(res)
