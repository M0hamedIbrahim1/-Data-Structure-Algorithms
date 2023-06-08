# link : https://leetcode.com/problems/design-graph-with-shortest-path-calculator/description/
# author : Mohamed Ibrahim


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.Graph = defaultdict(list)
        for fr,to,edgeCosti in edges:
            self.Graph[fr].append([to,edgeCosti])

    def addEdge(self, edge: List[int]) -> None:
        fr,to,edgeCosti = edge
        self.Graph[fr].append([to,edgeCosti])

    def shortestPath(self, node1: int, node2: int) -> int:
        # n = len(self.Graph)
        distance = [float('inf')]* self.n
        heap = [[0 , node1]]
        distance[node1] = 0
        while heap:
            dist , node = heapq.heappop(heap)
            if node == node2:return dist
            for neigh , edge_cost in self.Graph[node]:
                new_dist = edge_cost+dist
                if new_dist < distance[neigh]:
                    distance[neigh] =  new_dist
                    heapq.heappush(heap , [new_dist , neigh])
        
        
        
        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
