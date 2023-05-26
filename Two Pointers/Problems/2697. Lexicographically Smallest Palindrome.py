# link   : https://leetcode.com/contest/weekly-contest-346/problems/lexicographically-smallest-palindrome/
# author : Mohamed Ibrahim

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        def make_Palindrome(i , j):
            while i >= 0 and j < len(s):
                if s[i] != s[j] and s[i] < s[j] : 
                    s[j] = s[i]
                elif s[i] != s[j] and s[j] < s[i]:
                    char = s[j]
                    s[i] = char
                i-=1 ; j+=1

        indx = len(s) // 2
        if len(s) % 2:make_Palindrome(indx , indx)
        else:make_Palindrome(indx-1 , indx)
        return ''.join(s)
        
