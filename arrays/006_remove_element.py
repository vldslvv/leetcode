
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
       
        # Go from the start of the array
        # When val to delete occurs, add 1 to shift var
        # If next value is not val, shift it
        # k = shift

        shift = 0

        for i in range(len(nums)):
            if nums[i] == val:
                shift += 1
            else:
                nums[i - shift] = nums[i]
                
        return len(nums) - shift