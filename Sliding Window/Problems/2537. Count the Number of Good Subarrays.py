# link   : https://leetcode.com/problems/count-the-number-of-good-subarrays/description/
# author : Mohamed Ibrahim


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
 #   [3,1,4,3,2,2,4,1]
        counter = defaultdict(int)
        l , res , cnt = 0 , 0 ,0

        for i in range(len(nums)):
            cnt += counter[nums[i]]
            counter[nums[i]] += 1

            while cnt >= k:
                counter[nums[l]] -= 1
                cnt -= counter[nums[l]] 
                l+=1
            # print(l)
            res+=l
        return res
