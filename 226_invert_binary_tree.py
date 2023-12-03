from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        self.dfs(root)
        return root
        
    def dfs(self, root) -> None:
        root.left, root.right = root.right, root.left
        if root.left:
            self.dfs(root.left)
        if root.right:
            self.dfs(root.right)
