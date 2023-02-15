# Link   : https://leetcode.com/problems/reverse-linked-list/description/
# Author : Mohamed Ibrahim

 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        pre = None
        nxt = None
        while(curr):
            nxt = curr.next # hold the next address of curr
            curr.next = pre # connect current to pre " <- " (reverse node)
            pre = curr # move previous
            curr = nxt # move curr 
            
        return pre
        
        
        
