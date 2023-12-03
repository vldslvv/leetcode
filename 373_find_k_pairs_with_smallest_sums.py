from typing import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        visited = set()
        answer = []
        heap = [(nums1[0] + nums2[0], (0, 0))]
        visited.add((0, 0))

        while heap and len(answer) < k:
            _, (i, j) = heapq.heappop(heap)
            answer.append((nums1[i], nums2[j]))

            if j < len(nums2) - 1 and (i, j + 1) not in visited:
                next1 = (nums1[i] + nums2[j + 1], (i, j + 1))
                heapq.heappush(heap, next1)
                visited.add((i, j + 1))

            if i < len(nums1) - 1 and (i + 1, j) not in visited:
                next2 = (nums1[i + 1] + nums2[j], (i + 1, j))
                heapq.heappush(heap, next2)
                visited.add((i + 1, j))

        return answer


s = Solution()
# a1 = [1,7,11]
a1 = [1, 400]
# a2 = [2,4,6]
a2 = [2, 3]
res = s.kSmallestPairs(a1, a2, 10)
print(res)
