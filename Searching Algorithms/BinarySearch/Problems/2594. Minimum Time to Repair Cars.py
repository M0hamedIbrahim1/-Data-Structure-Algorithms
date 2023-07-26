# link : https://leetcode.com/problems/minimum-time-to-repair-cars/description/
# author : Mohamed Ibrahim

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def cal(minutes):
            cars = 0
            for rank in ranks:
                cars += math.floor((minutes / rank) ** 0.5)
            return cars

        lo = 1
        hi = min(ranks) * cars * cars
        while lo < hi:
            mi = lo + (hi-lo) // 2
            x = cal(mi)
            print(x , mi)
            if x < cars:
                lo = mi + 1
            else:
                hi = mi

        return lo

        
