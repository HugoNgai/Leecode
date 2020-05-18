#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret = ''
        for s in zip(*strs):
            if len(set(s)) > 1:
                break
            ret += s[0]
        return ret
