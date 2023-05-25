# link : https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/
# author : Mohamed Ibrahim

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = [(nums[i][0] , i , 0) for i in range(len(nums))]
        mx = max([ nums[i][0]  for i in range(len(nums))])
        heapq.heapify(heap)
        ans = [float('-inf') , float('inf')]

        while heap:
            left , order_in_list , order_in_nums = heapq.heappop(heap)
            if mx - left < ans[1] - ans[0]:
                ans[0],ans[1] = left,mx
            if order_in_nums == len(nums[order_in_list])-1:return ans
            shift_right = nums[order_in_list][order_in_nums+1]
            if shift_right > mx : mx = shift_right
            heapq.heappush(heap , ( shift_right , order_in_list , order_in_nums+1))
            
