#!/usr/bin/env python
# encoding: utf-8


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = []
        self.b = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.a.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return
        if len(self.b) == 0:
            while len(self.a) != 0:
                self.b.append(self.a.pop())
        return self.b.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return
        if len(self.b) == 0:
            while len(self.a) != 0:
                self.b.append(self.a.pop())
        return self.b[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.a) == 0 and len(self.b) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
