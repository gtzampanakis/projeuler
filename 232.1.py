import pylab, itertools, scipy, random
import scipy.misc as sm

def p_x_tries(x, T, raceto):
	b = int(scipy.ceil(float(raceto)/2**(T-1)))
	r = 1./2**T
	e = x - b
	p = r**b * (1-r)**e * (sm.comb(b+e-1, b-1, exact=0))
	return p

T_strategy = [3, 6, 7]
MAX_X = 1000
xs = range(1, MAX_X+1)
distra = scipy.array([[p_x_tries(x, 1, 100) for x in xs]])

def payoff(T):
	return 2**(T-1)

def p_b_wins():
	# Equal to P(b<a).
	T=6; distrb3 = scipy.array([[p_x_tries(x, T, payoff(T)) for x in xs]])
	T=7; distrb6 = scipy.array([[p_x_tries(x, T, payoff(T)) for x in xs]])
	T=3; distrb7 = scipy.array([[p_x_tries(x, T, payoff(T)) for x in xs]])

	table36 = scipy.fliplr(scipy.dot(distrb3.T, distrb6))
	distr36 = scipy.zeros((1, 2*MAX_X)) # First element should be 0.
	for offseti, offset in enumerate(xrange(-(MAX_X-1), MAX_X)):
		distr36[0,-offseti-1] = scipy.trace(table36, offset)
	del table36
	distr36 = distr36[:,:MAX_X]
	assert distr36[0,0] == 0

	table367 = scipy.fliplr(scipy.dot(distr36.T, distrb7))
	del distr36
	distr367 = scipy.zeros((1, 2*MAX_X)) # First two elements should be 0.
	for offseti, offset in enumerate(xrange(-(MAX_X-1), MAX_X)):
		distr367[0,-offseti-1] = scipy.trace(table367, offset)
	del table367
	distr367 = distr367[:,:MAX_X]
	assert distr367[0,0] == 0 and distr367[0,1] == 0

	#pylab.bar(xs, distr367[0,:]); pylab.show()
	m = scipy.dot(distra.T, distr367)
	p = 0.
	for offseti, offset in enumerate(xrange(-(MAX_X-1), 0)):
		p += scipy.trace(m, offset)

	return p


def p_b_wins_mc():
	MC = 2*10**4
	r = random.random
	wins_of_b = 0
	for mc_round in xrange(MC):
		scorea = 0
		scoreb = 0
		while True:
			if r() < .5:
				scorea += 1
			if scorea >= 100:
				break
			if scoreb == 4:
				T = 6
			elif scoreb == 36:
				T = 7
			else:
				T = 3
			pb = 1./2**T
			sb = 2**(T-1)
			if r() < pb:
				scoreb += sb
			if scoreb >= 100:
				wins_of_b += 1
				break
	return float(wins_of_b) / MC

print p_b_wins(), p_b_wins_mc()
		
if 0:
	for T in range(1, 20):
		print T, 2**(T-1), p_b_wins(T), p_b_wins_mc(T)

#pylab.bar(xs, [p_x_tries(x, 7, 100) for x in xs])
#pylab.show()
