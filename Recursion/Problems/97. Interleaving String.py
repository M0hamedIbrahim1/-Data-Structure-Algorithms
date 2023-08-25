# link   : https://leetcode.com/problems/interleaving-string/description/
# author : Mohamed Ibrahim
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        n1 , n2 , n3 = len(s1) , len(s2) , len(s3)
        if n1 + n2 != n3:return False
        @cache
        def resc(i , j , k ):
            if k == n3:
                return True

            ans = False
            if i < n1 and s1[i] == s3[k]:
                ans = ans or resc(i + 1 , j , k + 1 )
            if j < n2 and s2[j] == s3[k]:
                ans = ans or resc(i , j + 1 , k + 1)

            return ans
        return resc(0 , 0 , 0 )




