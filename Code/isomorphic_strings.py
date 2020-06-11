#!/usr/bin/env python
# encoding: utf-8


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        res = dict()
        for i in range(len(s)):
            if s[i] not in res:
                if t[i] in res.values():
                    return False
                else:
                    res[s[i]] = t[i]
            else:
                if res[s[i]] != t[i]:
                    return False
        return True


