from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid

            if target <= nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return start if target <= nums[start] else start + 1

        
s = Solution()
# res = s.searchInsert([1,3,5,6], 5)
# assert res == 2

# res = s.searchInsert([1,3,5,6], 2)
# assert res == 1

# res = s.searchInsert([1,3,5,6], 7)
# print(res)
# assert res == 4

res = s.searchInsert([1,3], 0)
print(res)