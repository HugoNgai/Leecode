#!/usr/bin/env python
# encoding: utf-8

"""
    思路：杨辉三角可以通过错位相加等下一列
    e.g：   1，
          1，1
        1，2，1
    1，3，3，1 = 0，1，2，1 + 1，2，1，0

"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        while len(res) < numRows:
            new_row = [a + b for a, b in zip([0] + res[-1], res[-1] + [0])]
            res.append(new_row)
        return res


