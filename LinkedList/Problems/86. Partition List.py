# link   : https://leetcode.com/problems/partition-list/description/
# author : Mohamed ibrahim

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lst = []
        lst2 = []
        cur = head
        while cur:
            if cur.val < x:
                lst.append(cur.val)
            else:
                lst2.append(cur.val)
            cur = cur.next
        
        node = dummy = ListNode()

        for i in range(len(lst)):
            node.next = ListNode(lst[i])
            node = node.next
        for i in range(len(lst2)):
            node.next = ListNode(lst2[i])
            node = node.next
        return dummy.next
