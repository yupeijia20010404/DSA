from design_linked_list import ListNode
from typing import Optional
def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    fast = head
    slow = head
    while fast and slow and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    if not fast or not fast.next:
        return None
    new_start = head
    while slow != new_start:
        slow = slow.next
        new_start = new_start.next
    return slow