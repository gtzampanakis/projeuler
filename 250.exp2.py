import itertools, math, fractions

def ss(m, l):
	lenl = len(l)
	total = 0
	for k in xrange(lenl+1):
		for subs in itertools.combinations(l, k):
			if sum(subs) % m == 0 and sum(subs) > 0:
				total += 1
	return total

for rmax in itertools.count(1):
	A = [k**k for k in xrange(1, rmax+1)]
	ts = 2 ** len(A)
	ms = [250]
	occs = [ss(m, A) for m in ms]
	for m, ss_ in zip(ms, occs):
		ss_ = ss(m, A)
		print 'Subs of 1^1...{m}^{m} that sum to a mult of {u:>3}: {ss:>5}, fraction: {f}'.format(
					m = rmax,
					u = m,
					ss = ss_,
					f = fractions.Fraction(ss_, ts),
		)
	#print 'Total subsets: {ts}, sum of A: {sa}'.format(
	#		ts = ts,
	#		sa = sum(A),
	#)

