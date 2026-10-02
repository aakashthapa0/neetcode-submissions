# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy = ListNode(0, head)
        before_left = dummy

        for _ in range(left - 1):
            before_left = before_left.next
        
        current = before_left.next
        previous = None
        tail = current

        for _ in range(right - left + 1):
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        
        before_left.next = previous
        tail.next = current
        return dummy.next