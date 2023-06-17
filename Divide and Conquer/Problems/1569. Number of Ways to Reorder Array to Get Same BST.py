# link : https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/description/
# author : Mohamed Ibrahim

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10 ** 9 +7
        def dfs(arr):
            if len(arr) <3:
                return 1
            root = arr[0]
            N = len(arr)
            left = [arr[i] for i in range(1, N) if arr[i] < root]
            right = [arr[i] for i in range(1, N) if arr[i] > root]
            # print(comb(N-1, len(left)))
            return dfs(left) * dfs(right) * comb(N-1, len(left)) % MOD
        return dfs(nums) % MOD - 1
