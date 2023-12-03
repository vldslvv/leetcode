from typing import Tuple, Optional, List
from math import floor
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_children_ids(parent_id: int) -> Tuple[int, int]:
    return (2 * parent_id + 1, 2 * parent_id + 2)


def get_parent_id(child_id: int) -> int:
    # TODO if needed ever
    raise NotImplementedError()


def get_children(parent_id: int, tree: List[Optional[int]]) -> Tuple[Optional[int], Optional[int]]:
    left_id, right_id = get_children_ids(parent_id)
    return tree[left_id] if left_id < len(tree) else None, tree[right_id] if right_id < len(tree) else None


def parse_tree(str_tree: str) -> Optional[TreeNode]:
    # Assume correct input
    s = str_tree.strip("[]")
    if not s or len(s) == 0:
        return None
    tree = list(map(lambda int_or_null: None if int_or_null == "null" else int(int_or_null), s.split(",")))
    if not tree or len(tree) == 0:
        return None

    # Use BFS to construct a tree
    root = TreeNode(val=tree[0])
    q = deque()
    q.appendleft((root, 0))
    while q:
        node, index = q.pop()
        left_id, right_id = get_children_ids(index)

        # Get children if they are inside list's bounds and are not None
        left = TreeNode(val=tree[left_id]) if left_id < len(tree) and tree[left_id] else None
        right = TreeNode(val=tree[right_id]) if right_id < len(tree) and tree[right_id] else None

        node.left = left
        node.right = right
        if left:
            q.appendleft((left, left_id))
        if right:
            q.appendleft((right, right_id))

    return root


def print_in_order(root: Optional[TreeNode]) -> None:
    if not root:
        return
    
    print_in_order(root.left)
    print(root.val)
    print_in_order(root.right)


def print_post_order(root: Optional[TreeNode]) -> None:
    if not root:
        return
    
    print(root.val)
    print_post_order(root.left)
    print_post_order(root.right)


# a = "[3,9,20,null,null,15,7]"
# # a = "[]"
# root = parse_tree(a)
# print(root)


# # print_in_order(root)
# print_post_order(root)
