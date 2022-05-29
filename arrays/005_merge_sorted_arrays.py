
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        # Start from right side of each array
        # Write to resulting array in reverse order
        # Compare right-most elements of each array
        # Take the largest and insert it in resulting array to the right-most
        
        r1 = m - 1
        r2 = n - 1
        res = m + n - 1
        
        while r1 >= 0 and r2 >= 0:
            if nums1[r1] >= nums2[r2]:
                nums1[res] = nums1[r1]
                r1 -= 1
            else:
                nums1[res] = nums2[r2]
                r2 -= 1
            res -= 1
            
        while r1 >= 0:
            nums1[res] = nums1[r1]
            res -= 1
            r1 -= 1
            
        while r2 >= 0:
            nums1[res] = nums2[r2]
            res -= 1
            r2 -= 1 
            