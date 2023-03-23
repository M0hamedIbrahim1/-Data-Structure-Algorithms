import collections
import heapq
n = 5
edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]

graph = collections.defaultdict(list)       # build graph
for a, b, w in edges:
    graph[a].append((w, b))
    graph[b].append((w, a))
heap = graph[n]

heap = graph[n]
d = {n: 0}

while heap:                                 # Dijkstra from node `n` to other nodes, record shortest distance to each node
    cur_w, cur = heapq.heappop(heap)
    if cur in d: continue
    d[cur] = cur_w
    for w, nei in graph[cur]:
        heapq.heappush(heap, (w+cur_w, nei))

for src,destination in d.items():
       print("min cost from : ",n,"to :",src," = ",destination)
       
      
