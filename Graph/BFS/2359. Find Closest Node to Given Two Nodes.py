# link   : https://leetcode.com/problems/find-closest-node-to-given-two-nodes/
# author : Mohamed Ibrahim


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        graph = collections.defaultdict(list)
        for i,src in enumerate(edges):
            graph[i].append(src)
        
        def bfs(node,dist):
            q = deque()
            q.append([node,0])
            dist[node] = 0
            
            while q:
                n , dist_from_node = q.popleft()
                for neigh in graph[n]:
                    if neigh not in dist:
                        q.append([neigh,dist_from_node+1])
                        dist[neigh] = dist_from_node+1

        d_ofNode1 = {}
        d_ofNode2 = {}
        bfs(node1,d_ofNode1)        
        bfs(node2,d_ofNode2)

        res = -1
        x = float("inf")
        for i in range(len(edges)):
            if i in d_ofNode1 and i in d_ofNode2:
                distance = max(d_ofNode1[i],d_ofNode2[i])
                if distance < x:
                    x = distance
                    res = i
        return res
        
        
