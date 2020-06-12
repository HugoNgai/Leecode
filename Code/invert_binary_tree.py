#!/usr/bin/env python
# encoding: utf-8


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 迭代
        if not root:
            return None
        q = deque()
        q.append(root)
        while q:
            cur = q.popleft()
            tmp = cur.left
            cur.left = cur.right
            cur.right = tmp
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        return root

        # 递归
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root
