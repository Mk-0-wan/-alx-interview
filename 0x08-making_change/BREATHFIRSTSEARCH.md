### README

# Coin Change Problem

## Description

This repository contains the implementation of a function to solve the coin change problem using a Breadth-First Search (BFS) approach. The goal is to determine the fewest number of coins needed to meet a given amount total. If it's not possible to meet the total with the given coins, the function returns -1.

## Function Prototype

```python
def makeChange(coins, total):
```

### Parameters

- `coins`: A list of integers representing the values of the coins in your possession.
- `total`: An integer representing the total amount of money to be made.

### Return Value

- Returns the fewest number of coins needed to meet the given total.
- If the total is 0 or less, returns 0.
- If the total cannot be met by any number of coins, returns -1.

## Usage

### Example

```python
# Example usage:
coins = [1, 2, 5]
total = 11
print(makeChange(coins, total))  # Output: 3 (5+5+1)
```

### Explanation of the Example

- Given coins: `[1, 2, 5]`
- Given total: `11`
- The minimum number of coins needed to make the total 11 is 3 (using two 5-value coins and one 1-value coin).

## Algorithm Explanation

### Breadth-First Search (BFS) Approach

1. **Base Cases**:
    - If the total is 0, the function returns 0 because no coins are needed.
    - If the total is less than or equal to 0, the function returns 0 because a negative or zero amount doesn't require any coins.
2. **BFS Initialization**:
    - A `queue` is initialized with `(0, 0)`, representing an amount of 0 with 0 coins used.
    - A `visited` set is initialized with `0` to keep track of the amounts that have already been considered.
3. **BFS Execution**:
    - Use a `while` loop to process each state in the `queue`.
    - For each state, try adding each coin to the current amount.
    - If the new amount equals the target `total`, return the number of coins used.
    - If the new amount is less than the target and hasn't been visited, add it to the `queue` and `visited` set.
4. **Result**:
    - If the `queue` is exhausted without finding the target amount, return -1.

### Complexity

- **Time Complexity**: O(n * m), where n is the number of coins and m is the total amount.
- **Space Complexity**: O(m), where m is the total amount.

# Example usage:
coins = [1, 2, 5]
total = 11
print(makeChange(coins, total))  # Output: 3 (5+5+1)
```

## Testing

To test the function, you can use the provided example or create your own test cases by changing the values of `coins` and `total`.

```python
# Test cases
print(makeChange([1, 2, 5], 11))  # Expected output: 3
print(makeChange([2], 3))         # Expected output: -1
print(makeChange([1, 2, 5], 0))   # Expected output: 0
print(makeChange([1, 2, 5], -5))  # Expected output: 0
print(makeChange([1], 1))         # Expected output: 1
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
