from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def parse_linked_list(s: str) -> Optional[ListNode]:
    # Assume correct input
    s = s.strip("[]")
    if not s or len(s) == 0:
        return None
    linked_list = list(map(lambda int_or_null: None if int_or_null == "null" else int(int_or_null), s.split(",")))

    prev_node = None
    for value in reversed(linked_list):
        curr_node = ListNode(val=value)
        if prev_node:
            curr_node.next = prev_node
        prev_node = curr_node
    
    return prev_node


def linked_list_to_list(head: Optional[ListNode]) -> List:
    curr_node = head
    result = []
    while curr_node:
        result.append(curr_node.val)
        curr_node = curr_node.next

    return result
    

def print_linked_list(head: Optional[ListNode]) -> None:
    l = linked_list_to_list(head)
    print(l)
