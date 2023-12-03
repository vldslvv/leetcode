from tree_parser import parse_tree, print_in_order, print_post_order, TreeNode
from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.dfs(preorder, inorder, 0, 0, len(preorder) - 1)


    def dfs(self, preorder: List[int], inorder: List[int], preorder_root_id: int, start_inorder: int, end_inorder: int) -> TreeNode:
        # If tree has no elements
        if end_inorder < start_inorder:
            return None

        # We know root value straight away since preorder
        # visits root first
        root = TreeNode(val=preorder[preorder_root_id])
        print(root.val)

        # If there's only one element in the tree
        if end_inorder == start_inorder:
            return root

        # Find root index in inorder
        root_id_inorder = inorder.index(root.val)

        # Now we know left an right subtree bounds since
        # inorder visits root in the middle of traversal
        l_start_inorder, l_end_inorder = start_inorder, root_id_inorder - 1
        r_start_inorder, r_end_inorder = root_id_inorder + 1, end_inorder

        # Postorder start from 1st element
        # For postorder we don't need to know the end element since the array slices
        # Are glued together when doing DFS
        l_start_preorder = preorder_root_id + 1
        len_left_tree = l_end_inorder - l_start_inorder + 1
        r_start_preorder = preorder_root_id + 1 + len_left_tree

        # recursively go into subtrees
        root.left = self.dfs(preorder=preorder, inorder=inorder, preorder_root_id=l_start_preorder, start_inorder=l_start_inorder, end_inorder=l_end_inorder)
        root.right = self.dfs(preorder=preorder, inorder=inorder, preorder_root_id=r_start_preorder, start_inorder=r_start_inorder, end_inorder=r_end_inorder)

        return root


s_tree1 = "[3,9,20,null,null,15,7]"
# s_tree2 = "[3,9,20,15,7]"

t1 = parse_tree(s_tree1)
# t2 = parse_tree(s_tree2)

# print_post_order(t1)
# print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
# print_in_order(t1)
# print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
# print_post_order(t2)
# print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
# print_in_order(t2)

s = Solution()
root = s.buildTree([3,9,20,15,7], [9,3,15,20,7])
