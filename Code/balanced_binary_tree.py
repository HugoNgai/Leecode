#!/usr/bin/env python
# encoding: utf-8
"""
    两种解法，自顶向下和自底向上，时间复杂度：O(nlogn), O(n)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    """
    自底向上, O(n)
    """
    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedHelper(root)[0]

    def isBalancedHelper(self, root):
        if not root:
            return True, -1

        leftBalance, leftHeight = self.isBalancedHelper(root.left)
        if not leftBalance:
            return False, 0
        rightBalance, rightHeight = self.isBalancedHelper(root.right)
        if not rightBalance:
            return False, 0

        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)


class Solution:
    """
    自顶向下，O(nlogn)
    """
    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root):
        return abs(self.height(root.left) - self.height(root.right)) < 2 \
               and self.isBalanced(root.left) and self.isBalanced(root.right)
