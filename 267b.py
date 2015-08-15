import fractions
import scipy as s
import pylab
import scipy.misc as m
import scipy.optimize as opt
import random

N = 1000
TARGET = 10**9
LIKEL = fractions.Fraction(1, 2**N)
MC_ROUNDS = int(1e4)

def kt(f):
	arithm = s.log10(TARGET) - N * s.log10(1-f)
	paron = s.log10((1+2*f)/(1-f))
	return int(s.ceil(arithm/paron))


fs = s.linspace(.1, .2, 2000)
kts = [kt(f) for f in fs]

def p(f):
	return LIKEL * sum(m.comb(N, k, exact=1) for k in xrange(kt(f), N+1))

def p_mc(f):
	hits = 0
	for mc_round in xrange(MC_ROUNDS):
		b = 1.
		for roll in s.rand(N):
			bet = b*f
			if roll < .5:
				b += bet
			else:
				b -= bet
		print b
		if b >= TARGET:
			hits += 1
	return float(hits) / MC_ROUNDS

		

print '{r:14.13f}'.format(r=float(p(.14)))
#print '{r:14.13f}'.format(r=float(p_mc(.2)))

pylab.plot(fs, kts); pylab.show()

