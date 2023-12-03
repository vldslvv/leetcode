from typing import Dict, Tuple


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = {}
        res = self.dp(0, 0, m, text1, text2)
        return res

    # k -- longest substring so far
    # fst -- index of first string to search from
    # snd -- index of second string to search from
    # m -- dictionary of (fst, snd): k -- memoized values of longest substring
    def dp(self, fst: int, snd: int, m: Dict[Tuple[int, int], int], text1: str, text2: str) -> int:
        if fst >= len(text1) or snd >= len(text2):
            return 0

        if (fst, snd) in m:
            return m[(fst, snd)]
        
        # Two cases on each pass: first letter match
        if text1[fst] == text2[snd]:
            longest = 1 + self.dp(fst + 1, snd + 1, m, text1, text2)
            m[(fst, snd)] = longest
            return longest
        # second case -- letters do not match
        else:
            left, right = (self.dp(fst + 1, snd, m, text1, text2), self.dp(fst, snd + 1, m, text1, text2))
            longest = max(left, right)
            m[(fst, snd)] = longest
            return longest


s = Solution()
# a = ("abc", "aab")
# a = ("abcde", "ace")

a = ("bl", "yby")
a = ("lb", "yby")
res = s.longestCommonSubsequence(a[0], a[1])
print(res)
