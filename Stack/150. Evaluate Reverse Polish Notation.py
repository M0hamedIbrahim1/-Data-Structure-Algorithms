# link   : https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
# author : Mohamed Ibrahim

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        chars = ['+','*','/','-']
        stack = []
        for c in tokens:
            if c not in chars:
                stack.append(int(c))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if c == '+':
                    stack.append(num1+num2)
                if c == '-':
                    stack.append(num1-num2)
                if c == '*':
                    stack.append(num1*num2)
                if c == '/':
                    stack.append(int(num1/num2))
        return stack[-1]
      
      
      
