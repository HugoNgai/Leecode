#!/usr/bin/env python
# encoding: utf-8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
        use queue to implement BFS, needs to record level(广度优先遍历)
    """
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue = collections.deque()
        queue.append((root, 0))
        res = []
        if not root:
            return res
        while queue:
            node, depth = queue.popleft()
            if node:
                if len(res) <= depth:
                    res.insert(0, [])

                res[-(depth + 1)].insert(0, node.val)
                queue.insert(0, (node.left, depth + 1))
                queue.insert(0, (node.right, depth + 1))



class Solution:
    """
    use stack to implement DFS, record depth(深度优先遍历)
    """
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        stack = [(root, 0)]
        while len(stack) > 0:
            node, depth = stack.pop()
            if node:
                if len(res) <= depth:
                    res.insert(0, [])
                res[-(depth+1)].append(node.val)
                stack.append((node.right, depth+1))
                stack.append((node.left, depth+1))
        return res


class Solution:
    """
    recursive DFS(递归深度有点遍历)
    """
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, depth, res):
        if root:
            if depth >= len(res):
                res.insert(0, [])
            res[-(depth+1)].append(root.val)
            self.dfs(root.left, depth+1, res)
            self.dfs(root.right, depth+1, res)
