import pylab, itertools, scipy, random
import scipy.misc as sm

def p_x_tries(x, T, raceto):
	b = int(scipy.ceil(float(raceto)/2**(T-1)))
	r = 1./2**T
	e = x - b
	p = r**b * (1-r)**e * (sm.comb(b+e-1, b-1, exact=0))
	return p

MAX_X = 1000
xs = range(1, MAX_X+1)

def payoff(T):
	return 2**(T-1)

class Strategy:
	def __init__(self, Ts, bp):
		assert len(Ts) == len(bp) + 1
		self.Ts = Ts
		self.targets = bp
		last_payoff = payoff(Ts[-1])
		self.targets.append(last_payoff)
		while sum(self.targets) < 100:
			self.targets[-1] += last_payoff
		assert sum(self.targets) >= 100
		assert all(t % payoff(T) == 0 for t, T in zip(self.targets, self.Ts))
	def __repr__(self):
		return '<Strategy: {Ts}, {targets}>'.format(
			Ts = self.Ts,
			targets = self.targets
		)

def p_b_wins(strategy, scorea = 0):
	# Equal to P(b<a).
	Ts = strategy.Ts
	targets = strategy.targets
	distr = None
	for T, target, i in zip(Ts, targets, itertools.count()):
		distrT = scipy.array([[p_x_tries(x, T, target) for x in xs]])
		if distr is not None:
			table = scipy.fliplr(scipy.dot(distr.T, distrT))
			distr = scipy.zeros((1, 2*MAX_X))
			for offseti, offset in enumerate(xrange(-(MAX_X-1), MAX_X)):
				distr[0, -offseti-1] = scipy.trace(table, offset)
			distr = distr[:,:MAX_X]
		else:
			distr = distrT
		assert distr[0,:i].sum() == 0

	E = (xs * distr[0,:]).sum()
	#pylab.bar(xs, distr[0,:]); pylab.show()
	distra = scipy.array([[p_x_tries(x, 1, 100 - scorea) for x in xs]])
	m = scipy.dot(distra.T, distr)
	p = 0.
	for offseti, offset in enumerate(xrange(-(MAX_X-1), 0)):
		p += scipy.trace(m, offset)

	return p


def p_b_wins_mc(strategy, scorea_at_start = 0):
	Ts = strategy.Ts
	targets = strategy.targets
	MC = 1*10**4
	r = random.random
	wins_of_b = 0
	for mc_round in xrange(MC):
		scorea = scorea_at_start
		scoreb = 0
		Tsi = iter(Ts)
		targetsi = iter(targets)
		T = Tsi.next()
		target = targetsi.next()
		while True:
			if r() < .5:
				scorea += 1
			if scorea >= 100:
				break
			if scoreb >= target:
				T = Tsi.next()
				target += targetsi.next()
			pb = 1./2**T
			if r() < pb:
				scoreb += payoff(T)
			if scoreb >= 100:
				wins_of_b += 1
				break
	return float(wins_of_b) / MC

# Best so far:
Ts = (1, 7)
bp = [36]
scorea = 0
#################

Ts = (1, 3)
bp = [36]
scorea = 0

strategy = Strategy(Ts, bp)
print strategy
print p_b_wins(strategy, scorea), p_b_wins_mc(strategy, scorea)
		
