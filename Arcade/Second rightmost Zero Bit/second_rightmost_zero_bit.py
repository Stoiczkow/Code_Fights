def secondRightmostZeroBit(n):
    return 2 ** ((bin(n)[2:][::-1][0: bin(n)[2:][::-1].index("0")] + bin(n)[2:][::-1][bin(n)[2:][::-1].index("0") + 1:]).index('0') + 1)