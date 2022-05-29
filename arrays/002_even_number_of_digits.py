class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n_even = 0
        for n in nums:
            if num_digits2(n) % 2 == 0:
                n_even += 1
        return n_even

def num_digits1(n):
    digits = 1
    n = n // 10
    
    while n != 0:
        n = n // 10
        digits += 1
        
    return digits

def num_digits2(n):
    return len(str(n))
