# link : https://leetcode.com/problems/reverse-nodes-in-k-group/
# author : Mohamed Ibrahim

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):

        cnt = 0 
        cur = head
        while cur and cnt < k:
            cur = cur.next
            cnt+=1
        if cnt < k:
            return head

        prev = None
        cur = head
        for i in range(k):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        if cur:
            head.next = self.reverseKGroup(cur, k)
        return prev
        
