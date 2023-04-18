# Link : https://leetcode.com/problems/word-ladder/description/
# author : Mohamed Ibrahim 

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord  not in wordList :
            return 0
        visited = set()
        visited.add(beginWord)
        q = deque([beginWord])

        Dict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                Dict[pattern].append(word)
        res = 1
        while q:
            for i in range(len(q)):
                w = q.popleft()
                if w == endWord:return res
                for j in range(len(w)):
                    pattern = w[:j]+"*"+w[j+1:]
                    for neigh in Dict[pattern]:
                        if neigh not in visited:
                            q.append(neigh)
                            visited.add(neigh)
            res+=1
        return 0
        

