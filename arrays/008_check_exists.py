class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        # For each number, check if there's a double or a half in the array
        # Do not check for odd numbers

        saved = {}
        for i in range(len(arr)):
            n = arr[i]
            if n in saved:
                return True

            saved[n * 2] = True
            if n % 2 == 0:
                saved[n / 2] = True
        return False
        