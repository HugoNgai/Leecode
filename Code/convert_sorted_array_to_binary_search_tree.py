#!/usr/bin/env python
# encoding: utf-8
"""
    根据中序遍历有序的特点，选取有序数组的中间值作为根节点
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    """
    最左原则，偶数个数时选取靠左的结点为根节点
    """
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)


class Solution:
    """
    最右原则，偶数个数时选取靠右的结点为根节点
    """
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            if mid % 2:
                mid += 1

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)


