class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best_n = 0
        curr_n = 0
        for i, n in enumerate(nums):
            if n == 1:
                curr_n += 1
            if n == 0:
                if curr_n > best_n:
                    best_n = curr_n
                curr_n = 0
                
                if len(nums) - i - 1 <= best_n:
                    return best_n

        if curr_n > best_n:
            return curr_n
            
        return best_n
    
nums = [1,1,0,1,1,1]
s1 = Solution().findMaxConsecutiveOnes(nums)
print(s1)

nums = [1,0,1,1,0,1]
s2 = Solution().findMaxConsecutiveOnes(nums)
print(s2)

nums = [1, 1, 1, 0, 1, 1, 1]
s2 = Solution().findMaxConsecutiveOnes(nums)
print(s2)