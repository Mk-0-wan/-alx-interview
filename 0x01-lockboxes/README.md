# LockBoxes
---
* Understanding iterables and the inner working of different datastructures in python.
* List, and Sets are the most focused subject in this code base.
* Learning how mutation works, and different ascpect which each one of the datastructres methodhas different from the other one.
* Overall this would be a the best code example i would recommmend for someone needing an Understanding of the difference between List and Sets in python.

---
## Code example
---
To solve this problem, we need to determine if all boxes can be unlocked given the initial state where only the first box (box 0) is unlocked. Here is the step-by-step process you should consider:

1. **Understand the Problem**:
    - You have `n` boxes, each potentially containing keys to other boxes.
    - Each box is identified by an integer index from 0 to n-1.
    - A key with a number can unlock the corresponding box.
    - The first box (index 0) is always unlocked.
    - The goal is to determine if you can unlock all the boxes starting from box 0.

2. **Initialize Data Structures**:
    - Use a set to keep track of boxes that have been unlocked (`unlocked`).
    - Use a queue (or stack) for the boxes that you can explore next (`to_explore`).

3. **Start with the First Box**:
    - Since the first box is already unlocked, add its keys to your exploration list and mark it as unlocked.

4. **Explore the Boxes**:
    - While there are boxes in the `to_explore` list:
        - Remove a box from `to_explore`.
        - Mark the box as unlocked.
        - Add all keys found in this box to the `to_explore` list (but only if those boxes haven't been unlocked yet).

5. **Check if All Boxes Are Unlocked**:
    - At the end of the exploration, compare the size of your `unlocked` set with the total number of boxes.
    - If all boxes are in the `unlocked` set, return `True`. Otherwise, return `False`.

6. **Edge Cases**:
    - Handle the scenario where there are no keys in any boxes.
    - Ensure that the function can handle cases where there are redundant keys (keys to already unlocked boxes).

Here is the detailed pseudocode:

1. Define the function `canUnlockAll(boxes)`.
2. Initialize a set `unlocked` and add the first box (index 0) to it.
3. Initialize a set `to_explore` with the keys found in the first box.
4. While there are items in `to_explore`:
    - Pop a key from `to_explore`.
    - If this key corresponds to a box that has not been unlocked:
        - Mark the corresponding box as unlocked.
        - Add all keys from this box to `to_explore` (only if they correspond to boxes that haven't been unlocked).
5. After the loop, check if the number of unlocked boxes is equal to the total number of boxes.
6. Return `True` if all boxes are unlocked, otherwise return `False`.

Here is the pseudocode in detail:

```python3
#pseudocode
def canUnlockAll(boxes):
    # Step 1: Initialize the unlocked set with the first box
    unlocked = set()
    unlocked.add(0)

    # Step 2: Initialize the to_explore set with the keys in the first box ( this is to avoid repettion and only have O(1) )
    to_explore = set(boxes[0])

    # Step 3: While there are boxes to explore
    while to_explore:
        # Pop a key from the to_explore set
        key = to_explore.pop()

        # ensure we are not outof bounds of the list and also appending correct keys only
        if key not in unlocked and key < len(boxes):
            unlocked.add(key)
            to_explore.update(key)

    # Step 4: Check if all boxes are unlocked
    return len(unlocked) == len(boxes)
```

By following these steps, you will systematically determine whether all boxes can be unlocked. This method ensures that you explore all possible keys and keep track of the unlocked boxes efficiently even with large datasets.
