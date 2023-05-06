# link   : https://leetcode.com/problems/find-all-anagrams-in-a-string/
# author : Mohamed Ibrahim

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d = Counter(p)
        Window = None 
        res = []
        for i in range(1+len(s)-len(p)):
            if i == 0:
                Window = Counter(s[:len(p)])
            else:
                Window[s[i-1]]-=1
                if Window[s[i-1]] == 0:del Window[s[i-1]]
                Window[s[i+len(p)-1]]+=1
            if d == Window:
                res.append(i)
        return res
