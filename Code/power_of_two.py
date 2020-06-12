#!/usr/bin/env python
# encoding: utf-8


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 二进制n, 如果是2的幂, 那么最高位为1, 其余位为0
        # 二进制n-1, 和n比较最高位为0, 其余为均为1
        # 做与运算结果一定为0
        return n > 0 and n & (n - 1) == 0

        # 方法二
        if n < 1:
            return False

        while n % 2 == 0:
            n /= 2

        return n == 1
