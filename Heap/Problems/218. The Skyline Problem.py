# link   : https://leetcode.com/problems/the-skyline-problem/description/
# author : Mohamed Ibrahim

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        building = []
        for x,y,h in  buildings:
            building.append((x,-h,y))
        for x,y,h in  buildings:
            building.append((y,0,0))
        building.sort()

        available = [(0, float("inf"))]
        res = [(0,0)]

        for x,h,y in building:
            while available[0][1] <= x:
                heappop(available)
            if h:
                heappush(available,(h,y))

            if res[-1][1] != -available[0][0]:
                res.append((x , -available[0][0]))
        return res[1:]
        
        
