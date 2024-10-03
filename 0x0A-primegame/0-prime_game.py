
#!/usr/bin/python3

"""
Game: Prime Game
Players: Maria and Ben
Rules: Players take turns choosing a prime
number and removing it and its multiples from the set
Winner: The player who cannot make a move loses
"""


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game for multiple rounds.
    Args:
    x (int): The number of rounds to play
    nums (list): A list of integers, each representing
        the upper bound (n) for a round
    Returns:
    str or None: The name of the player who won the most rounds,
        or None if it's a tie
    """

    def sieve_of_eratosthenes(n):
        """
        Generates a list of prime numbers up to n using the
            Sieve of Eratosthenes algorithm.

        Args:
        n (int): The upper bound of the range to check for primes

        Returns:
        list: A boolean list where True indicates a prime number
        """
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i*i, n + 1, i):
                    primes[j] = False
        return primes

    # Validate input
    if not nums or x != len(nums):
        return None

    # Find the maximum number in nums to determine
    # the range for prime calculation
    max_num = max(nums)

    # Generate a list of primes up to max_num
    is_prime = sieve_of_eratosthenes(max_num)

    # Precompute the count of primes up to each number
    prime_count = [0] * (max_num + 1)
    for i in range(2, max_num + 1):
        prime_count[i] = prime_count[i-1]
        if is_prime[i]:
            prime_count[i] += 1

    # Count Maria's wins
    # Maria wins a game if the count of primes up to n is odd
    maria_wins = sum(prime_count[n] % 2 == 1 for n in nums)

    # Calculate Ben's wins
    ben_wins = x - maria_wins

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
