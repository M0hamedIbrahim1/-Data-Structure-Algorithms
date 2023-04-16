# link   : https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
# author : Mohamed Ibrahim

class Solution:
    def longestSubstring(self, s, k):
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)
      
      
