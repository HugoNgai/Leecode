#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ['(', '[', '{']
        right = [')', ']', '}']
        stack = []
        for ch in s:
            if ch in left:
                stack.append(ch)
            else:
                if len(stack) != 0 and stack[-1] == left[right.index(ch)]:
                    stack.pop()
                else:
                    return False
        return not stack
