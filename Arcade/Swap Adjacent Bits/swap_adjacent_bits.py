def swapAdjacentBits(n):
	return int(''.join([j[::-1] for j in ['{0:032b}'.format(n)[i:i+2] for i in range(0, len('{0:032b}'.format(n)), 2)]]), 2)