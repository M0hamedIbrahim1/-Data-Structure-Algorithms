# link   : https://leetcode.com/contest/weekly-contest-356/problems/shortest-string-that-contains-three-strings/
# author : Mohamed Ibrahim

class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        
        def merge(s1 , s2):
            if s1 in s2:
                return s2
            for i in range(len(s2)):
                if s1.startswith(s2[i:]):
                    return s2[:i] + s1
            return s2+s1
        
        
        res = "a"*999
        for s in [merge(a , merge(b , c)) , merge(a , merge(c , b)) , merge(b , merge(a , c)) , 
                  merge(b , merge(c , a)) ,merge(c , merge(b , a)) , merge(c , merge(a , b)) ]:
            if len(s) < len(res):
                res = s
            elif len(s) == len(res):
                res = min(s , res)
        return res
      
