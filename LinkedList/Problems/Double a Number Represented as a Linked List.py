# Link   : https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/description/
# Author : Mohamed Ibrahim

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(node):
            res = (2*node.val) + (dfs(node.next) if node.next else 0)

            node.val = res % 10
            return res // 10


        carry = dfs(head)
        return ListNode(1 , head) if carry else head


                  
