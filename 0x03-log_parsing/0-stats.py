#!/usr/bin/python3
"""Where is the comment"""
import sys
import signal
from collections import Counter
import operator
from typing import Mapping

# Initialize global variables
stats_dct = Counter()
file_size = 0
interval = -1


def handler(signum, frame):
    _ = signal.Signals(signum).name
    _ = frame
    printer(file_size, stats_dct)
    sys.exit()


signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGQUIT, handler)


def printer(total_size: int, status_codes_counter: Mapping[int, int]) -> bool:
    """prints the required format to stdout
    Args:
        total_size (int): total value of all the first ten status code
        status_codes_counter (dict): key value pairs of the status code
        and their respective number of appearance
    """
    status_totals = sorted(status_codes_counter.items(),
                           key=operator.itemgetter(0))
    print("File size: {}".format(total_size))
    for code, count in status_totals:
        print("{}: {}".format(code, count))
    return (True)


if __name__ == '__main__':
    while True:
        try:
            logs = input()
            idx = logs.rfind('"')
            data = logs[idx + 1:].lstrip(" ").split(" ")
            file_size += int(data[1])
            stats_dct.update([int(data[0])])
            interval += 1
        except (ValueError, TypeError):
            continue
        # print(f"{stats_dct} -> {len(stats_dct)}")
        if interval % 10 == 0:
            printer(file_size, stats_dct)
