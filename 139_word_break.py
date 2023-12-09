from typing import List, Dict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # State stores i -- index of a letter to start searching from
        # Assume that previous subproblem before i-th was solved
        m = {}
        return self.dp(0, m, s, wordDict)

    def dp(self, i: int, m: Dict, s: str, wordDict: List[str]) -> bool:
        if i == len(s):
            return True

        if i in m:
            return m[i]

        is_solved = False
        # We cannot exit early at first solution found, but iterate through whole tree
        for w in wordDict:
            if s[i:].startswith(w):
                w_solved = self.dp(i + len(w), m, s, wordDict)

                # If at least once the later subproblems are solved, mark i-th subproblem solved
                if w_solved:
                    is_solved = True

        m[i] = is_solved
        return is_solved

s = Solution()
w = "catsandog"
d = ["cats","dog","sand","and","cat"]
res = s.wordBreak(w, d)
print(res)
