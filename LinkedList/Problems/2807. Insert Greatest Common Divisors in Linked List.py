# link   : https://leetcode.com/contest/biweekly-contest-110/problems/insert-greatest-common-divisors-in-linked-list/
# author : Mohamed Ibrahim

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        cur = head
        while cur:
            lst.append(cur.val)
            cur = cur.next
            
        # print(lst)
        Linked_list = []
        n = len(lst)
        for i in range(n - 1):
            Linked_list.append(lst[i])
            Linked_list.append(gcd(lst[i] , lst[i+1]))
        Linked_list.append(lst[n-1])
        # print(Linked_list)
        temp = CUR = ListNode()
        for i in range(len(Linked_list)):
            CUR.next = ListNode(Linked_list[i])
            CUR = CUR.next
        return temp.next
