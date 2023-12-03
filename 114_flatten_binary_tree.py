from typing import Optional, List
from tree_parser import TreeNode, parse_tree, print_post_order


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.dfs(root)
        self.rotate(root)

    def rotate(self, node: TreeNode) -> TreeNode:
        if node.left:
            node.right = node.left
            node.left = None
            return self.rotate(node.right)
        return node
    
    def dfs(self, node: TreeNode) -> TreeNode:
        # Return leaf node
        if not node.left and not node.right:
            return node

        left_leaf = None
        if node.left:
            left_leaf = self.dfs(node.left)
        if node.right:
            if left_leaf:
                left_leaf.left = node.right
                node.right = None
                return self.dfs(left_leaf.left)
            else:
                node.left = node.right
                node.right = None
                return self.dfs(node.left)

        return node
        

class Solution1:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.preorder_ll(root)

    # return right tail at the end
    def preorder_ll(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        if not root.left and not root.right:
            return root

        if not root.left:
            return self.preorder_ll(root.right)

        if not root.right:
            root.right = root.left
            root.left = None
            return self.preorder_ll(root.right)

        # Assign left branch as right, find its tail
        # Assign right branch to new found tail

        old_right = root.right
        root.right = root.left
        root.left = None
        right_tail = self.preorder_ll(root.right)
        right_tail.right = old_right

        # # Potentiall right_tail cannot be None, TODO verify
        # if right_tail:
        # else:
        #     root.right = old_right

        return self.preorder_ll(old_right)
        

def get_linked_list(root: TreeNode) -> List[int]:
    curr_node = root
    result = []
    while curr_node:
        result += [curr_node.val]
        curr_node = curr_node.right
    return result




# node_6 = TreeNode(val=6)
# node_5 = TreeNode(val=5, right=node_6)
# node_4 = TreeNode(val=4)
# node_3 = TreeNode(val=3)
# node_2 = TreeNode(val=2, left=node_3, right=node_4)
# root = TreeNode(val=1, left=node_2, right=node_5)

# root = parse_tree("[1,2,5,3,4,null,6]")
root = parse_tree("[1,2]")

s = Solution1()
res = s.flatten(root)
linked_list = get_linked_list(root)
print(linked_list)