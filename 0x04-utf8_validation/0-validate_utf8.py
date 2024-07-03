#!/usr/bin/python3
"""Utf8 Validation"""


def validUTF8(data):
    """Function the deterimines if a given data set represents
    valid UTF-8 encoding"""
    NOT_VALID = 1
    INVALID = 7
    ERROR = 8
    WRONG_BYTE_LENGTH = 5

    if data[0] >= 256:
        data = decode_utf8(data)

    iterable = iter(data)
    for idx in iterable:
        leading_one_bits = byte_array_count(idx)
        if leading_one_bits in [
                WRONG_BYTE_LENGTH,
                NOT_VALID,
                INVALID,
                ERROR
                ]:
            return False
        for _ in range(leading_one_bits - 1):
            nxt_iter = next(iterable, None)
            if nxt_iter is None or nxt_iter >> 6 != 0b10:
                return False
    return True


def byte_array_count(binary_data):
    """
    Count the number of leading 1 bits in each byte of a given byte array.

    This function calculates the number of leading 1
    bits (most significant bits) in each byte of the input list
    `binary_data`. This count is used to determine the number
    of 1-byte fields remaining, based on the bit pattern.

    Example:
    --------
    The byte 197 (binary: 11000101) has two leading 1 bits.

    Calling `byte_array_count([197, 130, 1])` would return 2 because:
        - 197 (binary: 11000101) has two leading 1 bits.
        - 130 (binary: 10000010) has one leading 1 bit.
        - 1 (binary: 00000001) has no leading 1 bits.

    Detailed Bitmask Demonstration:
    --------------------------------
    The function uses bitmasking to count the number of leading 1 bits.
    The demo below shows how the bitmasking
    works for various bit positions:

    Bitmasking:
    -----------
        print(bin(0b1111111 >> 7 & ~1), 1)  -> '0b0', 1
        print(bin(0b1111111 >> 6 & ~1), 2)  -> '0b0', 2
        print(bin(0b1111111 >> 5 & ~1), 3)  -> '0b10', 3
        print(bin(0b1111111 >> 4 & ~1), 4)  -> '0b110', 4
        print(bin(0b1111111 >> 3 & ~1), 5)  -> '0b1110', 5
        print(bin(0b1111111 >> 2 & ~1), 6)  -> '0b11110', 6
        print(bin(0b1111111 >> 1 & ~1), 7)  -> '0b111110', 7
        print(bin(197 >> 7), 1)             -> '0b1', 1
        print(bin(197 >> 6), 2)             -> '0b11', 2
        print(bin(197 >> 5), 3)             -> '0b110', 3
        print(bin(197 >> 4), 4)             -> '0b1100', 4
        print(bin(197 >> 3), 5)             -> '0b11000', 5
        print(bin(197 >> 2), 6)             -> '0b110001', 6
        print(bin(197 >> 1), 7)             -> '0b1100010', 7

    The results demonstrate how the bitmasking shifts and counts
    the number of leading 1 bits in each position.

    Parameters:
    -----------
    binary_data : list of int
        The input list of byte values (0-255) to analyze.

    Returns:
    --------
    int
        The count of bytes with a specific number of leading 1 bits.
    """

    BIT_FIELD = 8
    mask = 0b11111111
    for i in range(BIT_FIELD):
        if binary_data >> (7 - i) == mask >> (7 - i) & ~1:
            return i
    return BIT_FIELD


def decode_utf8(data):
    """decodes data to valid Utf8 for digis out of range"""
    new_data = [
            val % 256
            for val in data
            ]
    return new_data
