from typing import List


def search(start: int, end: int, nums: List[int], target: int) -> int:
    # If only one elemnet is in slice
    if end - start == 0:
        # return start if nums[start] <= target else start + 1
        return start if target <= nums[start] else start + 1

    middle = start + (end - start) // 2
    # If it's not possible to find it anywhere but in between the arrays
    if target > nums[middle] and target < nums[middle + 1]:
        return middle + 1

    if target <= nums[middle]:
        return search(start, middle, nums, target)
    
    return search(middle + 1, end, nums, target)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return search(0, len(nums) - 1, nums, target)
        

s = Solution()
res = s.searchInsert([1,3,5,6], 5)
assert res == 2

res = s.searchInsert([1,3,5,6], 2)
assert res == 1

res = s.searchInsert([1,3,5,6], 7)
print(res)
assert res == 4
