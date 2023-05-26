# link : https://leetcode.com/contest/weekly-contest-346/problems/minimum-string-length-after-removing-substrings
# author : Mohamed Ibrahim

class Solution:
    def minLength(self, s: str) -> int:
        
        # Input: s = "ABFCACDB"
        # Output: 2
        stack = []
        for i in range(len(s)):
            if s[i] == 'B' and stack and stack[-1] == 'A':
                stack.pop()
            elif s[i] == 'D' and stack and stack[-1] == 'C':
                stack.pop()
            else:stack.append(s[i])
        return len(stack)
        
