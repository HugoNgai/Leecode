#!/usr/bin/env python
# encoding: utf-8


import collections


class Solution:
    """
    哈希表方法，时间复杂度O(n), 空间复杂度O(n)
    """
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


class Solution:
    """
    排序法，时间复杂度O(nlogn), 空间复杂度O(logn)
    """
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]


class Solution:
    """
    Boyer-Moore投票算法，时间复杂度O(n), 空间复杂度O(1)
    """
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        counts = 0
        for i in nums:
            if counts == 0:
                candidate = i
            counts += (1 if i == candidate else -1)

        return candidate
