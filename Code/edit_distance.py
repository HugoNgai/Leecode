#!/usr/bin/env python
# encoding: utf-8


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # def dp(i, j):
        #     if i == -1:
        #         return j + 1
        #     if j == -1:
        #         return i + 1

        #     if word1[i] == word2[j]:
        #         return dp(i - 1, j - 1)
        #     else:
        #         return min(
        #             dp(i, j - 1) + 1,   # insert
        #             dp(i - 1, j - 1) + 1,   # replace
        #             dp(i - 1, j) + 1    # delete
        #         )

        # return dp(len(word1) - 1, len(word2) - 1)

        n = len(word1)
        m = len(word2)

        # 有一个字符串为空串
        if n * m == 0:
            return n + m

        # DP 数组
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # 边界状态初始化
        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,
                        dp[i][j - 1] + 1,
                        dp[i - 1][j - 1] + 1
                    )

        return dp[n][m]

