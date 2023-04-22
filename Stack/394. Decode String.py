# link   : https://leetcode.com/problems/decode-string/description/
# author : Mohamed Ibrahim


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_string , num = "" , 0
        for i in range(len(s)):
            if s[i] == '[':
                stack.append(cur_string)
                stack.append(num)
                cur_string = ""
                num = 0
            elif s[i] == ']':
                n = stack.pop()
                prev_string = stack.pop()

                cur_string =  prev_string + n*cur_string
            elif s[i].isdigit():
                num = num*10 + int(s[i])
            else:
                cur_string +=s[i]
        return cur_string
        
        
