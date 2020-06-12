#!/usr/bin/env python
# encoding: utf-8


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = dict()
        for i in range(len(nums)):
            if res.get(nums[i]):
                return True
            res[nums[i]] = 1
        return False
