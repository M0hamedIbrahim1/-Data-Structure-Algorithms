# link : https://leetcode.com/problems/longest-string-chain/description/?envType=daily-question&envId=2023-09-23
# author : Mohamed Ibrahim

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda w : -len(w))
        words_index = {}
        for i in range(len(words)):
            words_index[words[i]] = i
        
        @cache
        def dfs(i):
            if i >= len(words):
                return 0
            res = 1
            for j in range(len(words[i])):
                W = words[i]
                pred = W[:j]+W[j+1:]
                if  pred in words_index:
                    res = max(res , 1 + dfs(words_index[pred]))
            return res

        ans = 0
        for i in range(len(words)):
            ans = max( ans , dfs(i))
        return ans
