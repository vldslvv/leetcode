from linked_list import *
from typing import Optional


class Solution:
    def reverseList_iter(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=-1, next=None)

        # head will be tail after a reverse
        curr = head
        # Once head doesn't have any nodes left, it's reversed
        while curr:
            # Save removed node
            removed_node = curr
            # Remove it from the original list
            curr = curr.next
            # Put it in front of previous reversed tail
            removed_node.next = dummy.next
            # Make it a head of reversed list
            dummy.next = removed_node

        return dummy.next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next:
            new_head = self.reverseList(head.next)
            


# ll = parse_linked_list("[1,2,3,4,5]")
ll = parse_linked_list("[1,2]")
ll = parse_linked_list("[1]")
ll = parse_linked_list("[]")
s = Solution()
res = s.reverseList(ll)
print_linked_list(res)