#!/usr/bin/env python
# encoding: utf-8


class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        # 快慢指针
        # 时间复杂度O(logn), 空间复杂度O(1)
        slow = n
        fast = get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1

        # hash
        # 时间复杂度O(logn), 空间复杂度O(1)
        res_set = set()
        while n != 1 and n not in res_set:
            res_set.add(n)
            n = get_next(n)
        return n == 1
