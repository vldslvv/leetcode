
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Check in pairs?
        # Interate array only once, len(nums) times
        # Two indices, i (which indicates a non-duplicate element)
        # j indicates an element to compare to
        # while elements by indices are equal, comtinue to increase j
        # once finished, shift non-duplicated element to i + 1
        # continue running j
        
        length = len(nums)
        if length < 2:
            return length
        
        i = 0
        j = 1
        for _ in range(length - 1):
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i + 1] = nums[j]
                i += 1
                j += 1
                
        return i + 1