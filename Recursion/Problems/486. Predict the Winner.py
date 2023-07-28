# link : https://leetcode.com/problems/predict-the-winner/description/
# author : Mohamed Ibrahim

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def dfs(i: int, j: int) -> int:
            if i == j:
                return nums[i]
            return max(nums[i] - dfs(i + 1, j), nums[j] - dfs(i, j - 1))
        x = dfs(0, len(nums) - 1)
        return dfs(0, len(nums) - 1) >= 0
