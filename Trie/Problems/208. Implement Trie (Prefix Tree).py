# link   : https://leetcode.com/problems/implement-trie-prefix-tree/description/
# author : Mohamed Ibrahim



class TrieNode:
    def __init__(self):
        self.d = {}
        self.end_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur.d:
                cur.d[i] = TrieNode()
            cur = cur.d[i]
        cur.end_word = True
        
    def search(self, word: str) -> bool:
        cur = self.root
        for i in word:
            if i not in cur.d:
                return False
            cur = cur.d[i]
        return cur.end_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in prefix:
            if i not in cur.d:
                return False
            cur = cur.d[i]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

