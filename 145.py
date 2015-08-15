odds = set(str(d) for d in xrange(1, 10, 2))

def is_reversible(n):
	reverse = int(''.join(reversed(str(n))))

	s = n + reverse

	return all(c in odds for c in str(s))


#res = sum(1 for n in xrange(1, 10**9) if n % 10 != 0 and is_reversible(n))
res = sum(1 for n in xrange(1, 10**9))

print res
	
