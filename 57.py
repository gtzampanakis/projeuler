import fractions

def nd(n):
	return len(str(n))

fra = fractions.Fraction(1, 2)

n = 0
for i in xrange(2, 1001):
	fra = fractions.Fraction(1, 2 + fra)
	if nd((fra+1).numerator) > nd((fra+1).denominator):
		n += 1

print n


