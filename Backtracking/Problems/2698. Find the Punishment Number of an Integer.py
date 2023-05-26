# link   : https://leetcode.com/contest/weekly-contest-346/problems/find-the-punishment-number-of-an-integer/
# author : Mohamed Ibrahim

class Solution:
    def punishmentNumber(self, n: int) -> int:
        self.res = False
        def backtrack(start,num,target):
            if start == len(num) and target == 0:
                self.res = True
            for i in range(start, len(num)):
                current_num = int(num[start:i+1])
                backtrack(i+1,num, target - current_num)

        ans = 0
        for i in range(1 , n+1):
            self.res = False
            backtrack(0 , str(i*i) , i)
            if self.res :ans+=i*i
        return ans 
        
