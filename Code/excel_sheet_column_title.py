#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        while n > 0:
            if n % 26 != 0:
                res.insert(0, chr(n % 26 + 64))
            else:
                res.insert(0, "Z")
            n = int((n-1)/26)
        return "".join(res)
