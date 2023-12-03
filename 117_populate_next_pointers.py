# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        q = deque()
        # Store node and its level to point only within the same level
        q.appendleft((root, 0))
        prev_node = None
        prev_level = 0
        while q:
            node, level = q.pop()
            if prev_level == level:
                level.next = prev_node
            # Might be redundant, check
            else:
                level.next = None

            # Put into queue in reverse order
            if node.right:
                q.appendleft((node.right, level + 1))
            if node.left:
                q.appendleft((node.left, level + 1))

            prev_node = node
            prev_level = level

        return root
        