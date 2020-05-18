#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            a = '0'
        if not b:
            b = '0'
        return bin(int(a, 2) + int(b, 2))[2:]
