#!/usr/bin/python3
"""LockBoxes Algorithm"""
from typing import List


def canUnlockAll(boxes: List[int]) -> bool:
    """Returns true if all the boxes can be opened else false"""
    # holding the unique index of the array
    unlocked = set()
    # initialize it to zero to hold the index of the first elem
    unlocked.add(0)
    # get the first unlocked box
    to_explore = set(boxes[0])

    while to_explore:
        # to move on to the index of the next unlocked box
        key = to_explore.pop()
        # iterate over a box with more than one key
        if key not in unlocked and key < len(boxes):
            unlocked.add(key)
            to_explore.update(boxes[key])

    return len(unlocked) == len(boxes)
