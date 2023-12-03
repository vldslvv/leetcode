from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            pi, qi = stack.pop()
            if not pi and not qi:
                continue
            if not pi or not qi:
                return False
            if pi.val != qi.val:
                return False

            if pi:
                stack.append((pi.left, qi.left))
                stack.append((pi.right, qi.right))
            
        return True

s = Solution()
res = s.isSameTree(None, None)
print(res)