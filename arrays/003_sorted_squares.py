class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left = 0
        right = len(nums) - 1
        res = right
        squares = [None for _ in range(len(nums))]
        
        while left != right:
           if abs(nums[left]) > abs(nums[right]):
               squares[res] = nums[left]**2
               res -= 1
               left += 1
           else:
               squares[res] = nums[right]**2
               res -= 1
               right -= 1

        squares[res] = nums[left] ** 2
        
        return squares
         