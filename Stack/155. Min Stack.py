# link   : https://leetcode.com/problems/min-stack/description/
# author : Mohamed Ibrahim


class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        cur_min = self.getMin()
        if cur_min == None or cur_min > val:
            cur_min = val
        self.s.append([val,cur_min])
    def pop(self) -> None:
        self.s.pop() 

    def top(self) -> int:
        if len(self.s) == 0:
            return None
        else:
            return self.s[len(self.s)-1][0]
    def getMin(self) -> int:
        if len(self.s) == 0:
            return None
        else:
            return self.s[len(self.s)-1][1]


# MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


