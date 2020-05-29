#!/usr/bin/env python
# encoding: utf-8


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min_price = int(1e9)
        # max_price = 0
        # res = [0]
        # for price in prices:
        #     max_price = max(price - min_price, max_price)
        #     if max_price > 0:
        #         res.append(max_price)
        #         min_price = int(1e9)
        #         max_price = 0
        #     min_price = min(price, min_price)
        # return sum(res)
        max_profit = 0
        for i in range(len(prices)):
            if i + 1 < len(prices):
                if prices[i] < prices[i + 1]:
                    max_profit += prices[i + 1] - prices[i]
        return max_profit

