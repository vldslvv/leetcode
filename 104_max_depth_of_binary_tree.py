from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # return self.dfs(root, 0)
        # return self.dfs_iter(root)
        return self.bfs_iter(root)

    def dfs(self, node: Optional[TreeNode], level: int) -> int:
        if node == None:
            return level
        
        return max(self.dfs(node.left, level + 1), self.dfs(node.right, level + 1))

    def dfs_iter(self, node: Optional[TreeNode]) -> int:
        if node == None:
            return 0
        stack = [(node, 1)]
        max_depth = 1
        while stack:
            node, level = stack.pop()
            if level > max_depth:
                max_depth = level
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))

        return max_depth

    def bfs_iter(self, node: Optional[TreeNode]) -> int:
        if node == None:
            return 0
        
        q = deque()
        q.appendleft((node, 1))
        max_depth = 1

        while q:
            node, level = q.pop()
            if max_depth > level:
                max_depth = level
            if node.left:
                q.appendleft((node.left, level + 1))
            if node.right:
                q.appendleft((node.right, level + 1))
        
        return max_depth
