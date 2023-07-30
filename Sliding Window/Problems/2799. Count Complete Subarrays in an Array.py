# link   : https://leetcode.com/problems/count-complete-subarrays-in-an-array/
# author : Mohamed Ibrahim

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        c=len(set(nums))
        n=len(nums)
        res=0
        for i in range(n):
            seen=set()
            for j in range(i,n):
                seen.add(nums[j])
                if(len(seen)==c):
                    res+=1
        return res

# Sliding Window

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        l,r = 0 , 0
        cnt , ln = 0 , len(set(nums))
        n =  len(nums)
        d = defaultdict(int)

        while r < n:
            d[nums[r]]+=1

            while len(d) == ln:
                cnt+= n - r

                d[nums[l]] -= 1
                if d[nums[l]] == 0:
                    del d[nums[l]]
                
                l+=1
            r+=1
        return cnt
        
