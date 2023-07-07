# link   : https://leetcode.com/problems/maximize-the-confusion-of-an-exam/description/
# author : Mohamed Ibrahim

class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        d = Counter(s[:k])
        l,r = 0,k
        res = k
        while r < len(s):
            d[s[r]]+=1
            while l < len(s) and d['T'] + d['F'] > max(d['T'] , d['F']) + k :
                d[s[l]]-=1
                l+=1
            res = max(res ,d['T'] + d['F'] )
            r+=1
        return res
