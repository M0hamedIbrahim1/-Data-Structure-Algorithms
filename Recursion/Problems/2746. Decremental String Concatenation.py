# link   : https://leetcode.com/contest/biweekly-contest-107/problems/decremental-string-concatenation/
# author : Mohamed Ibrahim


class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        cache = {}
        def resc(indx , start , ind):
            if indx == len(words):return 0
            if (indx , start , ind) in cache:
                return cache[(indx , start , ind)]
            
            length1 = float('inf')
            length2 = float('inf')

            if words[indx][0] == ind:
                length1 =  min(length1 ,len(words[indx])-1 + resc(indx+1 , start , words[indx][-1]))
            else:
                length1 =  min(length1 ,len(words[indx]) + resc(indx+1 , start , words[indx][-1]))
            
            if words[indx][-1] == start:
                length2 = min(length2 , len(words[indx])-1 + resc(indx+1 , words[indx][0] , ind))
            else:
                length2 = min(length2 , len(words[indx]) + resc(indx+1 , words[indx][0] , ind))
            
            res = min(length1,length2)
            cache[(indx , start , ind)] = res
            return res
        
        
        
        return len(words[0]) + resc(1 , words[0][0] , words[0][-1])
