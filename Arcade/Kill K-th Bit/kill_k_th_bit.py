def killKthBit(n, k):
    return int((bin(n)[2:][::-1][0:k-1] + '0' + bin(n)[2:][::-1][k:])[::-1], 2)
