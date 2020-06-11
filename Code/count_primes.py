#!/usr/bin/env python
# encoding: utf-8


class Solution:
    def countPrimes(self, n: int) -> int:
        res = [1] * n
        for i in range(2, math.ceil(math.sqrt(n))):
            if res[i] == 1:
                for j in range(i * i, n, i):
                    res[j] = 0

        return sum(res[2:n])
