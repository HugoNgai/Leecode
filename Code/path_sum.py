#!/usr/bin/env python
# encoding: utf-8
# Definition for a binary tree node.


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    递归，O(n)
    """
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        sum -= root.val

        if root.left is None and root.right is None:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


class Solution:
    """
    非递归，使用栈，O(n)
    """
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        stack = [(root, sum - root.val)]
        while stack:
            node, cur_sum = stack.pop()
            if node.left is None and node.right is None and cur_sum == 0:
                return True
            if node.left:
                stack.append((node.left, cur_sum - node.left.val))
            if node.right:
                stack.append((node.right, cur_sum - node.right.val))

        return False
