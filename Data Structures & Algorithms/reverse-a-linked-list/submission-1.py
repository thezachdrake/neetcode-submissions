# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev : ListNode | None = None
        current: ListNode | None = head
        while current is not None:
            next_node = current.next   # save where we're going
            current.next = prev        # reverse the pointer
            prev = current             # advance prev
            current = next_node        # advance current
        return prev