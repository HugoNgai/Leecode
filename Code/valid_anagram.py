#!/usr/bin/env python
# encoding: utf-8


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # 排序 时间复杂度O(nlogn), 空间复杂度O(1)
        return sorted(s) == sorted(t)

        # 哈希表 时间复杂度O(n), 空间复杂度O(n)
        if len(s) != len(t):
            return False

        res = {}
        for i in range(len(s)):
            if s[i] in res:
                res[s[i]] += 1
            else:
                res[s[i]] = 1

        for i in range(len(t)):
            if t[i] in res:
                res[t[i]] -= 1
            else:
                res[t[i]] = 1

        for i in res.values():
            if i != 0:
                return False

        return True

