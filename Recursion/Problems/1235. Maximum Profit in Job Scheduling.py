# link   : https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/
# author : Mohamed Ibrahim

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:


        startTime, endTime, profit = zip(*sorted(zip(startTime, endTime, profit)))
        d = {i : bisect_left(startTime,endTime[i]) for i in range(len(startTime))}
        cache = {}
        def dfs(indx):
            if indx in cache:
                return cache[indx]
            if indx >= len(profit):
                return 0
            cache[indx] = max(
                        profit[indx] + dfs(d[indx]) ,
                        dfs(indx+1)

                    )
            return cache[indx]

        return dfs(0)
        
