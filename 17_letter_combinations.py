from typing import List
from collections import deque


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        d = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        n = len(digits)
        q = deque()
        for letter in d[digits[0]]:
            q.appendleft((letter, 1))
        result = []
        while q:
            # Get current combination and tree level
            combo, level = q.pop()
            if level != n:
                for letter in d[digits[level]]:
                    q.appendleft((combo + letter, level + 1))
            else:
                result += [combo]

        return result

s = Solution()
nums = "2222"
res = s.letterCombinations(nums)
print(res)