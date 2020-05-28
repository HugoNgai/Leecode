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
    层次遍历，O(n)
    """
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        depth = 1
        queue = [root]
        while queue:
            length = len(queue)
            for i in range(length):
                p = queue.pop(0)
                if p.left is None and p.right is None:
                    return depth
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
            depth += 1

        return depth


class Solution:
    """
    递归，O(n)
    """
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left_depth = self.minDepth(root.left) + 1
        right_depth = self.minDepth(root.righr) + 1
        child_depth = min(left_depth, right_depth) if left_depth and right_depth else left_depth or right_depth
        return 1 + child_depth

