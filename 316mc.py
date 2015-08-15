import random, itertools

digits = range(0, 10)

n = 12

ndigits = [int(c) for c in str(n)]

sr = [None for _ in xrange(len(str(n)))]

ks = 0
for mci in itertools.count(1):
	for i in itertools.count(1):
		r = random.choice(digits)

		del sr[0]
		sr.append(r)

		if sr == ndigits:
			ks += (i - len(sr) + 1)
			break

	if mci % 100 == 0:
		print n, float(ks) / mci


