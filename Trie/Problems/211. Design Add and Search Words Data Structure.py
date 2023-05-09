# link   : https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
# author : Mohamed Ibrahim

class WordDictionary:

    def __init__(self):
        self.root = {}
        
    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node: node[c] = {}
            node = node[c]
        node['*'] = False
        
    def search(self, w: str) -> bool:
    	def dfs(node, i):
    		if node == False: return False
    		if i == L: return '*' in node
    		if w[i] != '.':
    			if w[i] not in node: return False
    			return dfs(node[w[i]],i+1)
    		for j in node.values():
    			if dfs(j,i+1): return True
    		return False
    	node, L = self.root, len(w)
    	return dfs(node,0)
		
