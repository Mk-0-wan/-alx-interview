### README

# Coin Change Problem

## Description

This repository contains the implementation of a function to solve the coin change problem. The goal is to determine the fewest number of coins needed to meet a given amount total using dynamic programming. If it's not possible to meet the total with the given coins, the function returns -1.

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

### Dynamic Programming Approach

1. **Base Cases**:
    - If the total is 0, the function returns 0 because no coins are needed.
    - If the total is less than 0, the function returns 0 because a negative amount doesn't make sense.
2. **Dynamic Programming Table**:
    - A list `dp` is created where `dp[i]` stores the fewest number of coins needed to make the amount `i`.
    - `dp[0]` is initialized to 0 because no coins are needed to make the amount 0.
    - All other values in `dp` are initialized to infinity (a large number) since the fewest number of coins for those amounts is unknown initially.
3. **Filling the DP Table**:
    - For each coin in the list of coins, the `dp` table is updated.
    - For each amount from the coin's value to the total, the `dp` value is updated by taking the minimum of the current `dp` value or the `dp` value of (current amount - coin's value) + 1.
4. **Result**:
    - The result is in `dp[total]`. If it's still infinity, the function returns -1 because it's not possible to make that amount with the given coins. Otherwise, it returns the value in `dp[total]`.

### Complexity

- **Time Complexity**: O(n * m), where n is the number of coins and m is the total amount.
- **Space Complexity**: O(m), where m is the total amount.

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

