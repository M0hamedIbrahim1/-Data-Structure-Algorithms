# link   : https://leetcode.com/problems/word-break-ii/description/
# author : Mohamed Ibrahim

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        words = []
        n = len(s)

        def backtracking(i):
            if i == n:
                res.append(" ".join(words))
            for w in wordDict:
                if s[i:i+len(w)] == w:
                    words.append(w)
                    backtracking(i+len(w))
                    words.pop()

        backtracking(0)
        return res
        
