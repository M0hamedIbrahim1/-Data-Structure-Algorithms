# Link   : https://leetcode.com/problems/node-with-highest-edge-score/description/
# author : Mohamed Ibrahim



def edgeScore(self, edges: List[int]) -> int:
    n, ans = len(edges), 0
    scores = [0] * n
    for src, tgt in enumerate(edges):
        scores[tgt] += src
    for i, score in enumerate(scores):
        if score > scores[ans]:
            ans = i
    return ans
