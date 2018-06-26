def equalPairOfBits(n, m):
	return [2 ** el for el in range(len(list(zip('{0:032b}'.format(n), '{0:032b}'.format(m)))[::-1])) if list(zip('{0:032b}'.format(n), '{0:032b}'.format(m)))[::-1][el][0] == list(zip('{0:032b}'.format(n), '{0:032b}'.format(m)))[::-1][el][1]][0]
