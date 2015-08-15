import fractions
import scipy.misc as m
import scipy.optimize as opt

TURNS = 1000
TARGET = 10**9
LIKEL = fractions.Fraction(1, 2**TURNS)

def R(k, f):
	return (1+f)**k * (1-f)**(TURNS-k)

def p_k(k):
	return LIKEL * m.comb(TURNS, k, exact = 1)
ps = [p_k(k) for k in xrange(TURNS+1)]

def p_billion(f):
	rs = [R(k, f) for k in xrange(TURNS+1)]
	s = 0
	for r, p in zip(rs, ps):
		if r >= TARGET:
			s += p
	return s

if 0:
	print opt.brute(
		lambda f: -p_billion(f), 
		ranges = ((.0001, .99999)),
		Ns = 100,
	)

#e = 1./10
#k = .0001
#while k < 1:
#	print k, p_billion(k)
#	k += e

arg = fractions.Fraction(22, 100)
print '{r:14.12f}'.format(r=float(p_billion(arg)))

