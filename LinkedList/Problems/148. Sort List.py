# link   : https://leetcode.com/problems/sort-list/description/
# author : Mohamed Ibrahim

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left,right)

    def getMid(self,node):
        slow , fast = node , node.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self,list1,list2):
        tail = dummy = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next

