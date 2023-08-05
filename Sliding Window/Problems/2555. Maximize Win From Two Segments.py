# link   : https://leetcode.com/problems/maximize-win-from-two-segments/description/
# author : Mohamed Ibrahim

class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        dp, left, ans = [0] * (len(prizePositions) + 1), 0, 0
        for right in range(len(prizePositions)):
            while prizePositions[right] - prizePositions[left] > k:
                left += 1
            dp[right + 1] = max(dp[right], right - left + 1)
            ans = max(ans, dp[left] + right - left + 1)
        print(dp)
        return ans

        #[1,1,2,2,2,2,3,3,7,13,13,13,13,13,15]
