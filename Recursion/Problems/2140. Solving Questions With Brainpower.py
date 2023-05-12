# link : https://leetcode.com/problems/solving-questions-with-brainpower/description/
# author : Mohamed Ibrahim

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        cache = {}
        def resc(i):
            if i in cache:
                return cache[i]
            if i >= len(questions):return 0

            cache[i] = max(questions[i][0]+ resc(i+questions[i][1]+1) , resc(i+1))
            return cache[i]            
        return resc(0)

