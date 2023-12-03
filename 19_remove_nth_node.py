from linked_list import parse_linked_list, print_linked_list, ListNode
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fake = ListNode(val=-1, next=head)
        first = fake
        second = fake

        for _ in range(0, n):
            first = first.next

        while first.next:
            first = first.next
            second = second.next

        second.next = second.next.next

        return fake.next


        # # First, step N times if we can
        # prev = head
        # remove = head
        # tail = head

        # # Before moving remove an tail in sync, move tail N times to make a gap
        # i = 1
        # while tail.next and i < n:
        #     i += 1
        #     tail = tail.next

        # # Now, search until tail
        # while tail.next:
        #     tail = tail.next
        #     prev = remove
        #     remove = remove.next

        # prev.next = remove.next

        # # If there's one element in the list
        # if head == tail:
        #     return None
        # # If the element is the first one
        # if prev == remove:
        #     return remove.next
        # return head
        
s = Solution()
ll = parse_linked_list("[1,2,3]")
res = s.removeNthFromEnd(ll, 1)
print_linked_list(res)
