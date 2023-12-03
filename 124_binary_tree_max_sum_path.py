from tree_parser import parse_tree, TreeNode
from typing import Optional, Tuple


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        abs_max, cont_max = self.inorder(root, -1001, -1001)
        return max(cont_max, abs_max)

    # abs_max_sum is the best sum we know so far, but it cannot be increased anymore since it might be disjoined from the future path
    # cont_max_sum is the bext sum we can increase up the tree hierarchy
    def inorder(self, root, abs_max_sum, cont_max_sum) -> Tuple[int, int]:
        if not root:
            return (abs_max_sum, -1001)

        if not root.left and not root.right:
            return (max(root.val, abs_max_sum), root.val)
        
        # Solve most basic path
        l_abs_sum, l_cont_sum = self.inorder(root.left, abs_max_sum, cont_max_sum)
        center_sum = root.val
        r_abs_sum, r_cont_sum = self.inorder(root.right, abs_max_sum, cont_max_sum)

        cont_sum = max(l_cont_sum + center_sum, center_sum, r_cont_sum + center_sum)
        abs_sum = max(cont_sum, l_abs_sum, r_abs_sum, l_cont_sum + center_sum + r_cont_sum)

        return (abs_sum, cont_sum)


s = Solution()
# root = parse_tree("[1,-2,-3,1,3,-2,null,-1]")
# root = parse_tree("[1,-2,null,1,3]")
root = parse_tree("[1,2,3]")
res = s.maxPathSum(root)
print(res)