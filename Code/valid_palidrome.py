#!/usr/bin/env python
# encoding: utf-8


class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        res = ''.join(re.findall(r'[a-zA-Z0-9]+', s))
        res = res.lower()
        return res == res[::-1]
