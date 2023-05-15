# link   : https://leetcode.com/problems/reorder-list/description/
# author : Mohamed Ibrahim

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return []
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev,cur = None , slow.next
        while cur:
            Next = cur.next
            cur.next = prev
            prev = cur
            cur = Next
        slow.next = None
        head1 , head2 = head ,prev
        while head2:
            Next = head1.next
            Next_head2 = head2.next

            head1.next = head2
            head2.next = Next

            head1 = Next
            head2 = Next_head2
