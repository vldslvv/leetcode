from tree_parser import TreeNode, parse_tree
from typing import Optional


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # dfs iteratively, on each step multiplying current sum by ten

        stack = [(root, root.val)]
        total = 0
        while stack:
            node, node_sum = stack.pop()

            if not node.right and not node.left:
                total += node_sum
                continue

            curr_sum = node_sum * 10
            if node.right:
                stack.append((node.right, curr_sum + node.right.val))
            if node.left:
                stack.append((node.left, curr_sum + node.left.val))

        return total
