#!/usr/bin/env python
# encoding: utf-8


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = int(1e9)
        max_price = 0
        for price in prices:
            max_price = max(price - min_price, max_price)
            min_price = min(price, min_price)
        return max_price
