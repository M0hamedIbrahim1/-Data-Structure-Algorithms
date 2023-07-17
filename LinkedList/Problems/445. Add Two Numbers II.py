# link   : https://leetcode.com/problems/add-two-numbers-ii/description/
# author : Mohamed Ibrahim
class Solution:
    def helper(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        result = None
        carry = 0

        while stack1 or stack2 or carry:
            digit1 = stack1.pop() if stack1 else 0
            digit2 = stack2.pop() if stack2 else 0

            total = digit1 + digit2 + carry
            digit = total % 10
            carry = total // 10

            newNode = ListNode(digit)
            newNode.next = result
            result = newNode

        return result

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = self.helper(l1, l2)
        return ans
