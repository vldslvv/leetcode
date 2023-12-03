from linked_list import ListNode, parse_linked_list, print_linked_list, linked_list_to_list
from typing import Optional, Tuple


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # First, find left and right halves of the list
        left, right = self.split(head)

        if not right:
            return left
        if not left:
            return right

        l_sorted = self.sortList(left)
        r_sorted = self.sortList(right)

        head = None
        tail = None
        # 2 -> 4
        # 1 -> 3
        while l_sorted and r_sorted:
            if l_sorted.val < r_sorted.val:
                if tail:
                    tail.next = l_sorted
                    tail = tail.next
                else:
                    tail = l_sorted
                if not head:
                    head = l_sorted
                l_sorted = l_sorted.next
            else:
                if tail:
                    tail.next = r_sorted
                    tail = tail.next
                else:
                    tail = r_sorted
                if not head:
                    head = r_sorted
                r_sorted = r_sorted.next
            tail.next = None

        # If there are some remainders after merge
        if l_sorted:
            tail.next = l_sorted
        if r_sorted:
            tail.next = r_sorted

        return head

    def split(self, head: ListNode) -> Tuple[Optional[ListNode], Optional[ListNode]]:
        if not head:
            return (None, None)
        if not head.next:
            return (head, None)

        # Two runners, one steps over one node (if it can)
        # Second runner steps to next node
        half = head
        left_tail = head.next
        tail = head
        while tail:
            tail = None if not tail.next else tail.next if not tail.next.next else tail.next.next
            if tail:
                left_tail = half
                half = half.next

        left_tail.next = None

        return (head, half)


s = Solution()
# ll = parse_linked_list("[4,2,1,3]")
# ll = parse_linked_list("[4,2,1]")
# ll = parse_linked_list("[4,1]")
# ll = parse_linked_list("[1]")
ll = parse_linked_list("[-1,5,3,4,0]")
res = s.sortList(ll)
print_linked_list(res)
