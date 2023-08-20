# link   : https://leetcode.com/problems/sorting-three-groups/description/
# author : Mohamed Ibrahim

import bisect

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        longestNonDecreasing = []
        
        for num in nums:
            pos = bisect.bisect_right(longestNonDecreasing, num)
            
            if pos == len(longestNonDecreasing):
                longestNonDecreasing.append(num)
            else:
                longestNonDecreasing[pos] = num
            print(longestNonDecreasing)

        return len(nums) - len(longestNonDecreasing)
