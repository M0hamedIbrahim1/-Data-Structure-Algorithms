# link   : https://leetcode.com/problems/longest-common-prefix/description/
# author : Mohamed Ibrahim

class Trie:
    def __init__(self):
        self.d = {}
        self.endword = False
    def add_words(self,word):
        cur = self
        for w in word:
            if w not in cur.d:
                cur.d[w] = Trie()
            cur = cur.d[w]
        cur.endword = True
    def calc_mx_length(self,res,w1):
        cur = self
        i = 0
        if len(w1) == 0: return res
        while len(cur.d) == 1 and not cur.endword :
            res+=w1[i]
            cur = cur.d[w1[i]]
            i+=1
        return res
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        my_trie = Trie()
        for word in strs:
            my_trie.add_words(word)
        res = ""
        return my_trie.calc_mx_length(res,strs[0])
        
