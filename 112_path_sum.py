from tree_parser import parse_tree, TreeNode
from typing import Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # Do an iterative dfs
        # Each tuple contains current node and path sum
        s = [(root, root.val)]

        while s:
            node, path_sum = s.pop()

            # If leaf node and target sum is found
            if not node.right and not node.left and path_sum == targetSum:
                return True
            
            if node.right:
                s.append((node.right, path_sum + node.right.val))
            if node.left:
                s.append((node.left, path_sum + node.left.val))
        
        return False


s = Solution()
root = parse_tree("[5,4,8,11,null,13,4,7,2,null,null,null,1]")
res = s.hasPathSum(root, 22)
print(res)
