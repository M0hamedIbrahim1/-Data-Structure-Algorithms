# link : https://leetcode.com/problems/implement-stack-using-queues/description/

from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        tmp = deque([x])
        tmp.extend(self.queue)
        self.queue = tmp
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0
