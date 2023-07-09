# link   : https://leetcode.com/problems/substring-with-largest-variance/description/
# author : Mohamed Ibrahim

class Solution:
    def largestVariance(self, s: str) -> int:
        pairs = [(a,b) for a in set(s) for b in set(s) if a!=b]
        res = 0
        for i in range(2):
            for pair in pairs:
                c1 , c2 = 0 , 0
                for char in s:
                    if char not in pair:continue

                    if char == pair[0]:c1+=1
                    else:c2+=1

                    if c2 > c1: c1 = c2 = 0
                    elif c1 > 0 and c2 > 0:
                        res = max(res , c1 - c2)
            s = s[::-1]
        return res
