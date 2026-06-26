# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_list = []
        if head is None:
            return head
        current: ListNode | None = head
        while current is not None:
            if current.next is not None:
                temp_list.append(current)
                current = current.next
            if current.next is None:
                temp_list.append(current)
                current = None

        reversed_list = list(reversed(temp_list))
        for idx, node in enumerate(reversed_list):
            if idx == len(temp_list) - 1:
                node.next = None
            else: 
                node.next = reversed_list[idx + 1]
        return temp_list[-1]
