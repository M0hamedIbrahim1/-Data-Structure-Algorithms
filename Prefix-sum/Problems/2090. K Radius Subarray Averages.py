# link   : https://leetcode.com/problems/k-radius-subarray-averages/description/
# author : Mohamed Ibrahim

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        n = len(nums)
        averages = [-1] * n

        if 2 * k + 1 > n:
            return averages

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        for i in range(k, n - k):
            leftBound, rightBound = i - k, i + k
            subArraySum = prefix[rightBound + 1] - prefix[leftBound]
            average = subArraySum // (2 * k + 1)
            averages[i] = average

        return averages
