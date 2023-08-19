# link   : 2825. Make String a Subsequence Using Cyclic Increments
# author : Mohamed Ibrahim

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n = len(str2)
        i = j = 0
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                i+=1;j+=1
            else:
                if str1[i] == 'z':
                    if 'a' == str2[j]: i+=1;j+=1
                    else:i+=1
                else:
                    if ord(str1[i]) + 1 == ord(str2[j]): i+=1;j+=1
                    else:i+=1
                    
            if j == n:return True
        return False



