# link : https://leetcode.com/problems/length-of-the-longest-valid-substring/description/
# author : Mohamed Ibrahim

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        s = set(forbidden)
        res = left = 0
        for i in range(len(word)):

            for j in range(max(left, i - 10), i+1):

                if word[j:i+1] in s:
                    left = j+1
                 
            res = max(res, i - left + 1)
        
        return res
