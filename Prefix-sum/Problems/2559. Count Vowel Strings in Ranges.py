# link   : https://leetcode.com/problems/count-vowel-strings-in-ranges/description/
# author : Mohamed Ibrahim

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'} 
        val = [0] * (len(words) + 1)
        res = []

        # Calculate cumulative sums
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                val[i+1] = val[i] + 1
            else:
                val[i+1] = val[i]

        # Calculate the sum for each query
        for l, r in queries:
            res.append(val[r+1] - val[l])

        return res
      
