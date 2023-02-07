# link : https://leetcode.com/problems/daily-temperatures/description/
# author : Mohamed Ibrahim


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for index, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                current = stack.pop()
                result[current] = index - current
            stack.append(index)
        return result



      
      
    
