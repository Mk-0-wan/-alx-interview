#!/usr/bin/python3
"""Coin Change Problem"""


from collections import deque


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Queue for BFS
    queue = deque([(0, 0)])
    visited = set([0])

    while queue:
        current_amount, num_coins = queue.popleft()

        for coin in coins:
            new_amount = current_amount + coin

            if new_amount == total:
                return num_coins + 1
            if new_amount < total and new_amount not in visited:
                visited.add(new_amount)
                queue.append((new_amount, num_coins + 1))

    return -1
