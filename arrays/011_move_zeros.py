class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # where to put next non-zero value
        i = 0
        # running index
        j = 0
        
        for j in range(len(nums)):
            if nums[j] == 0:
                continue
            else:
                # Swap ith and jth elements
                if i != j:
                    nums[i] = nums[j]
                    nums[j] = 0
                i += 1