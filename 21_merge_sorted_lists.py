from linked_list import parse_linked_list, print_linked_list, ListNode
from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=None)
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2

        return dummy.next


s = Solution()
l1 = parse_linked_list("[1,2,4]")
l2 = parse_linked_list("[1,3,4]")
res = s.mergeTwoLists(l1, l2)
print_linked_list(res)
