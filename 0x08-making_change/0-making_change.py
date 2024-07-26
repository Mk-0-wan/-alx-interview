#!/usr/bin/python3
"""Coin Change Problem"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    
    # Initialize DP table
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Fill DP table
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return result
    return dp[total] if dp[total] != float('inf') else -1
