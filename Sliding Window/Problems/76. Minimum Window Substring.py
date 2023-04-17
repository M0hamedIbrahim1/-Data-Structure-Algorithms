# link   : https://leetcode.com/problems/minimum-window-substring/description/
# author : Mohamed Ibrahim

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d_t = Counter(t)
        d_s = defaultdict(int)
        have , Full = 0 , len(d_t)
        l ,mn = 0,float('inf')
        substring = ""
        ans = [[float('inf'),substring]]
        for i in range(len(s)):
            d_s[s[i]]+=1

            if d_t[s[i]] == d_s[s[i]]:
                have+=1

            while have == Full and l <= i:
                # mn
                if len(s[l:i+1]) < ans[0][0]:
                    ans[0][0] = len(s[l:i+1])
                    ans[0][1] = s[l:i+1] 
                c = s[l]
                d_s[c]-=1
                if c in d_t and d_s[c] < d_t[c]:
                    have-=1
                l+=1
        return ans[0][1]
        
        
