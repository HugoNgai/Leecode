#!/usr/bin/env python
# encoding: utf-8


class Solution:
    def romanToInt(self, s: str) -> int:
        res, prev = 0, 0
        symbol_map = {'I': 1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D': 500, 'M': 1000}
        for i in s[::-1]:
            if symbol_map[i] < prev:
                res -= symbol_map[i]
            else:
                res += symbol_map[i]
            prev = symbol_map[i]
        return res