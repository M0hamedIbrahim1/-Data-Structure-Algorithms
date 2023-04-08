# link   : https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# author : Mohamed Ibrahim

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        num_to_char = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }

        def backtracing(i,cur_string):
            if len(cur_string) == len(digits):
                res.append(cur_string)
                return
            for c in num_to_char[digits[i]]:
                backtracing(i+1,cur_string+c)
        if digits:
            backtracing(0,"")
        return res
        
        
