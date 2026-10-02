# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None

        current = second_half
        previous = None
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        
        second_half = previous
        first_half = head
        while second_half:
            first_half_next = first_half.next
            second_half_next = second_half.next

            first_half.next = second_half
            second_half.next = first_half_next

            first_half = first_half_next
            second_half = second_half_next