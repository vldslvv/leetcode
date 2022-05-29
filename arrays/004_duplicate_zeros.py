
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        shift = 0
        for el in arr:
            if el == 0:
                shift += 1
                
        for i in range(len(arr) - 1, -1, -1):
            # If we can shift the original element
            if shift + i < len(arr):
               arr[shift + i] = arr[i]
            
            # If we have zero, duplicate it to the left
            if arr[i] == 0:
                shift -= 1
                if shift + i < len(arr):
                    arr[shift + i] = arr[i]