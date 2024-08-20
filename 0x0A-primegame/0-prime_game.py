#!/usr/bin/python3

# Game: Prime Game
# Players: Maria and Ben
# Rules: Players take turns choosing a prime
# number and removing it and its multiples from the set
# Winner: The player who cannot make a move loses

def isWinner(x, nums):
    """
    Determines the winner of the Prime Game for multiple rounds.
    Args:
    x (int): The number of rounds to play
    nums (list): A list of integers,
        each representing the upper bound (n) for a round

    Returns:
    str or None: The name of the player who won the most
        rounds, or None if it's a tie
    """

    def is_prime(n):
        """
        Checks if a number is prime.

        Args:
        n (int): The number to check

        Returns:
        bool: True if n is prime, False otherwise
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def play_game(n):
        """
        Simulates a single game and determines the winner.

        Args:
        n (int): The upper bound of the set of numbers for this game
        Returns:
        bool: True if Maria wins, False if Ben wins
        """
        # Count the number of primes up to n
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        # Maria wins if the number of primes is odd (she goes first)
        return len(primes) % 2 == 1

    # Validate input
    if not nums or x != len(nums):
        return None

    # Count wins for Maria (Ben's wins = total games - Maria's wins)
    maria_wins = sum(play_game(num) for num in nums)
    ben_wins = x - maria_wins

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
