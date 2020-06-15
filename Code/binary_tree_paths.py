#!/usr/bin/env python
# encoding: utf-8


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        # 递归 时间复杂度O(n), 空间复杂度O(n)
        def construct_path(root, path):
            if not root:
                return

            path += str(root.val)
            if not root.left and not root.right:
                paths.append(path)
            path += '->'
            construct_path(root.left, path)
            construct_path(root.right, path)

        paths = []
        construct_path(root, '')
        return paths

        # 迭代 时间复杂度O(n), 空间复杂度O(n)
        if not root:
            return []

        paths = []
        stack = [(root, str(root.val))]

        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))

        return paths

