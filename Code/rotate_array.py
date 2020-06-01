#!/usr/bin/env python
# encoding: utf-8
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        self.swap(nums, 0, len(nums) - 1)
        self.swap(nums, 0, k - 1)
        self.swap(nums, k, len(nums) - 1)

    def swap(self, nums, l, r):
        while (l < r):
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
            l += 1
            r -= 1

