# link   : https://leetcode.com/problems/find-the-town-judge/description/
# Author : Mohamed Ibrahim


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        to_me = [0]*(n+1)
        from_me = [0]*(n+1)
        for x,y in trust:
            from_me[x]+=1
            to_me[y]+=1
        for i in range(1,n+1):
            if from_me[i] == 0 and to_me[i] == n-1:
                return i
        return -1
        
        
        
        
