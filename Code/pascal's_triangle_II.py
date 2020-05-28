#!/usr/bin/env python
# encoding: utf-8
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(1, rowIndex + 1):
            res.insert(0, 0)
            # 因为i行的数据长度为i+1, 所以j+1不会越界, 并且最后一个1不会被修改.
            for j in range(i):
                res[j] = res[j] + res[j + 1]
        return res


