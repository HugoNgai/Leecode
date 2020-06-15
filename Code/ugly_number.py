#!/usr/bin/env python
# encoding: utf-8


class Solution:
    def isUgly(self, num: int) -> bool:
        if num < 0:
            return False

        while True:
            last = num
            if num % 2 == 0:
                num /= 2
            if num % 3 == 0:
                num /= 3
            if num % 5 == 0:
                num /= 5
            if num == 1:
                return True
            if num == last:
                return False

