class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n , m = len(heights) , len(heights[0])
        minHeap = [[0 , 0 , 0]]
        visited = set()
        directions = [(0 , -1) , (0 , 1) , (-1 , 0) ,(1 , 0)]

        while minHeap:
            diff , i , j = heappop(minHeap)
            if i == n-1 and j == m-1:
                return diff
            if (i , j) in visited:continue
            visited.add((i , j))
            for x , y in directions:
                if i+x < 0 or j+y < 0 or i+x == n or j+y == m or (i+x , j+y) in visited:
                    continue
                heappush(minHeap , [max( diff, abs(heights[i][j]-heights[i+x][j+y])) , i+x , j+y])


        
