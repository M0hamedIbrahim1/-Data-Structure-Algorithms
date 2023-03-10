# link   : https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/
# author : Mohamed Ibrahim


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        dist =[[int(1e9)] * n for i in range(n)]

        for i in range(n):
            dist[i][i] = 0 

        for i,j,d in edges:
            dist[i][j] =  dist[j][i] = d

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j] , dist[i][k] + dist[k][j])

        lst_validPath = [[] for i in range(n)]
        city_min_cnt = int(1e9)

        for i in range(n):
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    lst_validPath[i].append(j)

            if len(lst_validPath[i]):
                city_min_cnt = min(city_min_cnt,len(lst_validPath[i]))
        res = []        
        for i in range(n):
            if len(lst_validPath[i]) == city_min_cnt:
                res.append(i)
        return max(res)


